# Auto Greet Instagram - Backend

Python Flask backend for scheduling and sending Instagram greeting messages.

## 🚀 Setup Instructions

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Instagram Credentials

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your Instagram credentials:

```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

## 📡 API Endpoints

### Check Status
```
GET /status
```

### Login to Instagram
```
POST /login
```

### Schedule a Message
```
POST /schedule
Content-Type: application/json

{
  "recipient": "friend_username",
  "message": "Good Morning ☀️",
  "time": "08:00",
  "date": "2025-10-22",
  "repeat_daily": false
}
```

### List All Schedules
```
GET /list
```

### Delete a Schedule
```
DELETE /delete/<schedule_id>
```

### Send Message Now (Testing)
```
POST /send-now
Content-Type: application/json

{
  "recipient": "friend_username",
  "message": "Test message"
}
```

## 🔐 Security Notes

- Never commit your `.env` file
- Use your own Instagram account only
- Avoid sending too many messages (max 1-2 per day per recipient)
- The app adds 30-second delays between messages to prevent spam detection

## 🌐 Hosting Options

### Option 1: Run Locally with ngrok
```bash
ngrok http 5000
```

### Option 2: Deploy to Render.com (Free)
1. Create account on render.com
2. Connect your GitHub repo
3. Add environment variables in dashboard
4. Deploy!

### Option 3: Deploy to Replit
1. Import project to Replit
2. Add secrets (environment variables)
3. Run the app

## 📝 Notes

- The scheduler runs in a background thread
- Messages are checked every 30 seconds
- Schedule data is stored in `schedule.json`
- Failed messages are marked with error details
