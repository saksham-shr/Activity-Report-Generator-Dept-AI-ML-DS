# Deployment Structure for EC2 and GitHub

## Directory Structure to Deploy

```
rep-gen-com/
├── app.py                          # Main Flask application
├── config.py                       # Configuration (emails, secret key)
├── database.py                     # Database operations
├── report_logic.py                 # PDF generation logic
├── geolocation.py                  # IP geolocation
├── logging_config.py               # Logging setup
├── requirements.txt                # Python dependencies
├── gunicorn_config.py              # Gunicorn configuration
├── ec2_deploy.sh                   # EC2 deployment script
├── create_accounts.py              # Bulk account creation
├── reset_password_admin.py         # Password reset utility
├── generate_sample_report.py       # Sample report generator
├── generate_test_report_with_images.py  # Test report with images
├── test_all_features.py            # Comprehensive test suite
├── test_system.py                  # System check script
│
├── static/                          # Static files
│   └── christ_logo.png            # University logo
│
├── templates/                       # HTML templates
│   ├── landing.html                # Landing page
│   ├── login.html                  # Login page
│   ├── register.html               # Registration page
│   ├── dashboard.html              # User dashboard
│   ├── index.html                  # Report generator form
│   ├── contact.html                # Contact page
│   ├── privacy_policy.html         # Privacy policy
│   ├── terms_of_use.html           # Terms of use
│   ├── forgot_password.html        # Password reset request
│   ├── reset_password.html         # Password reset form
│   ├── admin_panel.html            # Admin panel
│   ├── admin_locations.html        # Admin location view
│   ├── admin_users.html             # Admin user management
│   ├── admin_stats.html             # Admin statistics
│   ├── admin_unauthorized.html     # Unauthorized access logs
│   └── my_locations.html           # User location view
│
├── uploads/                         # Upload directories (created automatically)
│   ├── photos/                       # Activity photos
│   ├── speaker/                     # Speaker images
│   ├── signatures/                  # Digital signatures
│   ├── attendance/                  # Attendance documents
│   ├── brochure/                    # Brochure documents
│   ├── notice/                      # Notice documents
│   ├── feedback/                    # Feedback documents
│   └── impact/                      # Impact analysis documents
│
├── logs/                            # Log files (created automatically)
│   ├── report_generator.log        # Main application log
│   ├── errors.log                   # Error log
│   └── access.log                   # Access log
│
├── .gitignore                       # Git ignore file
├── README.md                        # Project documentation
├── SETUP.md                         # Setup instructions
├── DEPLOYMENT.md                    # EC2 deployment guide
└── DEPLOYMENT_STRUCTURE.md          # This file
```

## Files to Exclude from GitHub

Create a `.gitignore` file with:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
dist/
build/

# Database
*.db
*.sqlite
*.sqlite3

# Logs
logs/
*.log

# Uploads
uploads/
!uploads/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Test files
test_report_*.pdf
sample_report_*.pdf
*.tmp

# Temporary files
tmp/
temp/
```

## Files Required for EC2 Deployment

### Essential Files (Must Deploy):
1. `app.py` - Main application
2. `config.py` - Configuration
3. `database.py` - Database operations
4. `report_logic.py` - PDF generation
5. `geolocation.py` - Location services
6. `logging_config.py` - Logging
7. `requirements.txt` - Dependencies
8. `gunicorn_config.py` - Production server config
9. `templates/` - All HTML templates
10. `static/` - Static files

### Optional but Recommended:
- `create_accounts.py` - For bulk account creation
- `reset_password_admin.py` - For password management
- `test_all_features.py` - For testing
- `DEPLOYMENT.md` - Deployment guide

### Files NOT to Deploy:
- `*.db` - Database files (will be created on server)
- `logs/` - Log files (will be created on server)
- `uploads/` - Upload directories (will be created, but keep structure)
- `venv/` - Virtual environment
- `__pycache__/` - Python cache
- Test PDFs

## GitHub Repository Structure

```
your-repo/
├── .gitignore
├── README.md
├── SETUP.md
├── DEPLOYMENT.md
├── DEPLOYMENT_STRUCTURE.md
├── requirements.txt
├── app.py
├── config.py
├── database.py
├── report_logic.py
├── geolocation.py
├── logging_config.py
├── gunicorn_config.py
├── create_accounts.py
├── reset_password_admin.py
├── test_all_features.py
├── static/
│   └── christ_logo.png
└── templates/
    └── [all HTML files]
```

## EC2 Deployment Checklist

### Before Deployment:
- [ ] Update `config.py` with production `SECRET_KEY`
- [ ] Verify `ALLOWED_EMAILS` and `ADMIN_EMAIL` in `config.py`
- [ ] Test locally with `python app.py`
- [ ] Run `python test_all_features.py` to verify all features
- [ ] Generate test report to verify PDF generation

### Deployment Steps:
1. **Clone/Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **On EC2 Instance:**
   ```bash
   git clone <your-repo-url>
   cd rep-gen-com
   chmod +x ec2_deploy.sh
   ./ec2_deploy.sh
   ```

3. **Manual Setup (if script doesn't work):**
   - Follow `DEPLOYMENT.md` guide
   - Install dependencies: `pip3 install -r requirements.txt`
   - Initialize database: `python3 -c "from database import init_db; init_db()"`
   - Start service: `sudo systemctl start report-generator`

## Viewing Logs

### Application Logs:
```bash
# Main log
tail -f logs/report_generator.log

# Error log
tail -f logs/errors.log

# Access log
tail -f logs/access.log

# All logs
tail -f logs/*.log
```

### Systemd Service Logs:
```bash
# Service status
sudo systemctl status report-generator

# Service logs
sudo journalctl -u report-generator -f

# Recent logs
sudo journalctl -u report-generator -n 100

# Logs since today
sudo journalctl -u report-generator --since today
```

### Nginx Logs (if using):
```bash
# Access log
sudo tail -f /var/log/nginx/access.log

# Error log
sudo tail -f /var/log/nginx/error.log
```

### Gunicorn Logs:
Gunicorn logs are configured to go to stdout/stderr, which are captured by systemd.

## Testing After Deployment

1. **Test Basic Functionality:**
   ```bash
   python3 test_all_features.py
   ```

2. **Test Report Generation:**
   ```bash
   python3 generate_test_report_with_images.py
   ```

3. **Check System Status:**
   ```bash
   python3 test_system.py
   ```

4. **Manual Testing:**
   - Visit `http://your-ec2-ip` or `http://your-domain.com`
   - Test registration
   - Test login
   - Test report generation
   - Test all features

## Monitoring and Maintenance

### Daily Checks:
- Check error logs: `tail -n 50 logs/errors.log`
- Check service status: `sudo systemctl status report-generator`
- Monitor disk space: `df -h`

### Weekly Checks:
- Review access logs for suspicious activity
- Check database size
- Review unauthorized access logs (admin panel)

### Monthly Checks:
- Rotate logs if needed
- Update dependencies: `pip3 install -r requirements.txt --upgrade`
- Backup database

## Backup Strategy

### Database Backup:
```bash
# Create backup
cp report_generator.db backups/report_generator_$(date +%Y%m%d).db

# Restore from backup
cp backups/report_generator_YYYYMMDD.db report_generator.db
```

### Automated Backup Script:
Create `backup.sh:
```bash
#!/bin/bash
BACKUP_DIR="/opt/report-generator/backups"
mkdir -p $BACKUP_DIR
cp /opt/report-generator/report_generator.db $BACKUP_DIR/report_generator_$(date +%Y%m%d_%H%M%S).db
# Keep only last 30 days
find $BACKUP_DIR -name "*.db" -mtime +30 -delete
```

Add to crontab:
```bash
0 2 * * * /opt/report-generator/backup.sh
```

## Security Notes

1. **Never commit:**
   - `config.py` with real `SECRET_KEY`
   - Database files
   - Log files with sensitive data

2. **Use environment variables for sensitive data:**
   ```python
   import os
   SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key')
   ```

3. **Set proper file permissions:**
   ```bash
   chmod 600 config.py  # Only owner can read/write
   chmod 755 uploads/   # Owner can write, others can read
   ```

4. **Regular security updates:**
   ```bash
   sudo yum update -y  # Amazon Linux
   sudo apt update && sudo apt upgrade -y  # Ubuntu
   ```

