# Firebase Setup Guide for Shadow Slave Reader

This guide will help you enable Google/Discord authentication and the comment system for your Shadow Slave reader.

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Enter project name: `shadow-slave-reader` (or your preferred name)
4. Accept the terms and click "Create project"
5. Wait for the project to be created

## Step 2: Register Your Web App

1. In Firebase Console, click the web icon (`</>`)) to register a web app
2. App nickname: `Shadow Slave Reader`
3. Click "Register app"
4. You'll see your Firebase config - **COPY THIS CONFIG** for the next step

## Step 3: Update the Code with Your Firebase Config

The Firebase config is located in `generate_static_site.py` around line 1788.

Replace the `FirebaseConfig` object with your actual credentials:

```javascript
const FirebaseConfig = {
    apiKey: "YOUR_FIREBASE_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

Replace each `YOUR_*` placeholder with the actual value from Firebase Console.

## Step 4: Enable Authentication Methods

1. In Firebase Console, go to **Authentication** > **Sign-in method**
2. Click **Google**:
   - Enable it
   - Provide a project support email
   - Click "Save"
3. Click **Discord** (if available) or use only Google for now

## Step 5: Set Up Firestore Database

1. Go to **Firestore Database** in Firebase Console
2. Click "Create database"
3. Select: **Start in test mode** (for development)
4. Choose a location close to you
5. Click "Create"

## Step 6: Configure Firestore Security Rules

1. In Firestore Database, go to the **Rules** tab
2. Replace the default rules with:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /comments/{document=**} {
      allow read: if true;
      allow create: if request.auth != null;
      allow update, delete: if request.auth.uid == resource.data.userId;
    }
  }
}
```

3. Click "Publish"

## Step 7: Set Authorized Redirect URIs

1. Go to **Credentials** in Google Cloud Console
2. Find your OAuth 2.0 Client IDs for Web
3. Click edit, then add your authorized JavaScript origins:
   - `https://hawktuahcoin-hurhur.github.io`
   - `http://localhost:8000` (for local testing)
4. Add authorized redirect URIs:
   - `https://hawktuahcoin-hurhur.github.io`
   - `http://localhost:8000`

## Step 8: Regenerate and Deploy

1. Run the static site generator:
   ```bash
   python generate_static_site.py
   ```

2. Commit and push to GitHub:
   ```bash
   git add -A
   git commit -m "Add Firebase auth and comment system"
   git push
   ```

3. GitHub Pages will automatically deploy your updated site

## Features Now Available

Once configured:

1. **Sign In**: Users can sign in with their Google account
2. **Comments**: Authenticated users can click on any paragraph to add comments
3. **Word-by-Word TTS**: Text-to-speech now highlights each word as it's spoken

## Testing Locally

To test locally:

1. Start a local HTTP server:
   ```bash
   cd docs
   python -m http.server 8000
   ```

2. Visit `http://localhost:8000`
3. Firebase will work because you added it to authorized origins

## Troubleshooting

- **"Firebase not configured" message**: Check that your config values are correct
- **Auth popup not opening**: Ensure your domain is in Google OAuth authorized origins
- **Comments not saving**: Check Firestore security rules and that user is authenticated
- **TTS not working**: Verify browser supports Web Speech API (Chrome, Safari, Edge)

## Features Breakdown

### Word-by-Word TTS Highlighting
- Uses browser's Web Speech API
- Each word is highlighted as it's spoken
- Paragraphs are also highlighted during reading
- Control playback speed with the dropdown (0.85x - 1.3x)

### Comment System
- Click any paragraph to add a comment
- Comments are stored in Firestore
- All comments are visible to everyone
- Only the author can edit/delete their comments
- Comments appear below each paragraph with author name and date

### Authentication
- Google Sign-In integrated into navbar
- User email displayed when signed in
- Sign Out button available when authenticated
- Comments require authentication
