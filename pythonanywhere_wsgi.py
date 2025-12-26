"""
PythonAnywhere WSGI configuration file.
Copy this content to your WSGI file on PythonAnywhere.
Replace 'yourusername' with your actual PythonAnywhere username.
"""
import sys
import os

# Add your project directory to the path
project_home = '/home/yourusername/sumthsumthsdw'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables from .env
from dotenv import load_dotenv
env_path = os.path.join(project_home, '.env')
load_dotenv(env_path)

# Import the Flask app
from run_web_app import app as application
