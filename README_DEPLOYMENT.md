# Complete Deployment Guide - Report Generator

## ✅ Status: Ready for Deployment

All features have been tested and error handling has been implemented. The system is ready for EC2 deployment.

## 📁 Directory Structure for GitHub & EC2

### Files to Deploy:

```
rep-gen-com/
├── app.py                          # Main Flask application
├── config.py                       # Configuration (UPDATE SECRET_KEY!)
├── database.py                     # Database operations
├── report_logic.py                 # PDF generation (with error handling)
├── geolocation.py                  # IP geolocation
├── logging_config.py               # Logging setup
├── requirements.txt                # Python dependencies
├── gunicorn_config.py              # Production server config
├── create_accounts.py              # Bulk account creation
├── reset_password_admin.py         # Password reset utility
├── test_all_features.py            # Comprehensive test suite
├── view_logs.sh                    # Log viewing script
├── .gitignore                      # Git ignore rules
│
├── static/
│   └── christ_logo.png            # University logo
│
└── templates/                       # All HTML templates
    ├── landing.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── index.html
    ├── contact.html
    ├── privacy_policy.html
    ├── terms_of_use.html
    ├── forgot_password.html
    ├── reset_password.html
    ├── admin_panel.html
    ├── admin_locations.html
    ├── admin_users.html
    ├── admin_stats.html
    ├── admin_unauthorized.html
    └── my_locations.html
```

### Directories Created Automatically:
- `uploads/` - User uploads (created on first run)
- `logs/` - Application logs (created on first run)
- `*.db` - Database file (created on first run)

## 🚀 Quick Deployment Steps

### 1. Push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Production-ready Report Generator"
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Deploy to EC2

```bash
# SSH to EC2
ssh -i your-key.pem ec2-user@your-ec2-ip

# Clone repository
git clone <your-repo-url>
cd rep-gen-com

# Run deployment script
chmod +x ec2_deploy.sh
./ec2_deploy.sh

# OR follow manual steps in DEPLOYMENT.md
```

### 3. Configure

```bash
# Update SECRET_KEY in config.py
nano config.py

# Initialize database
python3 -c "from database import init_db; init_db()"

# Create upload directories
mkdir -p uploads/{photos,speaker,signatures,attendance,brochure,notice,feedback,impact}
```

### 4. Start Service

```bash
# Start systemd service
sudo systemctl start report-generator
sudo systemctl enable report-generator

# Check status
sudo systemctl status report-generator
```

## 🧪 Testing

### Before Deployment:
```bash
# Run comprehensive tests
python test_all_features.py

# Generate test report
python generate_test_report_with_images.py

# Check system status
python test_system.py
```

### After Deployment:
1. Visit `http://your-ec2-ip` or `http://your-domain.com`
2. Test registration and login
3. Generate a test report
4. Check admin panel at `/admin`

## 📊 Viewing Logs

### Quick Commands:
```bash
# View application log
./view_logs.sh app

# View error log
./view_logs.sh error

# View all logs
./view_logs.sh all

# Follow logs (live)
./view_logs.sh follow

# View service logs
./view_logs.sh service

# Follow service logs (live)
./view_logs.sh service-follow
```

### Manual Commands:
```bash
# Application logs
tail -f logs/report_generator.log

# Error logs
tail -f logs/errors.log

# All logs
tail -f logs/*.log

# Systemd service logs
sudo journalctl -u report-generator -f
```

## 🔒 Security Checklist

- [ ] Update `SECRET_KEY` in `config.py` (use strong random string)
- [ ] Verify `ALLOWED_EMAILS` and `ADMIN_EMAIL` in `config.py`
- [ ] Set proper file permissions
- [ ] Configure firewall (only open necessary ports)
- [ ] Use HTTPS in production (SSL certificate)
- [ ] Regular backups of database

## ✅ Error-Free Report Generation

### Implemented Error Handling:
- ✅ Image processing errors handled gracefully
- ✅ Missing images don't crash the system
- ✅ Large images automatically resized
- ✅ PDF conversion errors handled
- ✅ Comprehensive logging for all errors
- ✅ Try-catch blocks in all critical functions

### Test Scenarios Covered:
- ✅ Report with no images
- ✅ Report with some images
- ✅ Report with all images
- ✅ Report with large images (auto-resized)
- ✅ Report with PDF files (converted to images)
- ✅ Report with missing files (handled gracefully)

## 📝 Important Notes

1. **Database**: Will be created automatically on first run
2. **Logs**: Will be created automatically in `logs/` directory
3. **Uploads**: Directories created automatically, but ensure write permissions
4. **Poppler**: Required for PDF conversion - install on EC2: `sudo yum install poppler-utils`
5. **Secret Key**: MUST be changed in production - use a strong random string

## 🆘 Troubleshooting

### Report Generation Fails:
1. Check error logs: `./view_logs.sh error`
2. Verify image files exist and are readable
3. Check disk space: `df -h`
4. Verify permissions: `ls -la uploads/`

### Service Won't Start:
1. Check service status: `sudo systemctl status report-generator`
2. Check service logs: `sudo journalctl -u report-generator -n 50`
3. Verify Python path: `which python3`
4. Check dependencies: `pip3 list | grep flask`

### Database Errors:
1. Check database file: `ls -la *.db`
2. Verify permissions: `chmod 644 report_generator.db`
3. Reinitialize: `python3 -c "from database import init_db; init_db()"`

## 📚 Documentation Files

- `DEPLOYMENT.md` - Detailed EC2 deployment guide
- `DEPLOYMENT_STRUCTURE.md` - Complete directory structure
- `FINAL_CHECKLIST.md` - Pre-deployment checklist
- `SETUP.md` - Local setup instructions
- `README.md` - General project documentation

## 🎯 Success Criteria

✅ All tests pass
✅ Report generation works with all image types
✅ No errors in logs during normal operation
✅ Service runs without crashes
✅ All features accessible
✅ Admin panel works
✅ Logs are being written correctly

## 📞 Support

For issues:
1. Check logs: `./view_logs.sh all`
2. Review error messages
3. Check system status: `sudo systemctl status report-generator`
4. Review documentation files

---

**Ready to deploy!** Follow the steps above and your application will be running on EC2.

