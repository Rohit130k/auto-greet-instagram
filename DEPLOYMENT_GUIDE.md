# 🚀 Deployment Guide - Auto Greet Instagram Backend

## 🌐 Option 1: Render.com (Recommended)

### Why Render?
- ✅ **Free tier**: 750 hours/month (24/7 operation)
- ✅ **Easy setup**: No credit card required
- ✅ **Auto-deploy**: Connects to GitHub
- ✅ **HTTPS**: Free SSL certificate
- ✅ **Always on**: No sleep after inactivity

### Steps to Deploy:

#### 1. Create GitHub Repository

```bash
# Initialize git in your project
cd c:\Users\LENOVO\AndroidStudioProjects\insta

# Create .gitignore (already exists)
# Add files
git init
git add .
git commit -m "Initial commit - Auto Greet Instagram"

# Create repo on GitHub and push
git remote add origin https://github.com/YOUR_USERNAME/auto-greet-instagram.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Render

1. Go to: https://render.com
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub repository
5. Configure:
   - **Name**: `auto-greet-instagram`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: `Free`

6. Add Environment Variables:
   - Click **"Environment"** tab
   - Add:
     - `INSTAGRAM_USERNAME` = your_username
     - `INSTAGRAM_PASSWORD` = your_password

7. Click **"Create Web Service"**

8. Wait 2-3 minutes for deployment

9. Your backend URL will be:
   ```
   https://auto-greet-instagram.onrender.com
   ```

#### 3. Update Flutter App

In your Flutter app settings, change backend URL to:
```
https://auto-greet-instagram.onrender.com
```

---

## 🌐 Option 2: Railway.app

### Why Railway?
- ✅ **Free tier**: $5 credit/month (enough for small apps)
- ✅ **Easy setup**: One-click deploy
- ✅ **Fast**: Quick deployment
- ✅ **Auto-deploy**: GitHub integration

### Steps:

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Set root directory: `backend`
6. Add environment variables:
   - `INSTAGRAM_USERNAME`
   - `INSTAGRAM_PASSWORD`
7. Deploy!

Your URL: `https://auto-greet-instagram.up.railway.app`

---

## 🌐 Option 3: Fly.io

### Why Fly.io?
- ✅ **Free tier**: 3 shared VMs
- ✅ **Fast**: Global edge network
- ✅ **Docker-based**: More control

### Steps:

1. Install Fly CLI:
   ```powershell
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. Login:
   ```bash
   fly auth login
   ```

3. Create fly.toml:
   ```bash
   cd backend
   fly launch
   ```

4. Set secrets:
   ```bash
   fly secrets set INSTAGRAM_USERNAME=your_username
   fly secrets set INSTAGRAM_PASSWORD=your_password
   ```

5. Deploy:
   ```bash
   fly deploy
   ```

---

## 🌐 Option 4: PythonAnywhere

### Why PythonAnywhere?
- ✅ **Free tier**: Always-on web app
- ✅ **No credit card**: Truly free
- ✅ **Python-focused**: Easy for Flask apps

### Steps:

1. Go to: https://www.pythonanywhere.com
2. Sign up for free account
3. Go to **"Web"** tab → **"Add a new web app"**
4. Choose **"Flask"** → **"Python 3.9"**
5. Upload your `backend` folder
6. Configure WSGI file
7. Set environment variables in **"Web"** tab
8. Reload web app

Your URL: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🌐 Option 5: Replit (Easiest for Beginners)

### Why Replit?
- ✅ **Super easy**: No Git required
- ✅ **Free tier**: Always-on with Hacker plan
- ✅ **Browser-based**: Edit code online

### Steps:

1. Go to: https://replit.com
2. Sign up
3. Click **"Create Repl"**
4. Choose **"Import from GitHub"** or **"Upload files"**
5. Upload your `backend` folder
6. Add secrets (environment variables):
   - Click **"Secrets"** (lock icon)
   - Add `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD`
7. Click **"Run"**

Your URL: `https://auto-greet-instagram.YOUR_USERNAME.repl.co`

---

## 📱 Update Flutter App After Deployment

1. Open Flutter app
2. Tap **Settings** (⚙️)
3. Change backend URL to your deployed URL:
   ```
   https://your-app.onrender.com
   ```
4. Tap **Save**
5. Tap **Refresh**
6. Should show: ✅ Connected & Logged In

---

## 🔧 Troubleshooting

### Backend Not Responding
- Check logs on hosting platform
- Verify environment variables are set
- Ensure Instagram login is working

### App Can't Connect
- Use HTTPS URL (not HTTP)
- Check if backend is running
- Test URL in browser: `https://your-url.com/status`

### Instagram Login Fails
- Check credentials in environment variables
- Instagram might require verification
- Try logging in manually on Instagram first

---

## 🎯 Recommended: Render.com

For most users, **Render.com** is the best choice because:
- ✅ Free and reliable
- ✅ No credit card required
- ✅ Easy GitHub integration
- ✅ Always-on (no sleep)
- ✅ Free SSL/HTTPS
- ✅ Auto-deploy on git push

---

## 🔐 Security Notes

- ✅ Never commit `.env` file
- ✅ Use environment variables on hosting platform
- ✅ Enable HTTPS (automatic on most platforms)
- ✅ Keep Instagram credentials secure
- ✅ Monitor for unusual activity

---

## 📊 Cost Comparison

| Platform | Free Tier | Always On | SSL | Ease |
|----------|-----------|-----------|-----|------|
| **Render.com** | 750h/mo | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐⭐ |
| **Railway.app** | $5 credit | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐ |
| **Fly.io** | 3 VMs | ✅ Yes | ✅ Yes | ⭐⭐⭐ |
| **PythonAnywhere** | 1 app | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐ |
| **Replit** | Limited | ⚠️ Sleeps | ✅ Yes | ⭐⭐⭐⭐⭐ |

---

## 🎉 Next Steps

1. Choose a hosting platform (Render.com recommended)
2. Follow the deployment steps
3. Update Flutter app with new URL
4. Test the connection
5. Start scheduling messages!

**Your backend will now be accessible 24/7 from anywhere! 🚀**
