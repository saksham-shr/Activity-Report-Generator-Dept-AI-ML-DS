"""
Admin script to reset password for a specific user
Use this if a faculty member forgets their password
"""
from database import get_user_by_email, get_db
from werkzeug.security import generate_password_hash
import getpass

def reset_user_password(email, new_password=None):
    """Reset password for a user"""
    email = email.strip().lower()
    
    user = get_user_by_email(email)
    if not user:
        print(f"❌ User with email {email} not found.")
        return False
    
    if new_password is None:
        print(f"\nResetting password for: {email}")
        while True:
            password = getpass.getpass("Enter new password: ")
            if len(password) < 6:
                print("Password must be at least 6 characters long. Try again.")
                continue
            
            confirm = getpass.getpass("Confirm new password: ")
            if password != confirm:
                print("Passwords do not match. Try again.")
                continue
            break
    else:
        password = new_password
    
    # Update password
    conn = get_db()
    cursor = conn.cursor()
    password_hash = generate_password_hash(password)
    cursor.execute(
        'UPDATE users SET password_hash = ? WHERE email = ?',
        (password_hash, email)
    )
    conn.commit()
    conn.close()
    
    print(f"✅ Password reset successfully for {email}")
    return True

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        email = sys.argv[1]
    else:
        email = input("Enter email address: ")
    
    try:
        reset_user_password(email)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

