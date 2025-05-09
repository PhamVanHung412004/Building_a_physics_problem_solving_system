import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize Flask app and SQLAlchemy
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # needed for url_for to generate with https

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///physics_bot.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)

# Configure login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import models after db initialization to avoid circular imports
with app.app_context():
    from models import User, ChatMessage
    db.create_all()

from google_auth import google_auth
from physics_bot import get_physics_response

# Register blueprints
app.register_blueprint(google_auth)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('chat'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Check if email already exists
        user_by_email = User.query.filter_by(email=email).first()
        if user_by_email:
            flash('Email already registered.', 'danger')
            return render_template('register.html')
        
        # Check if username already exists
        user_by_username = User.query.filter_by(username=username).first()
        if user_by_username:
            flash('Username already taken.', 'danger')
            return render_template('register.html')
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html', username=current_user.username)

@app.route('/api/chat', methods=['POST'])
@login_required
def process_message():
    data = request.json
    message = data.get('message', '').strip()
    
    if not message:
        return {'error': 'Empty message'}, 400
    
    # Save user message to database
    user_message = ChatMessage(
        user_id=current_user.id,
        message=message,
        is_from_user=True
    )
    db.session.add(user_message)
    
    # Get response from physics bot
    bot_response = get_physics_response(message)
    
    # Save bot response to database
    bot_message = ChatMessage(
        user_id=current_user.id,
        message=bot_response,
        is_from_user=False
    )
    db.session.add(bot_message)
    db.session.commit()
    
    return {
        'response': bot_response,
        'timestamp': user_message.timestamp.isoformat()
    }

@app.route('/api/chat/history', methods=['GET'])
@login_required
def get_chat_history():
    # Get unique conversations based on timestamps
    # Group by timestamp date, get first user message for each conversation
    user_messages = db.session.query(
        db.func.DATE(ChatMessage.timestamp).label('date'),
        db.func.MIN(ChatMessage.id).label('first_id')
    ).filter(
        ChatMessage.user_id == current_user.id,
        ChatMessage.is_from_user == True
    ).group_by(
        db.func.DATE(ChatMessage.timestamp)
    ).order_by(
        db.func.DATE(ChatMessage.timestamp).desc()
    ).all()
    
    # Fetch the actual messages
    history = []
    for date, first_id in user_messages:
        first_message = ChatMessage.query.get(first_id)
        if first_message:
            history.append({
                'date': date.strftime('%Y-%m-%d'),
                'preview': first_message.message[:50] + ('...' if len(first_message.message) > 50 else ''),
                'timestamp': first_message.timestamp.isoformat()
            })
    
    return {'history': history}

@app.route('/api/chat/messages/<date>', methods=['GET'])
@login_required
def get_chat_messages_by_date(date):
    try:
        # Validate date format (YYYY-MM-DD)
        datetime.strptime(date, '%Y-%m-%d')
        
        # Get all messages for the specified date
        start_date = f"{date} 00:00:00"
        end_date = f"{date} 23:59:59"
        
        messages = ChatMessage.query.filter(
            ChatMessage.user_id == current_user.id,
            ChatMessage.timestamp >= start_date,
            ChatMessage.timestamp <= end_date
        ).order_by(ChatMessage.timestamp).all()
        
        # Format messages for response
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({
                'id': msg.id,
                'message': msg.message,
                'is_from_user': msg.is_from_user,
                'timestamp': msg.timestamp.isoformat()
            })
        
        return {'messages': formatted_messages}
    
    except ValueError:
        # Invalid date format
        return {'error': 'Invalid date format. Use YYYY-MM-DD.'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
