# Network & System Engineer Portfolio Website

A professional Flask-based portfolio website with a secure admin portal for managing content dynamically. Designed specifically for Network and System Engineers with a tech-themed dark mode interface featuring cyan and green accent colors with terminal-style aesthetics.

## 🚀 Features

### Public Portfolio
- **Hero Section** - Eye-catching terminal-style header with animated grid background
- **About Section** - Professional introduction with tech-inspired design
- **Skills Showcase** - 20+ technical skills organized by category with proficiency bars
  - Categories: Networking, Systems, Virtualization, Cloud, Automation, Security
- **Professional Experience** - Career timeline with detailed work history
- **Projects Gallery** - Showcase your infrastructure projects with images and tech stacks
- **Testimonials** - Client and colleague recommendations
- **Contact Form** - Visitor inquiries with database storage and admin inbox

### Admin Portal
- **Secure Authentication** - Password hashing and session management
- **Dashboard** - Overview statistics for all content types
- **CRUD Operations** for:
  - **Projects** - Add, edit, delete with images, technologies, and GitHub links
  - **Skills** - Manage proficiency levels and categories
  - **Experience** - Add professional work history with company, title, dates
  - **Testimonials** - Manage client feedback
  - **Contact Messages** - View and manage visitor inquiries
- **CSRF Protection** - All forms protected against cross-site request forgery
- **Responsive Design** - Optimized for desktop, tablet, and mobile

## 🔒 Security Features

- ✅ Password hashing with Werkzeug Security (bcrypt)
- ✅ Session management with Flask-Login
- ✅ CSRF protection on all forms (Flask-WTF)
- ✅ Open redirect protection
- ✅ Secure admin password enforcement (minimum 8 characters)
- ✅ Environment variable validation
- ✅ PostgreSQL database with proper foreign key constraints

## 🛠️ Technology Stack

**Backend:**
- Flask 3.x - Python web framework
- SQLAlchemy - ORM for database operations
- PostgreSQL (Neon) - Production-grade database
- Flask-Login - User authentication
- Flask-WTF - Forms and CSRF protection
- Werkzeug - Password hashing and security utilities
- Gunicorn - Production WSGI server

**Frontend:**
- Jinja2 - Server-side templating
- Tailwind CSS 3.x - Utility-first CSS framework
- Font Awesome 6.x - Icon library
- Custom CSS - Dark mode theme with cyan/green accents

**Development:**
- Python 3.11
- UV - Fast Python package manager
- PostgreSQL 15+

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL database (automatically configured in Replit)
- UV package manager (automatically configured in Replit)

## 🔧 Environment Variables

The following environment variables are **required** and already configured in Replit:

```bash
SESSION_SECRET=your-secure-random-secret-key
DATABASE_URL=postgresql://user:password@host:port/database
PGHOST=your-postgres-host
PGPORT=5432
PGUSER=your-postgres-user
PGPASSWORD=your-postgres-password
PGDATABASE=your-database-name
```

For local development, create a `.env` file with these variables.

## 🚀 Quick Start (Replit)

The application is already configured and running in Replit:

1. **View the live site** - Click the webview or open the URL
2. **Access admin panel** - Click "Admin" in the top-right corner
   - Username: `admin`
   - Password: `admin123` (change this in production!)
3. **Start customizing** - Log in to the admin panel to update content

## 💻 Local Development Setup

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd <project-directory>
```

2. **Install dependencies using UV:**
```bash
uv pip install -r requirements.txt
```

Or using pip:
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf flask-dance \
            gunicorn python-dotenv psycopg2-binary email-validator \
            wtforms werkzeug oauthlib pyjwt
```

3. **Set up environment variables:**
Create a `.env` file in the project root:
```bash
SESSION_SECRET=your-random-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
```

4. **Initialize and populate the database:**
```bash
uv run python populate_db.py
```

This script will:
- Create all database tables (User, Project, Skill, Experience, Testimonial, ContactMessage)
- Create an admin user (username: admin, password: admin123)
- Populate with realistic sample data:
  - 21 technical skills across 6 categories
  - 6 infrastructure projects
  - 3 professional experiences
  - 3 testimonials

5. **Run the application:**
```bash
uv run python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
.
├── app.py                     # Main Flask application and configuration
├── models.py                  # SQLAlchemy database models
├── forms.py                   # WTForms for validation and CSRF
├── populate_db.py             # Database initialization and sample data
├── requirements.txt           # Python dependencies
├── routes/
│   ├── __init__.py
│   ├── public.py              # Public-facing routes (home, projects, contact)
│   └── admin.py               # Admin panel routes (CRUD operations)
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── public/
│   │   └── index.html         # Main public portfolio page
│   ├── admin/
│   │   ├── base_admin.html    # Admin panel base template
│   │   ├── dashboard.html     # Admin dashboard
│   │   ├── login.html         # Admin login page
│   │   ├── projects.html      # Project management
│   │   ├── project_form.html  # Add/edit project
│   │   ├── skills.html        # Skill management
│   │   ├── skill_form.html    # Add/edit skill
│   │   ├── experiences.html   # Experience management
│   │   ├── experience_form.html  # Add/edit experience
│   │   ├── testimonials.html  # Testimonial management
│   │   ├── testimonial_form.html # Add/edit testimonial
│   │   └── messages.html      # Contact message inbox
│   └── errors/
│       └── 404.html           # Custom 404 error page
└── static/
    ├── css/
    │   └── style.css          # Custom styles and animations
    └── js/
        └── main.js            # Client-side JavaScript

```

## 📊 Database Models

### User
- Admin authentication with hashed passwords
- Username and email fields
- Used for admin panel access

### Project
- Portfolio projects showcase
- Fields: title, description, image_url, github_url, demo_url, technologies, display_order
- Technologies stored as comma-separated string

### Skill
- Technical skills with proficiency levels
- Fields: name, category, proficiency (0-100), display_order
- Categories: Networking, Systems, Virtualization, Cloud, Automation, Security

### Experience
- Professional work history
- Fields: company, title, location, start_date, end_date, description, display_order
- Supports current positions (end_date can be null)

### Testimonial
- Client and colleague recommendations
- Fields: name, role, company, content, display_order

### ContactMessage
- Visitor inquiries from contact form
- Fields: name, email, subject, message, is_read, created_at
- Admin can mark as read and delete

## 🎨 Customization Guide

### Adding/Editing Projects

1. Log in to the admin panel (`/admin/login`)
2. Navigate to "Projects"
3. Click "Add Project"
4. Fill in the form:
   - **Title**: Project name
   - **Description**: Detailed project description
   - **Image URL**: Link to project screenshot/logo
   - **GitHub URL**: Repository link (optional)
   - **Demo URL**: Live demo link (optional)
   - **Technologies**: Comma-separated list (e.g., "Cisco, MPLS, BGP")
   - **Display Order**: Lower numbers appear first (e.g., 1, 2, 3)
5. Click "Save Project"

### Managing Skills

1. Navigate to "Skills" in the admin panel
2. Add new skills with:
   - **Name**: Skill name (e.g., "VMware vSphere")
   - **Category**: Choose from dropdown (Networking, Systems, etc.)
   - **Proficiency**: 0-100 (shows as progress bar)
   - **Display Order**: Order within category
3. Edit or delete existing skills

### Adding Professional Experience

1. Navigate to "Experiences" in the admin panel
2. Add work history entries:
   - **Company**: Company name
   - **Title**: Job title
   - **Location**: City, State/Country (optional)
   - **Start Date**: Format: MMM YYYY (e.g., "Jan 2020")
   - **End Date**: Format: MMM YYYY or leave blank for current position
   - **Description**: Achievements and responsibilities
   - **Display Order**: Most recent jobs should have lower numbers
3. Current positions will display "Present" instead of end date

### Managing Testimonials

1. Navigate to "Testimonials"
2. Add client/colleague recommendations:
   - **Name**: Person's name
   - **Role**: Their job title
   - **Company**: Their company
   - **Content**: The testimonial text
   - **Display Order**: Order of appearance

### Viewing Contact Messages

1. Navigate to "Messages" in the admin panel
2. View all contact form submissions
3. Mark as read (changes background color)
4. Delete spam or resolved messages
5. Unread messages are highlighted for easy identification

## 🎨 Customizing the Theme

### Colors
The theme uses CSS variables defined in `static/css/style.css`:
- Primary: Cyan (#06b6d4)
- Secondary: Green (#10b981)
- Background: Dark navy (#0f172a, #1e293b)

To change colors, edit the CSS variables or Tailwind classes in templates.

### Fonts
Currently using system fonts. To add custom fonts:
1. Link Google Fonts or upload font files
2. Update `font-family` in base templates

### Layout
All templates use Tailwind CSS utility classes. Modify classes directly in templates for layout changes.

## 🚀 Production Deployment

### Using Replit Deploy

1. Click the "Deploy" button in Replit
2. Configure deployment settings:
   - Deployment target: Autoscale or VM
   - Environment variables are automatically included
3. Click "Deploy"

### Manual Deployment

For deployment to other platforms:

1. **Disable Debug Mode:**
   - Set `debug=False` in `app.py`

2. **Use Production Server:**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
   ```

3. **Set Strong Secrets:**
   - Generate a strong SESSION_SECRET: `python -c "import secrets; print(secrets.token_hex(32))"`
   - Change the admin password from default

4. **Enable HTTPS:**
   - Use SSL/TLS certificates (Let's Encrypt recommended)
   - Configure reverse proxy (Nginx/Apache)

5. **Database Backups:**
   - Set up regular PostgreSQL backups
   - Consider automated backup solutions

6. **Environment Variables:**
   - Ensure all secrets are properly configured
   - Never commit secrets to version control

### Production Checklist

- [ ] Change admin password from default
- [ ] Set strong SESSION_SECRET
- [ ] Disable Flask debug mode
- [ ] Use Gunicorn or similar WSGI server
- [ ] Enable HTTPS/SSL
- [ ] Set up database backups
- [ ] Configure error monitoring
- [ ] Set up logging
- [ ] Test all admin features
- [ ] Test contact form submissions
- [ ] Verify responsive design on all devices

## 📝 Sample Data

The `populate_db.py` script includes comprehensive sample data:

**Skills (21 total):**
- Networking: Cisco IOS, Juniper JunOS, MPLS, BGP, OSPF, VLANs
- Virtualization: VMware vSphere, VMware NSX, Hyper-V
- Systems: Linux Administration, Windows Server, Active Directory
- Cloud: AWS, Azure, Terraform
- Automation: Python, Ansible, Bash Scripting
- Security: Firewalls, VPN, IDS/IPS

**Projects (6 total):**
- Enterprise Network Redesign
- VMware vSphere Deployment
- AWS Cloud Migration
- Network Security Enhancement
- SD-WAN Implementation
- Automated Backup Solution

**Professional Experience (3 entries):**
- Senior Network Engineer at TechCorp Solutions (2020-Present)
- Network & Systems Administrator at Global Tech Services (2017-2020)
- Junior Network Engineer at DataFlow Inc. (2015-2017)

**Testimonials (3 entries):**
- Network architecture testimonial
- Project management testimonial
- Problem-solving testimonial

You can delete or modify all sample data through the admin panel.

## 🔍 Admin Panel Features

### Dashboard
- Total counts for projects, skills, experiences, and testimonials
- Unread message count with alert badge
- Quick navigation to all management sections

### Project Management
- List all projects with preview
- Add new projects with rich details
- Edit existing projects
- Delete projects (with confirmation)
- Reorder projects via display_order

### Skill Management
- Organized by category
- Visual proficiency bars
- Add, edit, delete skills
- Category-based organization

### Experience Management
- Chronological work history
- Support for current positions
- Location information (optional)
- Detailed job descriptions

### Message Inbox
- View all contact submissions
- Mark messages as read/unread
- Delete messages
- Visual highlighting for unread messages
- Sender details (name, email, subject)

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Check PostgreSQL is running
psql $DATABASE_URL

# Reinitialize database
uv run python populate_db.py
```

### Admin Login Not Working
- Verify admin user exists in database
- Check ADMIN_PASSWORD environment variable
- Try resetting password by running populate_db.py again

### Styles Not Loading
- Check Tailwind CSS CDN is accessible
- Clear browser cache
- Verify static files are being served correctly

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use a different port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Contributing

This is a personal portfolio template. Feel free to fork and customize for your own use.

## 📄 License

This project is open source and available for personal use.

## 💬 Support

For questions or issues:
- Use the contact form on the live website
- Check the troubleshooting section above
- Review Flask and PostgreSQL documentation

---

**Built with Flask and ❤️ for Network and System Engineers**
