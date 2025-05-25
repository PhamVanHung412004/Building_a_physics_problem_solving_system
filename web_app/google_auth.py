# Google authentication blueprint for Flask

import json
import os

import requests
from app import db
from flask import Blueprint, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user
from models import User
from oauthlib.oauth2 import WebApplicationClient

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# Make sure to use this redirect URL. It has to match the one in the whitelist
DEV_REDIRECT_URL = f'https://{os.environ.get("REPLIT_DEV_DOMAIN", "")}/google_login/callback'

# ALWAYS display setup instructions to the user:
print(f"""To make Google authentication work:
1. Go to https://console.cloud.google.com/apis/credentials
2. Create a new OAuth 2.0 Client ID
3. Add {DEV_REDIRECT_URL} to Authorized redirect URIs

For detailed instructions, see:
https://docs.replit.com/additional-resources/google-auth-in-flask#set-up-your-oauth-app--client
""")

if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    client = WebApplicationClient(GOOGLE_CLIENT_ID)
else:
    print("Warning: Google OAuth credentials not found in environment variables")
    client = None

google_auth = Blueprint("google_auth", __name__)

@google_auth.route("/google_login")
def login():
    if not client or not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        flash("Google OAuth is not configured. Please check your environment variables.", "danger")
        return redirect(url_for("login"))
        
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        # Replacing http:// with https:// is important as the external
        # protocol must be https to match the URI whitelisted
        redirect_uri=request.base_url.replace("http://", "https://") + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@google_auth.route("/google_login/callback")
def callback():
    if not client or not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        flash("Google OAuth is not configured properly.", "danger")
        return redirect(url_for("login"))
        
    # Get authorization code Google sent back
    code = request.args.get("code")
    if not code:
        flash("Authorization failed: No code received from Google", "danger")
        return redirect(url_for("login"))
    
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        # Replacing http:// with https:// is important as the external
        # protocol must be https to match the URI whitelisted
        authorization_response=request.url.replace("http://", "https://"),
        redirect_url=request.base_url.replace("http://", "https://"),
        code=code,
    )
    
    try:
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )
        
        # Parse the tokens
        client.parse_request_body_response(json.dumps(token_response.json()))
    except Exception as e:
        flash(f"Failed to obtain token: {str(e)}", "danger")
        return redirect(url_for("login"))

    # Get user info from Google
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    
    try:
        userinfo_response = requests.get(uri, headers=headers, data=body)
        userinfo = userinfo_response.json()
    except Exception as e:
        flash(f"Failed to get user info: {str(e)}", "danger")
        return redirect(url_for("login"))

    # Make sure email is verified
    if not userinfo.get("email_verified"):
        flash("User email not verified by Google.", "danger")
        return redirect(url_for("login"))

    # Get user data
    users_email = userinfo["email"]
    users_name = userinfo.get("given_name", users_email.split('@')[0])

    # Check if user exists, if not create a new user
    user = User.query.filter_by(email=users_email).first()
    if not user:
        user = User(username=users_name, email=users_email)
        db.session.add(user)
        db.session.commit()

    # Log in the user
    login_user(user)
    flash("Successfully signed in with Google.", "success")

    # Redirect to home page
    return redirect(url_for("chat"))

@google_auth.route("/google_logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))
