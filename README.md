# Shadow Slave Web Reader

📖 A beautiful web reader for Shadow Slave novel with 2,720 chapters.

## Features

- 📚 All 2,720 chapters pre-loaded
- 🌙 Beautiful dark theme
- ⌨️ Keyboard navigation (← →)
- 🔐 OAuth login (Google/Discord) to save progress
- 📱 Mobile-friendly

## Deploy to PythonAnywhere (Free)

1. **Create account** at https://www.pythonanywhere.com (free tier works!)

2. **Open a Bash console** and clone the repo:
   ```bash
   git clone https://github.com/hawktuahcoin-hurhur/sumthsumthsdw.git
   ```

3. **Create a virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 shadowslave
   cd sumthsumthsdw
   pip install -r requirements.txt
   ```

4. **Create your .env file**:
   ```bash
   cp .env.example .env
   nano .env  # Edit with your settings
   ```
   Set `BASE_URL=https://yourusername.pythonanywhere.com`

5. **Go to Web tab** → Add a new web app:
   - Choose "Manual configuration"
   - Select Python 3.10
   
6. **Configure the web app**:
   - **Source code**: `/home/yourusername/sumthsumthsdw`
   - **Virtualenv**: `/home/yourusername/.virtualenvs/shadowslave`
   
7. **Edit the WSGI file** (click the link in Web tab):
   Replace everything with:
   ```python
   import sys
   import os
   
   project_home = '/home/yourusername/sumthsumthsdw'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)
   
   from dotenv import load_dotenv
   load_dotenv(os.path.join(project_home, '.env'))
   
   from run_web_app import app as application
   ```

8. **Click "Reload"** and visit `https://yourusername.pythonanywhere.com`

## Run Locally

```bash
git clone https://github.com/hawktuahcoin-hurhur/sumthsumthsdw.git
cd sumthsumthsdw
pip install -r requirements.txt
python run_web_app.py
```
Open http://localhost:5000

## Configuration

Copy `.env.example` to `.env` and set:
- `BASE_URL` - Your site URL (for OAuth redirects)
- `SECRET_KEY` - Random string for sessions
- `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` - For Google login
- `DISCORD_CLIENT_ID` / `DISCORD_CLIENT_SECRET` - For Discord login

## License

MIT
