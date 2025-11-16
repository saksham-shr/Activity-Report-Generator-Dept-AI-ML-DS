# Final Deployment Checklist

## Pre-Deployment Testing

### 1. Run Comprehensive Tests
```bash
python test_all_features.py
```
**Expected:** All tests pass

### 2. Test Report Generation
```bash
python generate_test_report_with_images.py
```
**Expected:** PDF generated successfully with all images

### 3. Test System Status
```bash
python test_system.py
```
**Expected:** All systems operational

### 4. Manual Testing Checklist
- [ ] User registration works
- [ ] User login works
- [ ] Password reset works
- [ ] Dashboard loads correctly
- [ ] New report form loads
- [ ] All form sections work
- [ ] File uploads work (images and PDFs)
- [ ] Draft saving works
- [ ] Draft loading works
- [ ] Report generation works
- [ ] Live preview works
- [ ] Collaboration features work
- [ ] Admin panel accessible
- [ ] All admin features work

## Error-Free Report Generation Checklist

### Before Deployment:
- [ ] All image processing functions have error handling
- [ ] PDF generation has try-catch blocks
- [ ] Missing images don't crash the system
- [ ] Large images are properly resized
- [ ] PDF conversion errors are handled gracefully
- [ ] All logging is in place
- [ ] Test report generation with:
  - [ ] No images
  - [ ] Some images
  - [ ] All images
  - [ ] Large images
  - [ ] PDF files
  - [ ] Missing files

## GitHub Repository Setup

### Files to Commit:
```bash
git add .
git commit -m "Initial deployment-ready version"
git push origin main
```

### Files NOT to Commit (handled by .gitignore):
- Database files (*.db)
- Log files (logs/*)
- Upload files (uploads/*)
- Virtual environment (venv/)
- Test PDFs

## EC2 Deployment Steps

### 1. Initial Setup
```bash
# Connect to EC2
ssh -i your-key.pem ec2-user@your-ec2-ip

# Clone repository
git clone <your-repo-url>
cd rep-gen-com
```

### 2. Install Dependencies
```bash
# Install system dependencies
sudo yum install -y python3 python3-pip poppler-utils  # Amazon Linux
# OR
sudo apt install -y python3 python3-pip poppler-utils  # Ubuntu

# Install Python packages
pip3 install -r requirements.txt
pip3 install gunicorn
```

### 3. Configure Application
```bash
# Update config.py with production SECRET_KEY
nano config.py

# Initialize database
python3 -c "from database import init_db; init_db()"

# Create upload directories
mkdir -p uploads/{photos,speaker,signatures,attendance,brochure,notice,feedback,impact}
chmod -R 755 uploads
```

### 4. Setup Systemd Service
```bash
# Create service file
sudo nano /etc/systemd/system/report-generator.service
# (Copy content from DEPLOYMENT.md)

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable report-generator
sudo systemctl start report-generator

# Check status
sudo systemctl status report-generator
```

### 5. Setup Nginx (Optional)
```bash
# Install nginx
sudo yum install -y nginx  # Amazon Linux
# OR
sudo apt install -y nginx  # Ubuntu

# Configure nginx
sudo nano /etc/nginx/conf.d/report-generator.conf
# (Copy content from DEPLOYMENT.md)

# Start nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

## Post-Deployment Verification

### 1. Check Service Status
```bash
sudo systemctl status report-generator
```

### 2. Check Logs
```bash
# Application logs
./view_logs.sh app

# Error logs
./view_logs.sh error

# Service logs
./view_logs.sh service
```

### 3. Test Application
- Visit `http://your-ec2-ip` or `http://your-domain.com`
- Test all features
- Generate a test report
- Check admin panel

### 4. Monitor for Errors
```bash
# Watch logs in real-time
./view_logs.sh follow

# Or service logs
./view_logs.sh service-follow
```

## Log Viewing Commands

### Quick Reference:
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

### Manual Log Viewing:
```bash
# Application log
tail -f logs/report_generator.log

# Error log
tail -f logs/errors.log

# All logs
tail -f logs/*.log

# Service logs
sudo journalctl -u report-generator -f
```

## Troubleshooting

### If Report Generation Fails:
1. Check error logs: `./view_logs.sh error`
2. Check application logs: `./view_logs.sh app`
3. Verify image processing: Test with small images first
4. Check disk space: `df -h`
5. Check permissions: `ls -la uploads/`

### If Service Won't Start:
1. Check service status: `sudo systemctl status report-generator`
2. Check service logs: `sudo journalctl -u report-generator -n 50`
3. Verify Python path: `which python3`
4. Verify dependencies: `pip3 list | grep -E "flask|reportlab|pillow"`

### If Database Errors:
1. Check database file: `ls -la *.db`
2. Verify permissions: `chmod 644 report_generator.db`
3. Reinitialize if needed: `python3 -c "from database import init_db; init_db()"`

## Success Criteria

✅ All tests pass
✅ Report generation works with all image types
✅ No errors in logs
✅ Service runs without crashes
✅ All features accessible
✅ Admin panel works
✅ Logs are being written

## Support

For issues:
1. Check logs first: `./view_logs.sh all`
2. Review error messages
3. Check system status: `sudo systemctl status report-generator`
4. Review DEPLOYMENT.md for detailed instructions

