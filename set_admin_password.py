"""
Script to set or update admin password
Usage: python set_admin_password.py [password]
If password not provided, will prompt for it
"""
import sys
import getpass
from database import get_user_by_email, create_user, get_db
from werkzeug.security import generate_password_hash, check_password_hash

def set_admin_password(password):
    """Set or update admin password"""
    from config import ADMIN_EMAIL
    
    # Get database connection
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if admin user exists
    cursor.execute('SELECT * FROM users WHERE email = ?', (ADMIN_EMAIL.lower(),))
    admin_user = cursor.fetchone()
    
    if admin_user:
        # Update existing admin password
        password_hash = generate_password_hash(password)
        cursor.execute(
            'UPDATE users SET password_hash = ? WHERE email = ?',
            (password_hash, ADMIN_EMAIL.lower())
        )
        conn.commit()
        conn.close()
        print(f"[OK] Admin password updated successfully for {ADMIN_EMAIL}")
        return True
    else:
        # Create admin user
        password_hash = generate_password_hash(password)
        cursor.execute(
            'INSERT INTO users (email, password_hash) VALUES (?, ?)',
            (ADMIN_EMAIL.lower(), password_hash)
        )
        conn.commit()
        conn.close()
        print(f"[OK] Admin account created with password for {ADMIN_EMAIL}")
        return True

if __name__ == '__main__':
    print("=" * 60)
    print("Set Admin Password")
    print("=" * 60)
    print()
    
    # Get password from command line or prompt
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = getpass.getpass("Enter admin password: ")
        confirm_password = getpass.getpass("Confirm admin password: ")
        
        if password != confirm_password:
            print("[ERROR] Passwords do not match!")
            sys.exit(1)
    
    if len(password) < 6:
        print("[ERROR] Password must be at least 6 characters long!")
        sys.exit(1)
    
    # Set password
    try:
        from config import ADMIN_EMAIL
        set_admin_password(password)
        print()
        print("=" * 60)
        print("Admin password set successfully!")
        print("=" * 60)
        print(f"Admin email: {ADMIN_EMAIL}")
        print("You can now login with this email and password.")
    except Exception as e:
        print(f"[ERROR] Error setting admin password: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

