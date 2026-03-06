# Vercel Deployment Guide

## Prerequisites
1. GitHub account (done ✓ - code is pushed)
2. Vercel account (free at https://vercel.com)

## Step-by-Step Deployment

### Option 1: Deploy via Vercel Dashboard (Easiest)

1. Go to https://vercel.com
2. Click "New Project"
3. Click "Import Git Repository"
4. Paste GitHub repo URL: `https://github.com/mohamedsaif21/Mental-Health-Support-Assistant.git`
5. Authorize GitHub access
6. Select the repository and click "Import"
7. Vercel will auto-detect Flask and Python
8. Click "Deploy"
9. Wait for deployment to complete (usually 1-2 minutes)

### Option 2: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. In project directory, run:
   ```bash
   vercel
   ```

3. Follow the prompts:
   - Link to existing project or create new
   - Authorize GitHub
   - Configure project settings (defaults are fine)

4. Deployment completes automatically

## After Deployment

Your app will be live at: `https://your-project-name.vercel.app`

### Environment Variables
If needed, add in Vercel Dashboard → Settings → Environment Variables:
- No variables required for basic setup

### Monitoring
- View logs in Vercel Dashboard
- Monitor function invocations
- Check error reports

## Troubleshooting

### Issue: Module not found errors
- Check requirements.txt has all dependencies
- Vercel automatically installs from requirements.txt

### Issue: Static files not loading
- Vercel serves static files from `static/` folder
- All CSS and JS in static/ are correctly configured

### Issue: Templates not rendering
- Vercel mounts templates from `templates/` folder
- api/index.py configured with correct paths

## Project Configuration Files

### vercel.json
- Routes all requests to Flask app (api/index.py)
- Configured for Python 3.11
- 50MB max function size

### requirements.txt
- Flask 2.3.3
- Werkzeug 2.3.7
- python-docx 0.8.11

### api/index.py
- Entry point for Vercel serverless functions
- Same Flask app logic, configured for Vercel environment
- Handles all routes: /, /chat, /api/chat

## Important Notes

1. **First deployment may take time**: Building Python packages can take 2-3 minutes
2. **Cold starts**: First request after deployment may be slower (normal for serverless)
3. **Session handling**: Each request is stateless (no session data between requests)
4. **File system**: Only `/tmp` is writable; data is not persisted between requests

## Custom Domain (Optional)

1. In Vercel Dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed

## Support & Documentation

- Vercel Python Builder: https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python
- Flask on Vercel: https://vercel.com/docs/concepts/functions/serverless-functions/frameworks/flask
- GitHub Deployment: https://vercel.com/docs/git/vercel-for-github
