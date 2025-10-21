# ⚡ Quick Start Guide

Get up and running in 10 minutes!

## 🎯 Prerequisites

- ✅ Python 3.8+ installed
- ✅ Flutter SDK installed
- ✅ Android device or emulator
- ✅ Instagram account

## 🚀 Step 1: Backend Setup (3 minutes)

### Windows:

```powershell
# Navigate to backend
cd backend

# Create .env file
copy .env.example .env

# Edit .env and add your Instagram credentials
notepad .env

# Run the start script
start_backend.bat
```

### Mac/Linux:

```bash
# Navigate to backend
cd backend

# Create .env file
cp .env.example .env

# Edit .env and add your Instagram credentials
nano .env

# Install dependencies and run
pip install -r requirements.txt
python app.py
```

**Expected Output:**
```
🚀 Auto Greet Instagram Backend Started
📱 Scheduler thread running in background
* Running on http://0.0.0.0:5000
```

✅ Keep this terminal open!

## 📱 Step 2: Flutter App Setup (5 minutes)

### Open New Terminal:

```powershell
# Navigate to Flutter app
cd flutter_app

# Get dependencies
flutter pub get

# Run the app
flutter run
```

**First build takes 2-5 minutes. Be patient!**

## 🔧 Step 3: Configure App (2 minutes)

### Find Your IP Address:

**Windows:**
```powershell
ipconfig
```
Look for "IPv4 Address" (e.g., `192.168.1.100`)

**Mac/Linux:**
```bash
ifconfig
```

### In the App:

1. Tap **Settings** icon (⚙️)
2. Enter: `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`
3. Tap **Save**
4. Tap **Refresh** icon
5. Should show: ✅ Connected & Logged In

## 🎉 Step 4: Send First Message!

1. **Recipient**: Your Instagram username (for testing)
2. **Message**: "Test from Auto Greet! 🎉"
3. **Time**: 2 minutes from now
4. Tap **Schedule Message**
5. Switch to **History** tab
6. Wait and check your Instagram DMs!

## 📋 Common Issues

### "Backend Not Reachable"
- ✅ Use IP address, not `localhost`
- ✅ Ensure backend is running
- ✅ Both devices on same WiFi

### "Login Failed"
- ✅ Check credentials in `.env`
- ✅ Verify Instagram account works

### "No devices found"
- ✅ Connect Android device
- ✅ Or start Android emulator

## 🎯 Next Steps

1. **Schedule Daily Greetings:**
   - Morning: 08:00 - "Good Morning ☀️"
   - Night: 22:00 - "Good Night 🌙"
   - Enable "Repeat Daily"

2. **Add Multiple Friends:**
   - Create separate schedules for each friend
   - Personalize messages

3. **Monitor History:**
   - Check sent/pending/failed messages
   - Delete unwanted schedules

## 📚 Full Documentation

- **Detailed Setup**: See `SETUP_GUIDE.md`
- **Backend API**: See `backend/README.md`
- **Flutter App**: See `flutter_app/README.md`
- **Main README**: See `README.md`

## 🆘 Need Help?

1. Check troubleshooting in `SETUP_GUIDE.md`
2. Review backend terminal for errors
3. Verify all prerequisites installed

## 🎊 Success!

You're now ready to automate your Instagram greetings!

**Remember:**
- Max 1-2 messages per person per day
- Use responsibly
- Respect Instagram's terms

---

**Happy Greeting! 🎉**
