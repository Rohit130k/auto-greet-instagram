# 🚀 Quick Deploy to Render.com (5 Minutes)

## Step-by-Step Guide

### 1️⃣ Push to GitHub (First Time Only)

```powershell
# Navigate to project root
cd c:\Users\LENOVO\AndroidStudioProjects\insta

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Auto Greet Instagram - Ready for deployment"

# Create repository on GitHub:
# Go to https://github.com/new
# Repository name: auto-greet-instagram
# Make it Private (recommended)
# Don't initialize with README (we already have files)
# Click "Create repository"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/auto-greet-instagram.git
git branch -M main
git push -u origin main
```

### 2️⃣ Deploy on Render

1. **Go to Render**: https://render.com

2. **Sign Up/Login** with GitHub

3. **Create New Web Service**:
   - Click **"New +"** button (top right)
   - Select **"Web Service"**

4. **Connect Repository**:
   - Click **"Connect account"** if needed
   - Find and select **"auto-greet-instagram"**
   - Click **"Connect"**

5. **Configure Service**:
   ```
   Name: auto-greet-instagram
   Region: Choose closest to you
   Branch: main
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python app.py
   Instance Type: Free
   ```

6. **Add Environment Variables**:
   - Scroll down to **"Environment Variables"**
   - Click **"Add Environment Variable"**
   - Add these two:
     ```
     Key: INSTAGRAM_USERNAME
     Value: your_instagram_username
     
     Key: INSTAGRAM_PASSWORD
     Value: your_instagram_password
     ```

7. **Create Web Service**:
   - Click **"Create Web Service"** button
   - Wait 2-3 minutes for deployment

8. **Get Your URL**:
   - After deployment completes, you'll see:
   ```
   https://auto-greet-instagram.onrender.com
   ```
   - Copy this URL!

### 3️⃣ Test Your Deployment

Open browser and go to:
```
https://auto-greet-instagram.onrender.com/status
```

Should show:
```json
{
  "logged_in": true,
  "status": "running",
  "success": true
}
```

### 4️⃣ Update Flutter App

1. Open your Flutter app
2. Tap **Settings** icon (⚙️)
3. Change backend URL to:
   ```
   https://auto-greet-instagram.onrender.com
   ```
4. Tap **Save**
5. Tap **Refresh** icon
6. Should show: **✅ Connected & Logged In**

### 5️⃣ Schedule Your First Message!

Now you can schedule messages from anywhere! 🎉

---

## 🔄 Update Your Deployment

When you make changes to the code:

```powershell
# Commit changes
git add .
git commit -m "Updated feature"

# Push to GitHub
git push

# Render will automatically redeploy! ✨
```

---

## 📊 Monitor Your App

### View Logs
1. Go to Render dashboard
2. Click on your service
3. Click **"Logs"** tab
4. See real-time logs

### Check Status
- **Dashboard**: See if service is running
- **Metrics**: View CPU and memory usage
- **Events**: See deployment history

---

## ⚠️ Important Notes

### Free Tier Limitations
- ✅ 750 hours/month (enough for 24/7)
- ✅ Sleeps after 15 min of inactivity
- ✅ Wakes up on first request (takes ~30 seconds)

### Keep It Awake (Optional)
To prevent sleeping, use a service like **UptimeRobot**:
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add monitor:
   - Type: HTTP(s)
   - URL: `https://auto-greet-instagram.onrender.com/status`
   - Interval: 5 minutes
4. This pings your app every 5 minutes to keep it awake!

---

## 🐛 Troubleshooting

### Deployment Failed
- Check build logs in Render dashboard
- Verify `requirements.txt` is correct
- Ensure `backend` folder structure is correct

### Can't Login to Instagram
- Check environment variables are set correctly
- No quotes around values
- Instagram might require verification

### App Shows "Not Logged In"
- Wait 30 seconds after first request (cold start)
- Check logs for login errors
- Verify Instagram credentials

### 502 Bad Gateway
- Service is starting up (wait 30 seconds)
- Check if service crashed (view logs)
- Restart service from dashboard

---

## 🎯 Success Checklist

- [ ] Code pushed to GitHub
- [ ] Render service created
- [ ] Environment variables added
- [ ] Deployment successful
- [ ] `/status` endpoint returns `logged_in: true`
- [ ] Flutter app connected
- [ ] Test message scheduled and sent

---

## 🎉 You're Live!

Your Instagram auto-greet backend is now:
- ✅ Running 24/7 in the cloud
- ✅ Accessible from anywhere
- ✅ Automatically sending scheduled messages
- ✅ Free forever (on free tier)

**Congratulations! 🎊**

---

## 📞 Need Help?

- **Render Docs**: https://render.com/docs
- **Check Logs**: Render Dashboard → Your Service → Logs
- **Test Endpoint**: `https://your-url.onrender.com/status`

---

**Pro Tip**: Bookmark your Render dashboard and check logs occasionally to ensure everything is running smoothly!
