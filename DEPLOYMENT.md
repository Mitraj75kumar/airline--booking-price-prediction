# Deployment Guide

## Step-by-Step GitHub Deployment

### Prerequisites
- GitHub account (https://github.com)
- Git installed locally
- Your GitHub username and token

### 1. Create GitHub Repository

**Option A: Via GitHub Web Interface**
1. Go to https://github.com/new
2. Repository name: `airline-booking-price-prediction`
3. Description: "ML model for predicting airline booking prices"
4. Visibility: Public (or Private if preferred)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

**Option B: Via GitHub CLI**
```bash
gh repo create airline-booking-price-prediction --public --source=. --remote=origin --push
```

### 2. Initialize Local Git Repository

Navigate to your project folder:
```bash
cd "c:\Users\mitra\Practice Question"
```

Initialize Git:
```bash
git init
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### 3. Add Files to Git

Stage all files:
```bash
git add .
```

Or stage selectively:
```bash
git add project.ipynb README.md requirements.txt setup.py Dockerfile .gitignore .github/
```

Verify staged files:
```bash
git status
```

### 4. Make Initial Commit

```bash
git commit -m "Initial commit: Airline booking price prediction model

- Complete ML pipeline with EDA and feature engineering
- XGBoost model achieving R² of 0.6066
- Production-ready prediction function
- Comprehensive documentation and deployment configs"
```

### 5. Add Remote Repository

Replace `YOUR_USERNAME` with your actual GitHub username:
```bash
git remote add origin https://github.com/YOUR_USERNAME/airline-booking-price-prediction.git
```

Or with SSH (if SSH key configured):
```bash
git remote add origin git@github.com:YOUR_USERNAME/airline-booking-price-prediction.git
```

Verify remote:
```bash
git remote -v
```

### 6. Push to GitHub

For main branch (first time):
```bash
git branch -M main
git push -u origin main
```

Subsequent pushes:
```bash
git push origin main
```

### 7. Verify Upload

1. Go to https://github.com/YOUR_USERNAME/airline-booking-price-prediction
2. Verify all files are present
3. Check that README renders properly
4. Confirm workflow file is in `.github/workflows/`

---

## Deployment Options

### Option 1: Local Deployment

**Requirements:**
- Python 3.8+
- Git

**Steps:**
```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/airline-booking-price-prediction.git
cd airline-booking-price-prediction

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook project.ipynb
```

### Option 2: Docker Deployment

**Requirements:**
- Docker installed
- GitHub repo cloned

**Steps:**
```bash
# Build image
docker build -t airline-booking-model .

# Run container
docker run -p 8888:8888 airline-booking-model

# Access Jupyter at: http://localhost:8888
```

### Option 3: Cloud Deployment (AWS)

#### Deploy to EC2
```bash
# 1. Launch EC2 instance (Ubuntu 20.04)
# 2. SSH into instance
ssh -i your-key.pem ubuntu@your-instance-ip

# 3. Clone repo
git clone https://github.com/YOUR_USERNAME/airline-booking-price-prediction.git
cd airline-booking-price-prediction

# 4. Install dependencies
sudo apt-get update
sudo apt-get install python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Run Jupyter with nohup
nohup jupyter notebook --ip=0.0.0.0 --no-browser > notebook.log &

# 6. Access at: http://your-instance-ip:8888
```

#### Deploy to SageMaker
1. Upload notebook to S3
2. Create SageMaker Notebook Instance
3. Select Conda environment: `python3`
4. Upload from S3
5. Open and run

### Option 4: GitHub Pages Deployment (Static Results)

```bash
# Generate HTML from notebook
jupyter nbconvert --to html project.ipynb

# Create docs folder
mkdir -p docs
mv project.html docs/index.html

# Push to GitHub
git add docs/
git commit -m "Add HTML version of notebook"
git push origin main
```

Then enable GitHub Pages in repository settings.

### Option 5: Heroku Deployment (Flask API)

**1. Create Flask app** (`app.py`):
```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load('models/best_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({
        'predicted_price': float(prediction),
        'currency': 'USD'
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run()
```

**2. Create Procfile**:
```
web: gunicorn app:app
```

**3. Add to requirements.txt**:
```
flask
gunicorn
joblib
```

**4. Deploy to Heroku**:
```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create airline-booking-model

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

---

## Continuous Integration/Deployment (CI/CD)

### GitHub Actions Workflow

The included `.github/workflows/ci-cd.yml` automatically:

✓ Runs tests on Python 3.8, 3.9, 3.10  
✓ Lints code with flake8  
✓ Builds Docker image  
✓ Checks code quality with black/isort  

**Workflow status:** Visible in GitHub repo under "Actions" tab

### Manual Workflow Trigger

```bash
# View workflow status
gh workflow list

# Manually trigger workflow
gh workflow run ci-cd.yml
```

---

## Updating Your Repository

### Make Changes Locally

```bash
# Edit files, then stage and commit
git add .
git commit -m "Your commit message"
```

### Push Changes

```bash
git push origin main
```

### Create Feature Branches

```bash
# Create new branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "Add your feature"

# Push branch
git push origin feature/your-feature

# Create Pull Request on GitHub (or use GitHub CLI)
gh pr create --title "Your PR title" --body "Description"
```

---

## Troubleshooting

### Error: "fatal: not a git repository"
**Solution:** Run `git init` in project directory

### Error: "remote repository not found"
**Solution:** 
1. Verify repository exists on GitHub
2. Check URL: `git remote -v`
3. If wrong URL: `git remote set-url origin <correct-url>`

### Error: "Permission denied (publickey)"
**Solution:**
1. Generate SSH key: `ssh-keygen -t ed25519`
2. Add public key to GitHub (Settings → SSH Keys)
3. Use SSH URL for cloning/pushing

### Large file upload errors
**Solution:** Use Git LFS for files > 100MB
```bash
git lfs install
git lfs track "*.xlsx"
git add .gitattributes
git add large-file.xlsx
git commit -m "Add large file"
git push origin main
```

---

## Post-Deployment Checklist

- [ ] Repository created on GitHub
- [ ] All files pushed successfully
- [ ] README displays correctly
- [ ] CI/CD workflow triggered and passing
- [ ] Clone repo in fresh folder to verify
- [ ] Test prediction function works
- [ ] Add project to portfolio
- [ ] Share with team/community

---

## Security Best Practices

### Before Pushing:
1. ✓ No API keys or secrets in code
2. ✓ Sensitive data in `.gitignore`
3. ✓ No passwords in notebooks
4. ✓ Use environment variables for config

### After Pushing:
1. ✓ Enable branch protection (require reviews)
2. ✓ Set up Dependabot for dependency updates
3. ✓ Monitor for security alerts
4. ✓ Rotate any exposed credentials

---

## Support & Resources

- GitHub Docs: https://docs.github.com
- Git Guide: https://git-scm.com/doc
- GitHub CLI: https://cli.github.com
- Jupyter Docs: https://jupyter.org
- XGBoost Docs: https://xgboost.readthedocs.io
