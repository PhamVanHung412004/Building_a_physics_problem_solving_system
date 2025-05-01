from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

#Root, Main Page
@bp.route('/')
def index():
    return render_template('index.html')


#Login page
@bp.route('/login')
def login():
    return render_template('login.html')

#Chat page
@bp.route('/chat')
def chat():
    return render_template('chat.html')

#User page
@bp.route('/user')
def user():
    return render_template('user.html')
