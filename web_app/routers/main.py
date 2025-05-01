from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import User, Message, ContactMessage
from forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required
import logging

@app.route('/')
def index():
    """Render the homepage with the chatbot interface."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    """Handle user logout."""
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/about')
def about():
    """Render the about page with information about the chatbot."""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle the contact form submission."""
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')
            
            # Validate the form data
            if not all([name, email, subject, message]):
                flash('All fields are required.', 'danger')
                return redirect(url_for('contact'))
            
            # Save the contact message to the database
            contact_message = ContactMessage(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            db.session.add(contact_message)
            db.session.commit()
            
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            logging.error(f"Error processing contact form: {str(e)}")
            flash('An error occurred while sending your message. Please try again.', 'danger')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/api/chat', methods=['POST'])
@login_required
def chat():
    """API endpoint for the chatbot. Requires authentication."""
    try:
        message = request.json.get('message', '')
        if not message:
            return jsonify({'error': 'Message is required.'}), 400
        
        # This is a simple response for demonstration
        # In a real application, you would integrate with a physics chatbot backend
        response = generate_physics_response(message)
        
        # Save the user's message to the database
        user_message = Message(
            content=message,
            user_id=current_user.id,
            is_bot=False
        )
        
        # Save the bot's response to the database
        bot_message = Message(
            content=response,
            user_id=current_user.id,
            is_bot=True
        )
        
        db.session.add(user_message)
        db.session.add(bot_message)
        db.session.commit()
        
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error in chat API: {str(e)}")
        return jsonify({'error': 'An error occurred processing your request.'}), 500

def generate_physics_response(message):
    """Generate a simple physics-related response based on the input message."""
    message = message.lower()
    
    # Simple keyword-based responses
    if any(word in message for word in ['newton', 'gravity', 'force']):
        return "Newton's laws of motion describe the relationship between an object and the forces acting upon it. F=ma is the most famous equation from these laws."
    elif any(word in message for word in ['einstein', 'relativity', 'e=mc2']):
        return "Einstein's theory of relativity revolutionized our understanding of space and time. E=mc² states that energy and mass are interchangeable."
    elif any(word in message for word in ['quantum', 'particle', 'wave']):
        return "Quantum mechanics is a fundamental theory in physics that describes nature at the atomic and subatomic scales. It introduces concepts like wave-particle duality."
    elif any(word in message for word in ['thermo', 'heat', 'temperature']):
        return "Thermodynamics is the branch of physics dealing with heat and temperature and their relation to energy, work, radiation, and properties of matter."
    else:
        return "I'm your physics assistant. You can ask me about Newton's laws, Einstein's relativity, quantum mechanics, thermodynamics, and many other physics topics."
