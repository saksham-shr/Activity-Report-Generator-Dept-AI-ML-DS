# Setup Guide - Report Generator with Authentication

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note for PDF Support**: If you want PDF to image conversion to work, you need to install `poppler`:

- **Windows**: Download from https://github.com/oschwartz10612/poppler-windows/releases/ and add to PATH
- **Linux**: `sudo apt-get install poppler-utils` (Ubuntu/Debian) or `sudo yum install poppler-utils` (CentOS/RHEL)
- **macOS**: `brew install poppler`

### 2. Configure Allowed Emails

Edit `config.py` and add authorized email addresses:

```python
ALLOWED_EMAILS = [
    'faculty1@christuniversity.in',
    'faculty2@christuniversity.in',
    # Add more emails here
]

ADMIN_EMAIL = 'your-admin-email@christuniversity.in'  # Change this
SECRET_KEY = 'change-this-to-a-random-secret-key'  # Change this in production
```

### 3. Initialize Database

The database will be created automatically on first run. To manually initialize:

```python
from database import init_db
init_db()
```

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## New Features

### Authentication System
- Email whitelist-based access control
- Password hashing for security
- Password reset functionality
- Device tracking for security monitoring

### Draft Management
- Save drafts at any section
- View all saved drafts from dashboard
- Continue editing saved drafts
- Delete drafts

### New Sections
- Attendance List (PDF/Image upload with multiple files)
- Brochure (PDF/Image upload with multiple files)
- Notice for Approval (PDF/Image upload with multiple files)
- Feedback Analysis (PDF/Image upload with multiple files)
- Impact Analysis (PDF/Image upload with multiple files)

### PDF Features
- PDF to image conversion (one page = one image)
- Improved image compression for large files
- Better handling of large image uploads

### Security Features
- Device fingerprinting
- Login session tracking
- New device login alerts
- IP address logging

## First Time Setup

1. **Add Authorized Emails**: Edit `config.py` and add faculty email addresses (already done)
2. **Set Admin Email**: Update `ADMIN_EMAIL` in `config.py` to receive security alerts (already done)
3. **Change Secret Key**: Update `SECRET_KEY` in `config.py` (use a random string)
4. **Create Faculty Accounts** (Choose one option):

   **Option A: Pre-create all accounts with default password (Recommended)**
   ```bash
   python create_accounts.py
   ```
   This will create accounts for all faculty members in `config.py` with a default password. You'll be prompted to enter a default password. Faculty members can change it after first login.

   **Option B: Let faculty register themselves**
   - Faculty members visit the registration page
   - They enter their email (must be in whitelist) and set their own password
   - They can then login

5. **Run Application**: Start the server with `python app.py`
6. **Login**: Users can login and start creating reports

## Managing Passwords

### Reset a User's Password (Admin)
If a faculty member forgets their password, you can reset it:
```bash
python reset_password_admin.py
# Or with email as argument:
python reset_password_admin.py user@christuniversity.in
```

### Faculty Self-Service Password Reset
Faculty members can also use the "Forgot Password" link on the login page to reset their own password (requires email access).

## Database Schema

The system uses SQLite database (`report_generator.db`) with the following tables:

- **users**: User accounts with email and password hash
- **drafts**: Saved report drafts
- **login_sessions**: Login history and device tracking
- **known_devices**: Device fingerprints for security
- **password_reset_tokens**: Password reset tokens

## Security Monitoring

The system tracks:
- Device information (browser, OS)
- IP addresses
- Login times
- New device logins (alerts sent to admin)

To view new device logins, check the console output or implement email notifications in `app.py` (in the login route where it prints the alert).

## File Uploads

Uploaded files are stored in the `uploads/` directory:
- `uploads/signatures/` - Digital signatures
- `uploads/speaker/` - Speaker photos
- `uploads/photos/` - Activity photos
- `uploads/attendance/` - Attendance lists
- `uploads/brochure/` - Brochures
- `uploads/notice/` - Notices
- `uploads/feedback/` - Feedback analysis
- `uploads/impact/` - Impact analysis

## Troubleshooting

### PDF Conversion Not Working
- Ensure `poppler` is installed and in PATH
- Check that `pdf2image` package is installed: `pip install pdf2image`

### Database Errors
- Delete `report_generator.db` and restart the application
- Check file permissions in the project directory

### Authentication Issues
- Verify email is in `ALLOWED_EMAILS` in `config.py`
- Check that database is initialized
- Ensure Flask-Login is installed: `pip install Flask-Login Flask-Bcrypt`

### Image Upload Issues
- Check file size (max 10MB per file)
- Verify file format (JPG, PNG, or PDF)
- Check `uploads/` directory permissions

## Production Deployment

For production:

1. **Change Secret Key**: Use a strong random secret key
2. **Use Production Database**: Consider PostgreSQL or MySQL instead of SQLite
3. **Set Up Email**: Implement email sending for password resets and alerts
4. **Use HTTPS**: Deploy behind HTTPS/SSL
5. **Set Up Backups**: Regular database backups
6. **Configure Logging**: Set up proper logging for security events
7. **Use WSGI Server**: Use Gunicorn or uWSGI instead of Flask dev server

## Support

For issues or questions, contact the system administrator.

