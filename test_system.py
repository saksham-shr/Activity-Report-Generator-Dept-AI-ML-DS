"""
Comprehensive system test to verify everything is working
"""
import sys
import os

print("=" * 60)
print("SYSTEM CHECK - Report Generator")
print("=" * 60)

errors = []
warnings = []

# 1. Check Python version
print("\n1. Checking Python version...")
if sys.version_info < (3, 7):
    errors.append(f"Python 3.7+ required. Found: {sys.version}")
    print(f"   ERROR: {sys.version}")
else:
    print(f"   OK: {sys.version.split()[0]}")

# 2. Check required packages
print("\n2. Checking required packages...")
required_packages = {
    'flask': 'Flask',
    'flask_login': 'Flask-Login',
    'werkzeug': 'Werkzeug',
    'reportlab': 'ReportLab',
    'PIL': 'Pillow',
    'requests': 'requests'
}

for module, package_name in required_packages.items():
    try:
        __import__(module)
        print(f"   OK: {package_name}")
    except ImportError:
        errors.append(f"Missing package: {package_name}")
        print(f"   ERROR: {package_name} not installed")

# 3. Check optional packages
print("\n3. Checking optional packages...")
try:
    import pdf2image
    print("   OK: pdf2image (PDF conversion available)")
except ImportError:
    warnings.append("pdf2image not installed - PDF conversion will not work")
    print("   WARNING: pdf2image not installed")

# 4. Check configuration file
print("\n4. Checking configuration...")
try:
    from config import ALLOWED_EMAILS, ADMIN_EMAIL, SECRET_KEY
    if len(ALLOWED_EMAILS) == 0:
        warnings.append("No emails in ALLOWED_EMAILS list")
        print("   WARNING: No emails configured in ALLOWED_EMAILS")
    else:
        print(f"   OK: {len(ALLOWED_EMAILS)} emails configured")
    
    if ADMIN_EMAIL == 'admin@christuniversity.in':
        warnings.append("Admin email not changed from default")
        print("   WARNING: Admin email is still default")
    else:
        print(f"   OK: Admin email set to {ADMIN_EMAIL}")
    
    if SECRET_KEY == 'your-secret-key-change-this-in-production':
        warnings.append("Secret key not changed from default")
        print("   WARNING: Secret key is still default (change for production)")
    else:
        print("   OK: Secret key configured")
except Exception as e:
    errors.append(f"Config error: {e}")
    print(f"   ERROR: {e}")

# 5. Check database
print("\n5. Checking database...")
try:
    from database import init_db, get_db
    init_db()
    conn = get_db()
    conn.close()
    print("   OK: Database initialized successfully")
except Exception as e:
    errors.append(f"Database error: {e}")
    print(f"   ERROR: {e}")

# 6. Check file structure
print("\n6. Checking file structure...")
required_files = [
    'app.py',
    'database.py',
    'report_logic.py',
    'geolocation.py',
    'config.py',
    'requirements.txt',
    'templates/index.html',
    'templates/landing.html',
    'templates/login.html',
    'templates/dashboard.html'
]

for file in required_files:
    if os.path.exists(file):
        print(f"   OK: {file}")
    else:
        errors.append(f"Missing file: {file}")
        print(f"   ERROR: {file} not found")

# 7. Check upload directories
print("\n7. Checking upload directories...")
upload_dirs = [
    'uploads',
    'uploads/photos',
    'uploads/speaker',
    'uploads/signatures',
    'uploads/attendance',
    'uploads/brochure',
    'uploads/notice',
    'uploads/feedback',
    'uploads/impact'
]

for dir_path in upload_dirs:
    if os.path.exists(dir_path):
        print(f"   OK: {dir_path}/")
    else:
        os.makedirs(dir_path, exist_ok=True)
        print(f"   CREATED: {dir_path}/")

# 8. Test imports
print("\n8. Testing imports...")
try:
    from app import app
    print("   OK: app.py imports successfully")
except Exception as e:
    errors.append(f"Import error in app.py: {e}")
    print(f"   ERROR: {e}")

try:
    from report_logic import generate_report_pdf
    print("   OK: report_logic.py imports successfully")
except Exception as e:
    errors.append(f"Import error in report_logic.py: {e}")
    print(f"   ERROR: {e}")

try:
    from geolocation import get_location_from_ip
    print("   OK: geolocation.py imports successfully")
except Exception as e:
    errors.append(f"Import error in geolocation.py: {e}")
    print(f"   ERROR: {e}")

# 9. Test database functions
print("\n9. Testing database functions...")
try:
    from database import (
        create_user, verify_user, get_user_by_email,
        save_draft, get_user_drafts, log_login_session
    )
    print("   OK: Database functions available")
except Exception as e:
    errors.append(f"Database function error: {e}")
    print(f"   ERROR: {e}")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

if errors:
    print(f"\nERRORS FOUND: {len(errors)}")
    for error in errors:
        print(f"  - {error}")
    print("\nPlease fix these errors before running the application.")
else:
    print("\nNo errors found!")

if warnings:
    print(f"\nWARNINGS: {len(warnings)}")
    for warning in warnings:
        print(f"  - {warning}")
    print("\nThese warnings should be addressed but won't prevent the app from running.")

if not errors:
    print("\n" + "=" * 60)
    print("SYSTEM READY!")
    print("=" * 60)
    print("\nYou can now run the application with:")
    print("  python app.py")
    print("\nThe application will be available at:")
    print("  http://localhost:5000")
else:
    print("\n" + "=" * 60)
    print("SYSTEM NOT READY")
    print("=" * 60)
    print("\nPlease install missing packages:")
    print("  pip install -r requirements.txt")
    sys.exit(1)

