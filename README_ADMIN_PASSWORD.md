# Admin Password Setup

## Setting Admin Password

The admin account requires a password to be set. Use the provided script to set or update the admin password.

### Method 1: Interactive (Recommended)
```bash
python set_admin_password.py
```
This will prompt you to enter and confirm the password securely.

### Method 2: Command Line
```bash
python set_admin_password.py "your-secure-password"
```

## Admin Account Details

- **Email**: `saksham.sharma@btech.christuniversity.in` (from config.py)
- **Password**: Set using `set_admin_password.py`

## First Time Setup

1. **Initialize database** (if not already done):
   ```bash
   python -c "from database import init_db; init_db()"
   ```

2. **Set admin password**:
   ```bash
   python set_admin_password.py
   ```

3. **Login**:
   - Visit the login page
   - Use admin email: `saksham.sharma@btech.christuniversity.in`
   - Use the password you just set

## Changing Admin Password

To change the admin password later:
```bash
python set_admin_password.py
```

## Security Notes

- The admin password is stored securely using bcrypt hashing
- Admin login attempts are logged
- Use a strong password (at least 6 characters, but recommend 12+)
- Never share the admin password

## Admin Features

Once logged in as admin, you have access to:
- `/admin` - Admin panel dashboard
- `/admin/users` - User management
- `/admin/locations` - All user locations
- `/admin/stats` - System statistics
- `/admin/unauthorized-access` - Security logs

## Troubleshooting

### "Invalid email or password" when logging in as admin
1. Verify admin email in `config.py` matches what you're using
2. Ensure admin password was set: `python set_admin_password.py`
3. Check if admin account exists in database

### Admin account doesn't exist
The script will automatically create the admin account if it doesn't exist when you set the password.

### Forgot admin password
Run the script again to reset:
```bash
python set_admin_password.py
```

