# 📋 Complete Setup Guide - Auto Greet Instagram

Step-by-step guide to get your Auto Greet Instagram app running.

## 🎯 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Windows PC (you have this ✅)
- [ ] Python 3.8 or higher
- [ ] Flutter SDK installed
- [ ] Android Studio (for emulator) or Android device
- [ ] Instagram account
- [ ] Internet connection

## 📦 Part 1: Backend Setup (15 minutes)

### Step 1: Install Python

1. Download Python from: https://www.python.org/downloads/
2. During installation, **check "Add Python to PATH"**
3. Verify installation:
   ```powershell
   python --version
   ```

### Step 2: Setup Backend

1. Open PowerShell/Terminal in the project folder
2. Navigate to backend:
   ```powershell
   cd backend
   ```

3. Create virtual environment (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### Step 3: Configure Instagram Credentials

1. Copy the example environment file:
   ```powershell
   copy .env.example .env
   ```

2. Open `.env` in notepad:
   ```powershell
   notepad .env
   ```

3. Add your Instagram credentials:
   ```
   INSTAGRAM_USERNAME=your_actual_username
   INSTAGRAM_PASSWORD=your_actual_password
   ```

4. Save and close

### Step 4: Test Backend

1. Run the backend:
   ```powershell
   python app.py
   ```

2. You should see:
   ```
   🚀 Auto Greet Instagram Backend Started
   📱 Scheduler thread running in background
   * Running on http://0.0.0.0:5000
   ```

3. Test in browser: Open `http://localhost:5000/status`
   - Should show: `{"status": "running", "success": true, ...}`

4. Keep this terminal open (backend must run continuously)

## 📱 Part 2: Flutter App Setup (20 minutes)

### Step 1: Install Flutter

1. Download Flutter SDK: https://docs.flutter.dev/get-started/install/windows
2. Extract to `C:\src\flutter`
3. Add to PATH:
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add: `C:\src\flutter\bin`

4. Verify installation:
   ```powershell
   flutter doctor
   ```

### Step 2: Setup Android

**Option A: Using Android Device**
1. Enable Developer Options on your phone
2. Enable USB Debugging
3. Connect phone to PC via USB
4. Allow USB debugging when prompted

**Option B: Using Emulator**
1. Install Android Studio
2. Open AVD Manager
3. Create a new virtual device
4. Start the emulator

### Step 3: Setup Flutter App

1. Open new PowerShell window
2. Navigate to flutter app:
   ```powershell
   cd flutter_app
   ```

3. Get dependencies:
   ```powershell
   flutter pub get
   ```

4. Check connected devices:
   ```powershell
   flutter devices
   ```

### Step 4: Run the App

1. Make sure backend is still running (from Part 1)
2. Run Flutter app:
   ```powershell
   flutter run
   ```

3. Wait for app to build and install (first time takes 2-5 minutes)

## 🔧 Part 3: Configuration (5 minutes)

### Step 1: Find Your PC's IP Address

1. In PowerShell, run:
   ```powershell
   ipconfig
   ```

2. Look for "IPv4 Address" under your active network adapter
   - Example: `192.168.1.100`

### Step 2: Configure App

1. Open the app on your device/emulator
2. Tap the **Settings icon** (⚙️) in top-right
3. Enter backend URL:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```
   Example: `http://192.168.1.100:5000`

4. Tap **Save**
5. Tap **Refresh** icon
6. Should show: ✅ Connected & Logged In

## 🎉 Part 4: Test Your First Message (5 minutes)

### Step 1: Schedule a Test Message

1. In the app, fill in:
   - **Recipient Username**: Your own Instagram username (for testing)
   - **Message**: "Test message from Auto Greet! 🎉"
   - **Date**: Today
   - **Time**: 2 minutes from now

2. Tap **Schedule Message**
3. Should see: "Message scheduled successfully"

### Step 2: Verify Schedule

1. Switch to **History** tab (bottom navigation)
2. You should see your scheduled message with status: **PENDING**

### Step 3: Wait for Message

1. Wait for the scheduled time
2. Check your Instagram DMs
3. You should receive the message!
4. In History tab, status should change to: **SENT**

## 🚀 Part 5: Daily Usage

### To Schedule Morning Greetings:

1. Open app
2. Enter friend's username
3. Select template: "Good Morning ☀️ Have a great day!"
4. Set time: 08:00
5. Enable "Repeat Daily"
6. Tap Schedule

### To Schedule Night Greetings:

1. Same process
2. Select template: "Good Night 🌙 Sleep well!"
3. Set time: 22:00
4. Enable "Repeat Daily"
5. Tap Schedule

## 🔥 Part 6: 24/7 Operation (Optional)

For messages to send automatically, backend must run 24/7.

### Option 1: Keep PC Running
- Keep backend running on your PC
- PC must be on and connected to internet

### Option 2: Use ngrok (Easy Tunneling)

1. Download ngrok: https://ngrok.com/download
2. Run backend as usual
3. In new terminal:
   ```powershell
   ngrok http 5000
   ```
4. Copy the https URL (e.g., `https://abc123.ngrok.io`)
5. Update backend URL in app settings

### Option 3: Deploy to Cloud (Free)

**Using Render.com:**
1. Create account: https://render.com
2. Create new Web Service
3. Connect your GitHub repo (push this project first)
4. Set environment variables (Instagram credentials)
5. Deploy
6. Use the Render URL in app

## ⚠️ Troubleshooting

### Backend Issues

**"Module not found" error**
```powershell
pip install -r requirements.txt
```

**"Login failed" error**
- Check Instagram username/password in `.env`
- Try logging in manually on Instagram
- Instagram might require verification

**"Port already in use"**
```powershell
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Flutter Issues

**"Flutter not found"**
- Add Flutter to PATH (see Step 1)
- Restart PowerShell

**"No devices found"**
- Connect Android device or start emulator
- Enable USB debugging on device

**"Can't connect to backend"**
- Use PC's IP address, not `localhost`
- Check firewall isn't blocking port 5000
- Ensure backend is running

### App Issues

**"Backend Not Reachable"**
- Verify backend is running
- Check IP address is correct
- Both devices on same WiFi network

**"Message not sending"**
- Check backend terminal for errors
- Verify Instagram login successful
- Check recipient username is correct

## 📞 Getting Help

If stuck:

1. Check backend terminal for error messages
2. Check app logs in Android Studio
3. Verify all steps completed
4. Try restarting backend and app

## 🎓 Tips for Best Results

1. **Test First**: Always test with your own account first
2. **Limit Messages**: Max 1-2 per person per day
3. **Timing**: Schedule during reasonable hours
4. **Personalize**: Customize messages for each friend
5. **Monitor**: Check History tab regularly
6. **Backup**: Keep `.env` file safe but private

## ✅ Success Checklist

After setup, you should have:

- [ ] Backend running without errors
- [ ] App installed on device
- [ ] Backend URL configured in app
- [ ] Status shows "Connected & Logged In"
- [ ] Test message sent successfully
- [ ] Message appears in History tab

## 🎉 You're All Set!

Congratulations! Your Auto Greet Instagram app is ready to use.

Start scheduling those daily greetings and make your friends smile! 😊

---

**Remember**: Use responsibly and respect Instagram's terms of service!
