# 🔧 Troubleshooting Guide

## ❌ Error: "Failed to update credentials: FormatException"

### Problem
When updating username/password in Settings, you get an error:
```
Exception: Failed to update credentials: FormatException: Unexpected character (at character 1)
<!doctype html>
```

### Cause
The backend server is returning HTML instead of JSON. This means:
- The `/update-credentials` endpoint doesn't exist (old backend version)
- Backend needs to be restarted to load new endpoints

### ✅ Solution

**Step 1: Stop the Backend**
```powershell
# In the terminal running the backend, press:
Ctrl + C
```

**Step 2: Restart the Backend**
```powershell
cd c:\Users\LENOVO\AndroidStudioProjects\insta\backend
python app.py
```

**Step 3: Try Again**
- Go to Settings in the app
- Enter username and password
- Click Save Settings

---

## 📱 Username Auto-Fill Issue

### Problem
Username doesn't show in Settings page

### ✅ Solution
The username is now **automatically loaded** from saved preferences!

**To see it:**
1. Open app → Go to **Settings**
2. Username field will auto-fill if previously saved
3. If empty, enter username and save
4. Next time it will auto-fill

---

## 🏠 Connected Account Card Not Showing

### Problem
Instagram account card doesn't appear on Home screen

### ✅ Solution

**The card only shows if:**
- Username is saved in Settings
- Username is not empty

**To make it appear:**
1. Go to **Settings** tab
2. Enter Instagram username
3. Click **Save Settings**
4. Go back to **Home** tab
5. Card will appear! 🎉

---

## 🔄 Backend Endpoints Missing

### Problem
Getting 404 or HTML responses for API calls

### ✅ Solution

**Check Backend Version:**
```powershell
cd backend
python app.py
```

**Look for these endpoints in startup:**
- `/status`
- `/schedule`
- `/schedules`
- `/delete/<id>`
- `/update-credentials` ← **New endpoint**
- `/update/<id>` ← **New endpoint**

**If missing, the backend code needs updating!**

---

## 🚀 Quick Fixes

### Backend Not Reachable
```powershell
# 1. Check backend is running
cd backend
python app.py

# 2. Check IP address
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.100)

# 3. Update in app Settings
# Use: http://YOUR_IP:5000
```

### App Not Connecting
1. **Check backend URL** in Settings
2. **Use PC's IP** (not localhost)
3. **Ensure same network** (PC and phone)
4. **Check firewall** (allow port 5000)

### Credentials Not Saving
1. **Restart backend** first
2. **Enter both** username and password
3. **Click Save Settings**
4. **Wait for success message**

---

## 📋 Checklist

Before reporting issues, verify:

- [ ] Backend is running (`python app.py`)
- [ ] Backend shows all endpoints on startup
- [ ] Backend URL is correct in app Settings
- [ ] Phone and PC on same WiFi network
- [ ] Firewall allows port 5000
- [ ] Username is entered in Settings
- [ ] Password is entered (if updating credentials)

---

## 🆘 Still Having Issues?

### Check Backend Logs
Look at the terminal running `python app.py` for error messages.

### Check App Logs
In Android Studio or VS Code, check the Debug Console for errors.

### Common Error Messages

| Error | Solution |
|-------|----------|
| `Connection refused` | Backend not running |
| `FormatException` | Restart backend |
| `Timeout` | Check network/firewall |
| `401 Unauthorized` | Wrong credentials |
| `404 Not Found` | Endpoint missing, restart backend |

---

## ✅ Everything Working?

You should see:
- ✅ Green "Connected & Logged In" on Home
- ✅ Connected Account card on Home
- ✅ Username auto-filled in Settings
- ✅ Successful schedule creation
- ✅ Messages in History

**Enjoy your AutoGreet app! 🎉**
