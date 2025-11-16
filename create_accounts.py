"""
Script to create user accounts for all faculty members
Run this script to pre-create accounts with default passwords
"""
from database import create_user, get_user_by_email, init_db
from config import ALLOWED_EMAILS
import getpass

def create_faculty_accounts(default_password=None):
    """Create accounts for all faculty members in ALLOWED_EMAILS"""
    
    # Initialize database
    init_db()
    
    if default_password is None:
        print("\n" + "="*60)
        print("Faculty Account Creation Script")
        print("="*60)
        print("\nThis script will create accounts for all faculty members")
        print("listed in config.py with a default password.")
        print("\nIMPORTANT: Faculty members should change their password")
        print("after first login for security.")
        print("\n" + "-"*60)
        
        # Get default password
        while True:
            password = getpass.getpass("\nEnter default password for all accounts: ")
            if len(password) < 6:
                print("Password must be at least 6 characters long. Try again.")
                continue
            
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("Passwords do not match. Try again.")
                continue
            break
    else:
        password = default_password
    
    print(f"\nCreating accounts for {len(ALLOWED_EMAILS)} faculty members...")
    print("-"*60)
    
    created_count = 0
    existing_count = 0
    error_count = 0
    
    for email in ALLOWED_EMAILS:
        email = email.strip().lower()
        
        # Check if user already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            print(f"⚠️  {email} - Account already exists (skipped)")
            existing_count += 1
            continue
        
        # Create account
        user_id = create_user(email, password)
        if user_id:
            print(f"✅ {email} - Account created successfully")
            created_count += 1
        else:
            print(f"❌ {email} - Failed to create account")
            error_count += 1
    
    print("\n" + "="*60)
    print("Summary:")
    print(f"  ✅ Created: {created_count} accounts")
    print(f"  ⚠️  Already existed: {existing_count} accounts")
    print(f"  ❌ Errors: {error_count} accounts")
    print("="*60)
    
    if created_count > 0:
        print(f"\n✅ Successfully created {created_count} new accounts!")
        print(f"\nDefault password: {password}")
        print("\n📧 Please inform faculty members:")
        print("   1. Their email address (login username)")
        print("   2. The default password")
        print("   3. They should change their password after first login")
        print("   4. Login URL: http://localhost:5000 (or your server URL)")
    
    return created_count, existing_count, error_count

if __name__ == '__main__':
    try:
        create_faculty_accounts()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

