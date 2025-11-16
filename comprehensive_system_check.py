"""
Comprehensive System Check - Verifies all components work correctly
"""
import sys
import os
import traceback
from datetime import datetime

print("=" * 70)
print("COMPREHENSIVE SYSTEM CHECK")
print("=" * 70)
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

errors = []
warnings = []
success_count = 0

def check(name, func):
    """Run a check and track results"""
    global success_count
    try:
        result = func()
        if result:
            print(f"[OK] {name}")
            success_count += 1
            return True
        else:
            print(f"[WARNING] {name} - Check returned False")
            warnings.append(name)
            return False
    except Exception as e:
        print(f"[ERROR] {name} - {str(e)}")
        errors.append(f"{name}: {str(e)}")
        traceback.print_exc()
        return False

# 1. Check Python version
def check_python_version():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        return True
    raise Exception(f"Python 3.8+ required, found {version.major}.{version.minor}")

check("Python Version (3.8+)", check_python_version)

# 2. Check required files exist
def check_required_files():
    required_files = [
        'app.py', 'config.py', 'database.py', 'report_logic.py',
        'geolocation.py', 'logging_config.py', 'requirements.txt',
        'gunicorn_config.py', 'set_admin_password.py'
    ]
    missing = []
    for f in required_files:
        if not os.path.exists(f):
            missing.append(f)
    if missing:
        raise Exception(f"Missing files: {', '.join(missing)}")
    return True

check("Required Files Exist", check_required_files)

# 3. Check template files
def check_templates():
    templates_dir = 'templates'
    if not os.path.exists(templates_dir):
        raise Exception("Templates directory not found")
    
    required_templates = [
        'landing.html', 'login.html', 'register.html', 'dashboard.html',
        'index.html', 'admin_panel.html', 'contact.html'
    ]
    missing = []
    for t in required_templates:
        if not os.path.exists(os.path.join(templates_dir, t)):
            missing.append(t)
    if missing:
        raise Exception(f"Missing templates: {', '.join(missing)}")
    return True

check("Template Files Exist", check_templates)

# 4. Check static files
def check_static():
    if not os.path.exists('static'):
        os.makedirs('static', exist_ok=True)
    return True

check("Static Directory", check_static)

# 5. Test imports
def test_imports():
    try:
        import flask
        import flask_login
        from werkzeug.security import generate_password_hash
        from reportlab.lib.pagesizes import A4
        from PIL import Image
        import sqlite3
        return True
    except ImportError as e:
        raise Exception(f"Missing import: {e}")

check("Core Imports", test_imports)

# 6. Test config import
def test_config():
    try:
        from config import ALLOWED_EMAILS, ADMIN_EMAIL, SECRET_KEY
        if not ALLOWED_EMAILS:
            raise Exception("ALLOWED_EMAILS is empty")
        if not ADMIN_EMAIL:
            raise Exception("ADMIN_EMAIL is not set")
        return True
    except Exception as e:
        raise Exception(f"Config error: {e}")

check("Configuration", test_config)

# 7. Test database initialization
def test_database():
    try:
        from database import init_db, get_db
        init_db()
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        required_tables = ['users', 'drafts', 'login_sessions', 'saved_signatures']
        missing = [t for t in required_tables if t not in tables]
        if missing:
            raise Exception(f"Missing tables: {', '.join(missing)}")
        conn.close()
        return True
    except Exception as e:
        raise Exception(f"Database error: {e}")

check("Database Initialization", test_database)

# 8. Test database functions
def test_database_functions():
    try:
        from database import (
            create_user, verify_user, get_user_by_email,
            save_draft, get_user_drafts, get_draft_by_id
        )
        return True
    except Exception as e:
        raise Exception(f"Database functions error: {e}")

check("Database Functions", test_database_functions)

# 9. Test report logic imports
def test_report_logic():
    try:
        from report_logic import (
            generate_report_pdf, ensure_image_resized,
            convert_pdf_to_images, image_flowable
        )
        return True
    except Exception as e:
        raise Exception(f"Report logic error: {e}")

check("Report Logic Imports", test_report_logic)

# 10. Test geolocation
def test_geolocation():
    try:
        from geolocation import get_location_from_ip, format_location_string
        # Test with a dummy IP
        result = get_location_from_ip("8.8.8.8")
        return True
    except Exception as e:
        raise Exception(f"Geolocation error: {e}")

check("Geolocation Functions", test_geolocation)

# 11. Test logging config
def test_logging():
    try:
        from logging_config import setup_logging
        from flask import Flask
        test_app = Flask(__name__)
        setup_logging(test_app)
        return True
    except Exception as e:
        raise Exception(f"Logging error: {e}")

check("Logging Configuration", test_logging)

# 12. Test Flask app initialization
def test_flask_app():
    try:
        from app import app
        # Check routes
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        required_routes = ['/', '/login', '/register', '/dashboard', '/report', '/admin']
        missing = []
        for route in required_routes:
            if not any(route in r for r in routes):
                missing.append(route)
        if missing:
            raise Exception(f"Missing routes: {', '.join(missing)}")
        return True
    except Exception as e:
        raise Exception(f"Flask app error: {e}")

check("Flask Application", test_flask_app)

# 13. Test admin password script
def test_admin_password_script():
    try:
        import set_admin_password
        # Just check it imports without error
        return True
    except Exception as e:
        raise Exception(f"Admin password script error: {e}")

check("Admin Password Script", test_admin_password_script)

# 14. Test report generation with minimal data
def test_report_generation():
    try:
        from report_logic import generate_report_pdf
        test_data = {
            'general_info': {
                'Activity Type': 'Test',
                'Sub Category': 'Test',
                'Start Date': '2025-01-15',
                'End Date': '2025-01-15',
                'Start Time': '10:00',
                'End Time': '11:00',
                'Venue': 'Test Venue'
            },
            'speakers': [{
                'name': 'Test Speaker',
                'title': 'Test',
                'organization': 'Test',
                'contact': 'test@test.com',
                'presentation_title': 'Test'
            }],
            'participants': [{'type': 'Student', 'count': '10'}],
            'synopsis': {
                'highlights': 'Test',
                'key_takeaways': 'Test',
                'summary': 'Test',
                'follow_up': 'Test'
            },
            'preparers': [{'name': 'Test', 'designation': 'Test'}],
            'speaker_profile': {},
            'photos': [],
            'attendance_list': [],
            'brochure': [],
            'notice': [],
            'feedback': [],
            'impact': []
        }
        pdf_bytes, filename = generate_report_pdf(test_data)
        if not pdf_bytes or len(pdf_bytes) == 0:
            raise Exception("Generated PDF is empty")
        if not filename.endswith('.pdf'):
            raise Exception("Filename doesn't end with .pdf")
        return True
    except Exception as e:
        raise Exception(f"Report generation error: {e}")

check("Report Generation (Minimal Data)", test_report_generation)

# 15. Test user creation
def test_user_creation():
    try:
        from database import create_user, verify_user, get_user_by_email
        # Create test user
        test_email = f"test_{datetime.now().timestamp()}@test.com"
        user_id = create_user(test_email, "testpass123")
        if not user_id:
            raise Exception("User creation returned None")
        
        # Verify user
        user_data = verify_user(test_email, "testpass123")
        if not user_data:
            raise Exception("User verification failed")
        
        # Get user by email
        user = get_user_by_email(test_email)
        if not user:
            raise Exception("get_user_by_email returned None")
        
        return True
    except Exception as e:
        raise Exception(f"User creation error: {e}")

check("User Creation & Verification", test_user_creation)

# 16. Test draft operations
def test_draft_operations():
    try:
        from database import save_draft, get_user_drafts, get_draft_by_id
        from database import create_user
        
        # Create test user
        test_email = f"test_draft_{datetime.now().timestamp()}@test.com"
        user_id = create_user(test_email, "testpass123")
        
        # Save draft
        draft_id = save_draft(user_id, "Test Draft", {"test": "data"})
        if not draft_id:
            raise Exception("Draft save returned None")
        
        # Get user drafts
        drafts = get_user_drafts(user_id)
        if len(drafts) == 0:
            raise Exception("No drafts found after saving")
        
        # Get draft by ID
        draft = get_draft_by_id(draft_id)
        if not draft:
            raise Exception("get_draft_by_id returned None")
        
        return True
    except Exception as e:
        raise Exception(f"Draft operations error: {e}")

check("Draft Operations", test_draft_operations)

# 17. Test image processing
def test_image_processing():
    try:
        from PIL import Image
        import tempfile
        
        # Create test image
        img = Image.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        img.save(temp_file.name, 'JPEG')
        temp_file.close()
        
        # Test image resizing
        from report_logic import ensure_image_resized
        result = ensure_image_resized(temp_file.name)
        if result and os.path.exists(result):
            os.remove(result)
        if temp_file.name != result and os.path.exists(temp_file.name):
            os.remove(temp_file.name)
        
        return True
    except Exception as e:
        raise Exception(f"Image processing error: {e}")

check("Image Processing", test_image_processing)

# 18. Check upload directories
def check_upload_directories():
    try:
        upload_dirs = [
            'uploads/photos', 'uploads/speaker', 'uploads/signatures',
            'uploads/attendance', 'uploads/brochure', 'uploads/notice',
            'uploads/feedback', 'uploads/impact'
        ]
        for dir_path in upload_dirs:
            os.makedirs(dir_path, exist_ok=True)
        return True
    except Exception as e:
        raise Exception(f"Upload directories error: {e}")

check("Upload Directories", check_upload_directories)

# 19. Check logs directory
def check_logs_directory():
    try:
        os.makedirs('logs', exist_ok=True)
        return True
    except Exception as e:
        raise Exception(f"Logs directory error: {e}")

check("Logs Directory", check_logs_directory)

# 20. Test admin password functionality
def test_admin_password():
    try:
        from database import get_user_by_email
        from config import ADMIN_EMAIL
        
        # Check if admin user exists
        admin_user = get_user_by_email(ADMIN_EMAIL.lower())
        if not admin_user:
            warnings.append("Admin user not found - run set_admin_password.py")
            return True  # Not an error, just a warning
        
        # Check if admin has password set
        if not admin_user.get('password_hash'):
            warnings.append("Admin password not set - run set_admin_password.py")
            return True
        
        return True
    except Exception as e:
        raise Exception(f"Admin password check error: {e}")

check("Admin Password Check", test_admin_password)

# 21. Test all routes are accessible
def test_routes():
    try:
        from app import app
        with app.test_client() as client:
            # Test public routes
            routes_to_test = [
                ('/', 'GET'),
                ('/login', 'GET'),
                ('/register', 'GET'),
                ('/privacy-policy', 'GET'),
                ('/terms-of-use', 'GET'),
                ('/contact', 'GET'),
            ]
            
            for route, method in routes_to_test:
                if method == 'GET':
                    response = client.get(route)
                    if response.status_code == 500:
                        raise Exception(f"Route {route} returned 500 error")
        
        return True
    except Exception as e:
        raise Exception(f"Routes test error: {e}")

check("Route Accessibility", test_routes)

# Summary
print()
print("=" * 70)
print("SYSTEM CHECK SUMMARY")
print("=" * 70)
print(f"Total Checks: {success_count + len(errors) + len(warnings)}")
print(f"Successful: {success_count}")
print(f"Warnings: {len(warnings)}")
print(f"Errors: {len(errors)}")
print()

if warnings:
    print("WARNINGS:")
    for w in warnings:
        print(f"  - {w}")
    print()

if errors:
    print("ERRORS:")
    for e in errors:
        print(f"  - {e}")
    print()
    print("=" * 70)
    print("SYSTEM CHECK FAILED - Please fix errors above")
    print("=" * 70)
    sys.exit(1)
else:
    print("=" * 70)
    print("SYSTEM CHECK PASSED - All components working correctly!")
    print("=" * 70)
    if warnings:
        print("\nNote: Some warnings were found but they are not critical.")
    sys.exit(0)

