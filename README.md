# Network & System Engineer Portfolio Website

A professional Flask-based portfolio website with a secure admin portal for managing content dynamically. Designed specifically for Network and System Engineers with a tech-themed dark mode interface.

## Features

### Public Portfolio
- **Hero Section** with animated grid background and tech-inspired design
- **About Section** with terminal-style presentation
- **Skills Showcase** organized by category (Networking, Systems, Virtualization, Cloud, Automation)
- **Projects Gallery** with filtering and detailed project cards
- **Testimonials** from clients and colleagues
- **Contact Form** with database storage

### Admin Portal
- **Secure Authentication** with password hashing and session management
- **Dashboard** with overview statistics
- **CRUD Operations** for:
  - Projects (add, edit, delete with images and technologies)
  - Skills (manage proficiency levels and categories)
  - Testimonials (client feedback management)
  - Contact Messages (view and manage inquiries)
- **CSRF Protection** on all forms
- **Responsive Design** optimized for all devices

## Security Features

- ✅ Password hashing with Werkzeug Security
- ✅ Session management with Flask-Login
- ✅ CSRF protection on all forms (Flask-WTF)
- ✅ Open redirect protection
- ✅ Secure admin password enforcement (min 8 characters)
- ✅ Environment variable validation

## Technology Stack

**Backend:**
- Flask (Python web framework)
- SQLAlchemy (ORM for database)
- PostgreSQL (database)
- Flask-Login (authentication)
- Flask-WTF (forms and CSRF protection)

**Frontend:**
- Jinja2 (templating)
- Tailwind CSS (responsive design)
- Font Awesome (icons)
- Custom CSS with dark mode theme

## Setup Instructions

### Prerequisites
- Python 3.x
- PostgreSQL database

### Environment Variables

The following environment variables are **required**:

```bash
SESSION_SECRET=your-secure-random-secret-key
DATABASE_URL=postgresql://user:password@host:port/database
ADMIN_PASSWORD=your-strong-admin-password-min-8-chars
```

These are already configured in Replit. For local development, create a `.env` file.

### Installation

1. Install dependencies:
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf gunicorn python-dotenv psycopg2-binary
```

2. Initialize the database:
```bash
python init_db.py
```
This will create all tables and populate with sample data for a Network/System Engineer portfolio.

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Admin Access

**Username:** `admin`  
**Password:** Set via `ADMIN_PASSWORD` environment variable or prompted during database initialization

Access the admin panel at: `http://localhost:5000/admin/login`

## Project Structure

```
.
├── app.py                  # Main application entry point
├── config.py              # Configuration settings
├── models.py              # Database models
├── forms.py               # WTForms definitions
├── init_db.py             # Database initialization script
├── routes/
│   ├── public.py          # Public-facing routes
│   └── admin.py           # Admin panel routes
├── templates/
│   ├── base.html          # Base template
│   ├── public/            # Public page templates
│   ├── admin/             # Admin panel templates
│   └── errors/            # Error pages
└── static/
    ├── css/               # Custom styles
    ├── js/                # JavaScript files
    └── images/            # Image assets

## Customization

### Adding Projects
1. Log in to admin panel
2. Navigate to "Projects"
3. Click "Add Project"
4. Fill in project details, technologies, and image URL
5. Set display order (lower numbers appear first)

### Managing Skills
1. Skills are organized by category
2. Set proficiency level (0-100)
3. Categories: Networking, Systems, Virtualization, Cloud, Automation

### Contact Messages
- All contact form submissions are stored in the database
- Admin can view, mark as read, and delete messages
- Unread messages are highlighted

## Production Deployment

For production deployment:

1. **Disable Debug Mode:** Set `debug=False` in `app.py`
2. **Use Production Server:** Deploy with Gunicorn instead of Flask dev server
3. **Set Strong Secrets:** Ensure all environment variables use strong, random values
4. **Enable HTTPS:** Use SSL/TLS certificates
5. **Database Backups:** Set up regular PostgreSQL backups

Example Gunicorn command:
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

## Sample Data

The database initialization includes sample data for:
- 6 Infrastructure projects (Network redesign, VMware deployment, AWS migration, etc.)
- 20 Skills across 5 categories
- 3 Professional testimonials

You can delete or modify this sample data through the admin panel after initialization.

## License

This is a personal portfolio website. All rights reserved.

## Support

For issues or questions, use the contact form on the website.
