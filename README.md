# 🌟 Auto Greet for Instagram

A personal automation app that sends scheduled greeting messages (like "Good Morning ☀️" or "Good Night 🌙") to selected Instagram friends automatically.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Platform](https://img.shields.io/badge/platform-Android-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Overview

This project consists of two main components:

1. **Flutter Android App** - Beautiful UI to schedule messages
2. **Python Flask Backend** - Handles Instagram automation and scheduling

## 📁 Project Structure

```
auto_greet_instagram/
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example          # Environment variables template
│   ├── .gitignore            # Git ignore rules
│   └── README.md             # Backend documentation
│
└── flutter_app/               # Flutter Android app
    ├── lib/
    │   ├── main.dart         # App entry point
    │   ├── screens/          # UI screens
    │   │   ├── home_screen.dart
    │   │   └── history_screen.dart
    │   └── services/         # API services
    │       └── api_service.dart
    ├── android/              # Android configuration
    ├── pubspec.yaml          # Flutter dependencies
    └── README.md             # Flutter app documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Flutter SDK 3.0+
- Android device or emulator
- Instagram account

### Backend Setup

1. **Navigate to backend folder:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Instagram credentials:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   ```
   INSTAGRAM_USERNAME=your_username
   INSTAGRAM_PASSWORD=your_password
   ```

4. **Run the backend:**
   ```bash
   python app.py
   ```
   
   Backend will start on `http://localhost:5000`

### Flutter App Setup

1. **Navigate to Flutter app folder:**
   ```bash
   cd flutter_app
   ```

2. **Install dependencies:**
   ```bash
   flutter pub get
   ```

3. **Run the app:**
   ```bash
   flutter run
   ```

4. **Configure backend URL in app:**
   - Tap settings icon (⚙️)
   - Enter backend URL (use your PC's IP address, not localhost)
   - Example: `http://192.168.1.100:5000`

## 🎨 Features

### ✅ Implemented Features

- 📱 **Beautiful Material Design 3 UI**
- 🌙 **Dark mode support**
- ⏰ **Schedule messages with date & time**
- 🔄 **Daily repeat option**
- 📝 **Quick message templates**
- 📊 **Message history with status**
- 🔔 **Backend connection status**
- 🗑️ **Delete pending schedules**
- 🔐 **Secure credential storage**
- 🚀 **Automatic message sending**

### 🔮 Future Enhancements

- [ ] Multiple recipients per schedule
- [ ] Custom message templates management
- [ ] Push notifications
- [ ] Message analytics
- [ ] Birthday reminders
- [ ] Festival greetings
- [ ] Cloud database (Firebase)
- [ ] Background service for app

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Mobile App | Flutter (Dart) |
| Backend | Python Flask |
| Instagram API | instagrapi |
| Database | JSON file (simple storage) |
| Scheduler | Threading + time module |

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/status` | GET | Check backend status |
| `/login` | POST | Login to Instagram |
| `/schedule` | POST | Schedule a message |
| `/list` | GET | Get all schedules |
| `/delete/<id>` | DELETE | Delete a schedule |
| `/send-now` | POST | Send message immediately |

## 🔐 Security Notes

⚠️ **Important Security Guidelines:**

- ✅ Use your own Instagram account only
- ✅ Keep credentials in `.env` file (never commit)
- ✅ Limit to 1-2 messages per day per recipient
- ✅ Add 30-second delays between messages
- ✅ Don't spam or violate Instagram's terms
- ❌ Never share your credentials
- ❌ Don't use for commercial purposes

## 🌐 Deployment Options

### Option 1: Local with ngrok (Easiest)

```bash
# Install ngrok
# Run backend
python app.py

# In another terminal
ngrok http 5000
```

Use the ngrok URL in your Flutter app.

### Option 2: Render.com (Free Hosting)

1. Create account on [render.com](https://render.com)
2. Connect GitHub repository
3. Add environment variables
4. Deploy!

### Option 3: Replit

1. Import project to [Replit](https://replit.com)
2. Add secrets (environment variables)
3. Run the app

## 💰 Cost Breakdown

| Component | Cost |
|-----------|------|
| Flutter SDK | ₹0 (Free) |
| Python + Flask | ₹0 (Free) |
| instagrapi | ₹0 (Free) |
| Hosting (Render/Replit) | ₹0 (Free tier) |
| Instagram Account | Existing |
| **Total** | **₹0** |

## 🐛 Troubleshooting

### Backend Issues

**Problem:** Backend not starting
- **Solution:** Check Python version (3.8+), install dependencies

**Problem:** Instagram login failed
- **Solution:** Verify credentials in `.env`, check Instagram account status

**Problem:** Messages not sending
- **Solution:** Check Instagram account isn't flagged, reduce message frequency

### Flutter App Issues

**Problem:** Can't connect to backend
- **Solution:** Use PC's IP address instead of localhost, check firewall

**Problem:** App not building
- **Solution:** Run `flutter clean` then `flutter pub get`

**Problem:** Backend status shows disconnected
- **Solution:** Verify backend is running, check URL is correct

## 📱 Screenshots

### Home Screen
- Schedule new messages
- Quick templates
- Date & time picker
- Backend status indicator

### History Screen
- View all schedules
- Status badges (Pending/Sent/Failed)
- Delete pending messages
- Pull to refresh

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for personal use only. Use responsibly and in accordance with Instagram's Terms of Service. The developers are not responsible for any misuse or account issues.

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review backend and app logs
3. Ensure all dependencies are installed
4. Verify Instagram credentials are correct

## 🌟 Acknowledgments

- **Flutter** - Beautiful UI framework
- **Flask** - Lightweight Python web framework
- **instagrapi** - Instagram API library
- **Material Design 3** - Modern UI components

---

**Made with ❤️ for automating daily greetings**

*Remember: Use this tool responsibly and respect Instagram's policies!*
