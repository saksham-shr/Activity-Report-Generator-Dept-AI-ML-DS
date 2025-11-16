#!/bin/bash
# EC2 Deployment Script for Report Generator

echo "Starting EC2 deployment..."

# Update system
sudo yum update -y

# Install Python 3 and pip
sudo yum install -y python3 python3-pip

# Install poppler (required for PDF to image conversion)
sudo yum install -y poppler-utils

# Install nginx (optional, for reverse proxy)
sudo yum install -y nginx

# Create application directory
sudo mkdir -p /opt/report-generator
sudo chown $USER:$USER /opt/report-generator

# Copy application files (assuming they're in current directory)
# You would typically use git clone or scp here
# cp -r . /opt/report-generator/

# Install Python dependencies
cd /opt/report-generator
pip3 install -r requirements.txt

# Create uploads directory structure
mkdir -p uploads/{photos,speaker,signatures,attendance,brochure,notice,feedback,impact}

# Set permissions
chmod -R 755 uploads
chmod -R 755 static

# Create systemd service file
sudo tee /etc/systemd/system/report-generator.service > /dev/null <<EOF
[Unit]
Description=Report Generator Gunicorn Application Server
After=network.target

[Service]
User=$USER
Group=$USER
WorkingDirectory=/opt/report-generator
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
ExecStart=/usr/local/bin/gunicorn --config gunicorn_config.py app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and start service
sudo systemctl daemon-reload
sudo systemctl enable report-generator
sudo systemctl start report-generator

# Configure nginx (optional)
sudo tee /etc/nginx/conf.d/report-generator.conf > /dev/null <<EOF
server {
    listen 80;
    server_name _;

    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Start nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Configure firewall (if using firewalld)
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload

echo "Deployment complete!"
echo "Check service status with: sudo systemctl status report-generator"
echo "Check logs with: sudo journalctl -u report-generator -f"

