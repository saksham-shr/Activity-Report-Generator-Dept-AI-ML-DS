# EC2 Deployment Guide

This guide will help you deploy the Report Generator application on an AWS EC2 instance.

## Prerequisites

- AWS EC2 instance (Ubuntu 20.04/22.04 or Amazon Linux 2)
- SSH access to the instance
- Python 3.8 or higher
- Basic knowledge of Linux commands

## Step 1: Initial Server Setup

### Connect to your EC2 instance:
```bash
ssh -i your-key.pem ec2-user@your-instance-ip
```

### Update the system:
```bash
# For Amazon Linux 2
sudo yum update -y

# For Ubuntu
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install Dependencies

### Install Python and pip:
```bash
# Amazon Linux 2
sudo yum install -y python3 python3-pip

# Ubuntu
sudo apt install -y python3 python3-pip
```

### Install poppler (required for PDF to image conversion):
```bash
# Amazon Linux 2
sudo yum install -y poppler-utils

# Ubuntu
sudo apt install -y poppler-utils
```

### Install Gunicorn:
```bash
pip3 install gunicorn
```

## Step 3: Deploy Application

### Option A: Using Git (Recommended)
```bash
cd /opt
sudo git clone <your-repo-url> report-generator
cd report-generator
sudo chown -R $USER:$USER .
```

### Option B: Using SCP
```bash
# From your local machine
scp -i your-key.pem -r . ec2-user@your-instance-ip:/opt/report-generator
```

## Step 4: Install Python Dependencies

```bash
cd /opt/report-generator
pip3 install -r requirements.txt
```

## Step 5: Configure Application

### Create uploads directory:
```bash
mkdir -p uploads/{photos,speaker,signatures,attendance,brochure,notice,feedback,impact}
chmod -R 755 uploads
```

### Update config.py with your settings:
- Set `SECRET_KEY` to a strong random string
- Verify `ALLOWED_EMAILS` and `ADMIN_EMAIL`

### Initialize database:
```bash
python3 -c "from database import init_db; init_db()"
```

## Step 6: Set Up Gunicorn Service

### Create systemd service file:
```bash
sudo nano /etc/systemd/system/report-generator.service
```

### Add the following content:
```ini
[Unit]
Description=Report Generator Gunicorn Application Server
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/report-generator
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
ExecStart=/usr/local/bin/gunicorn --config gunicorn_config.py app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

**Note:** Replace `ec2-user` with your actual username if different.

### Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable report-generator
sudo systemctl start report-generator
```

### Check service status:
```bash
sudo systemctl status report-generator
```

## Step 7: Configure Nginx (Optional but Recommended)

### Install Nginx:
```bash
# Amazon Linux 2
sudo yum install -y nginx

# Ubuntu
sudo apt install -y nginx
```

### Create Nginx configuration:
```bash
sudo nano /etc/nginx/conf.d/report-generator.conf
```

### Add the following:
```nginx
server {
    listen 80;
    server_name your-domain.com;  # Replace with your domain or use _ for all

    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Start Nginx:
```bash
sudo systemctl enable nginx
sudo systemctl start nginx
```

## Step 8: Configure Firewall

### For Amazon Linux 2 (firewalld):
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### For Ubuntu (ufw):
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
sudo ufw enable
```

### Or use EC2 Security Groups:
- Add inbound rules for HTTP (port 80) and HTTPS (port 443)
- Add SSH (port 22) for management

## Step 9: SSL Certificate (Optional but Recommended)

### Using Let's Encrypt with Certbot:
```bash
# Install certbot
sudo yum install -y certbot python3-certbot-nginx  # Amazon Linux 2
# or
sudo apt install -y certbot python3-certbot-nginx  # Ubuntu

# Get certificate
sudo certbot --nginx -d your-domain.com
```

## Step 10: Verify Deployment

1. Open your browser and navigate to `http://your-ec2-ip` or `http://your-domain.com`
2. You should see the landing page
3. Test registration and login
4. Test report generation

## Troubleshooting

### Check Gunicorn logs:
```bash
sudo journalctl -u report-generator -f
```

### Check Nginx logs:
```bash
sudo tail -f /var/log/nginx/error.log
```

### Restart services:
```bash
sudo systemctl restart report-generator
sudo systemctl restart nginx
```

### Check if port 5000 is listening:
```bash
sudo netstat -tlnp | grep 5000
```

## Environment Variables

You can set environment variables in the systemd service file:

```ini
Environment="FLASK_ENV=production"
Environment="SECRET_KEY=your-secret-key-here"
```

## Backup

### Regular database backup:
```bash
# Add to crontab
0 2 * * * cp /opt/report-generator/report_generator.db /opt/report-generator/backups/report_generator_$(date +\%Y\%m\%d).db
```

## Updates

To update the application:

```bash
cd /opt/report-generator
git pull  # If using git
# or copy new files via SCP

# Restart service
sudo systemctl restart report-generator
```

## Security Notes

1. **Change SECRET_KEY**: Use a strong random string
2. **Use HTTPS**: Always use SSL in production
3. **Firewall**: Only open necessary ports
4. **Regular Updates**: Keep system and dependencies updated
5. **Backups**: Regular database backups
6. **Monitoring**: Set up log monitoring and alerts

## Support

For issues or questions, contact the system administrator or refer to the contact page in the application.

