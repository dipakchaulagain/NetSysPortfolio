# Project Information

## Overview
Professional portfolio website for a Network and System Engineer built with Flask. Features a modern dark-theme UI with network/infrastructure aesthetics and a secure admin portal for content management.

## Recent Changes
- **October 27, 2025**: Initial project creation
  - Implemented Flask application with blueprints architecture
  - Created database models for User, Project, Skill, Testimonial, and ContactMessage
  - Built secure authentication system with password hashing
  - Designed tech-themed responsive UI with Tailwind CSS
  - Implemented CRUD operations for all content types
  - Added CSRF protection and security hardening
  - Populated database with sample Network/System Engineer portfolio data

## User Preferences
- Tech/engineering theme with dark mode (cyan/green accent colors)
- Terminal and infrastructure-inspired design elements
- Professional presentation suitable for enterprise IT environments

## Project Architecture

### Backend Structure
- **app.py**: Main application factory and configuration
- **models.py**: SQLAlchemy database models
- **forms.py**: WTForms for validation and CSRF protection
- **routes/**: Blueprint-based routing
  - `public.py`: Public-facing portfolio pages
  - `admin.py`: Admin panel with authentication

### Frontend Structure
- **templates/**: Jinja2 templates
  - `public/`: Homepage, projects, contact
  - `admin/`: Dashboard, CRUD forms, message inbox
- **static/**: CSS, JavaScript, and assets

### Database Models
1. **User**: Admin authentication (hashed passwords)
2. **Project**: Portfolio projects with images, tech stack, links
3. **Skill**: Technical skills with proficiency levels and categories
4. **Testimonial**: Client/colleague recommendations
5. **ContactMessage**: Form submissions from visitors

### Security Features
- CSRF protection on all forms (Flask-WTF)
- Password hashing (Werkzeug Security)
- Session management (Flask-Login)
- Open redirect protection
- Mandatory environment secrets (SESSION_SECRET, DATABASE_URL)
- Admin password strength validation (min 8 characters)

## Key Dependencies
- Flask: Web framework
- Flask-SQLAlchemy: ORM
- Flask-Login: Authentication
- Flask-WTF: Forms and CSRF
- PostgreSQL: Database (via DATABASE_URL env variable)
- Gunicorn: Production WSGI server
- Tailwind CSS: Frontend framework (CDN)

## Environment Variables
Required secrets already configured in Replit:
- `SESSION_SECRET`: Flask session encryption key
- `DATABASE_URL`: PostgreSQL connection string
- `ADMIN_PASSWORD`: Admin user password (min 8 chars)

## Admin Credentials
- **Username**: admin
- **Password**: Set via ADMIN_PASSWORD environment variable

## Development Notes
- Debug mode is enabled for development
- For production deployment, disable debug and use Gunicorn
- Sample data includes 6 projects, 20 skills, and 3 testimonials
- All delete operations use POST requests with CSRF tokens

## Future Enhancements
- Blog/articles section with WYSIWYG editor
- File upload for project images and documentation
- Advanced project filtering and search
- Analytics dashboard
- Email notifications for contact form submissions
- Resume download functionality
