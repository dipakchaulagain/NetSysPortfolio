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
- PostgreSQL - Production-grade database
- Flask-Login - User authentication
- Flask-WTF - Forms and CSRF protection
- Werkzeug - Password hashing and security utilities
- Gunicorn - Production WSGI server

**Frontend:**
- Jinja2 - Server-side templating
- Tailwind CSS 3.x - Utility-first CSS framework
- Font Awesome 6.x - Icon library
- Custom CSS - Dark mode theme with cyan/green accents

**Development & Deployment:**
- Python 3.11
- Docker & Docker Compose
- PostgreSQL 15+
- UV - Fast Python package manager

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: At least 2GB free space
- **Network**: Internet connection for downloading dependencies

### Required Software
- **Docker**: Version 20.10+ with Docker Compose
- **Git**: For cloning the repository
- **Text Editor**: VS Code, Sublime Text, or any preferred editor

### Docker Installation
Choose your operating system:

**Windows:**
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Run the installer and follow the setup wizard
3. Restart your computer when prompted
4. Verify installation: Open Command Prompt and run `docker --version`

**macOS:**
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Drag Docker to Applications folder
3. Launch Docker Desktop
4. Verify installation: Open Terminal and run `docker --version`

**Linux (Ubuntu/Debian):**
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install docker.io docker-compose

# Add user to docker group
sudo usermod -aG docker $USER

# Log out and log back in, then verify
docker --version
```

## 🔧 Environment Configuration

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd NetSysPortfolio
```

### 2. Environment Variables Setup
Copy the environment template and configure your settings:

```bash
cp env.template .env
```

Edit the `.env` file with your configuration:

```bash
# Flask Configuration
SESSION_SECRET=your-very-secure-random-secret-key-change-this-in-production
FLASK_ENV=development
FLASK_DEBUG=true

# Database Configuration
DATABASE_URL=postgresql://portfolio_user:portfolio_pass@db:5432/portfolio_db
PGHOST=db
PGPORT=5432
PGUSER=portfolio_user
PGPASSWORD=portfolio_pass
PGDATABASE=portfolio_db

# Admin Configuration
ADMIN_PASSWORD=your-strong-admin-password-minimum-8-characters

# Demo Data Configuration
POPULATE_DEMO_DATA=true
```

### 3. Generate Secure Secrets

**For SESSION_SECRET:**
```bash
# Generate a secure random key
python -c "import secrets; print(secrets.token_hex(32))"
```

**For ADMIN_PASSWORD:**
- Use a strong password with at least 8 characters
- Include uppercase, lowercase, numbers, and special characters
- Example: `MyStr0ng!P@ssw0rd`

## 🐳 Docker Deployment Guide

### Quick Start (Recommended)

1. **Start the application:**
```bash
docker-compose up -d
```

2. **Initialize the database:**
```bash
docker-compose exec web python populate_db.py
```

3. **Access the application:**
- **Website**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin/login
  - Username: `admin`
  - Password: `admin123` (or your ADMIN_PASSWORD)

### Detailed Deployment Steps

#### Step 1: Build and Start Containers
```bash
# Build and start all services in detached mode
docker-compose up -d --build

# Check container status
docker-compose ps
```

Expected output:
```
NAME                    IMAGE                 COMMAND                  SERVICE   CREATED         STATUS         PORTS
netsysportfolio-db-1    postgres:15           "docker-entrypoint.s…"   db        2 minutes ago   Up 2 minutes   0.0.0.0:5432->5432/tcp
netsysportfolio-web-1   netsysportfolio-web   "gunicorn --bind 0.0…"   web       2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp
```

#### Step 2: Initialize Database
```bash
# Run database initialization script
docker-compose exec web python populate_db.py
```

Expected output:
```
Creating database tables...
Clearing existing data...
Creating admin user...
Adding skills...
Adding experience...
Adding projects...
Adding testimonials...

Database populated successfully!

Admin credentials:
Username: admin
Password: admin123
```

#### Step 3: Verify Deployment
```bash
# Test the application
curl -I http://localhost:5000

# Check application logs
docker-compose logs web --tail=10
```

### Docker Services Overview

The `docker-compose.yml` includes:

**Web Service (`web`):**
- **Image**: Custom Flask application
- **Port**: 5000 (mapped to host)
- **Command**: Gunicorn with 4 workers
- **Dependencies**: Database service
- **Volumes**: Application code mounted for development

**Database Service (`db`):**
- **Image**: PostgreSQL 15
- **Port**: 5432 (mapped to host)
- **Database**: portfolio_db
- **User**: portfolio_user
- **Password**: portfolio_pass
- **Volumes**: Persistent data storage

## 🚀 Production Deployment

### Production Environment Setup

1. **Update Environment Variables:**
```bash
# In .env file
SESSION_SECRET=your-production-secret-key-32-chars-minimum
ADMIN_PASSWORD=your-production-admin-password
FLASK_ENV=production
FLASK_DEBUG=false
POPULATE_DEMO_DATA=false
```

2. **Deploy with Docker Compose:**
```bash
# Pull latest changes
git pull origin main

# Deploy production stack
docker-compose up -d --build

# Initialize database (first time only)
docker-compose exec web python populate_db.py
```

### Production Security Checklist

- [ ] **Strong SESSION_SECRET**: Use `python -c "import secrets; print(secrets.token_hex(32))"`
- [ ] **Secure ADMIN_PASSWORD**: Minimum 12 characters with complexity
- [ ] **FLASK_DEBUG=false**: Disable debug mode
- [ ] **FLASK_ENV=production**: Set production environment
- [ ] **POPULATE_DEMO_DATA=false**: Disable demo data in production
- [ ] **HTTPS Configuration**: Set up SSL/TLS certificates
- [ ] **Firewall Rules**: Restrict database port access
- [ ] **Regular Backups**: Implement automated database backups

### Reverse Proxy Setup (Nginx)

Create `/etc/nginx/sites-available/portfolio`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL Configuration
    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    
    # Security Headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    
    # Proxy Configuration
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $server_name;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Static files optimization
    location /static/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### SSL Certificate Setup (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal setup
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 💻 Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone and setup:**
```bash
git clone <your-repo-url>
cd NetSysPortfolio
cp env.template .env
# Edit .env with your settings
```

2. **Start development environment:**
```bash
docker-compose up -d
docker-compose exec web python populate_db.py
```

3. **Access application:**
- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/login

### Option 2: Native Python Development

1. **Install Python 3.11+**
2. **Install dependencies:**
```bash
# Using pip
pip install -r requirements.txt

# Or using UV (faster)
uv pip install -r requirements.txt
```

3. **Setup PostgreSQL:**
```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'portfolio_pass';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
\q
```

4. **Configure environment:**
```bash
cp env.template .env
# Edit .env with local database settings
```

5. **Run application:**
```bash
python app.py
```

## 📁 Project Structure

```
NetSysPortfolio/
├── app.py                     # Main Flask application
├── config.py                  # Configuration settings
├── models.py                  # Database models
├── forms.py                   # WTForms definitions
├── populate_db.py             # Database initialization
├── env.template               # Environment variables template
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Docker image configuration
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Project metadata
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── routes/
│   ├── __init__.py
│   ├── public.py              # Public routes (home, projects, contact)
│   └── admin.py               # Admin panel routes
├── templates/
│   ├── base.html              # Base template
│   ├── public/
│   │   ├── index.html         # Homepage
│   │   ├── projects.html      # Projects page
│   │   └── contact.html       # Contact page
│   ├── admin/
│   │   ├── base_admin.html    # Admin base template
│   │   ├── dashboard.html     # Admin dashboard
│   │   ├── login.html         # Admin login
│   │   ├── projects.html      # Project management
│   │   ├── project_form.html  # Add/edit project
│   │   ├── skills.html        # Skill management
│   │   ├── skill_form.html    # Add/edit skill
│   │   ├── experiences.html   # Experience management
│   │   ├── experience_form.html # Add/edit experience
│   │   ├── testimonials.html  # Testimonial management
│   │   ├── testimonial_form.html # Add/edit testimonial
│   │   └── messages.html      # Contact message inbox
│   └── errors/
│       ├── 404.html           # 404 error page
│       └── 500.html            # 500 error page
└── static/
    ├── css/
    │   └── style.css          # Custom styles
    └── js/
        └── main.js            # JavaScript
```

## 📊 Database Schema

### Tables Overview

**Users Table:**
- `id` (Primary Key)
- `username` (Unique)
- `password_hash`
- `created_at`

**Projects Table:**
- `id` (Primary Key)
- `title`
- `description`
- `image` (URL)
- `technologies` (Comma-separated)
- `link` (Project URL)
- `date_created`
- `order` (Display order)

**Skills Table:**
- `id` (Primary Key)
- `name`
- `category` (Networking, Systems, etc.)
- `proficiency` (0-100)
- `order` (Display order)

**Experiences Table:**
- `id` (Primary Key)
- `title`
- `company`
- `location`
- `start_date`
- `end_date` (NULL for current)
- `description`
- `order` (Display order)

**Testimonials Table:**
- `id` (Primary Key)
- `name`
- `role`
- `company`
- `message`
- `order` (Display order)

**ContactMessages Table:**
- `id` (Primary Key)
- `name`
- `email`
- `subject`
- `message`
- `is_read` (Boolean)
- `created_at`

## 🎨 Customization Guide

### Adding/Editing Content

#### Projects Management
1. Access admin panel: `http://yourdomain.com/admin/login`
2. Navigate to "Projects"
3. Click "Add Project"
4. Fill in details:
   - **Title**: Project name
   - **Description**: Detailed description
   - **Image URL**: Link to project image
   - **Technologies**: Comma-separated list
   - **Link**: Project URL (optional)
   - **Display Order**: Lower numbers appear first

#### Skills Management
1. Navigate to "Skills"
2. Add skills with:
   - **Name**: Skill name
   - **Category**: Choose from dropdown
   - **Proficiency**: 0-100 percentage
   - **Display Order**: Order within category

#### Experience Management
1. Navigate to "Experiences"
2. Add work history:
   - **Company**: Company name
   - **Title**: Job title
   - **Location**: City, State/Country
   - **Start/End Date**: Format "MMM YYYY"
   - **Description**: Achievements and responsibilities

### Theme Customization

#### Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #06b6d4;    /* Cyan */
    --secondary-color: #10b981;  /* Green */
    --background-dark: #0f172a;  /* Dark navy */
    --background-light: #1e293b; /* Lighter navy */
}
```

#### Fonts
Add custom fonts in `templates/base.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```

## 🔍 Troubleshooting

### Common Issues

#### Docker Issues

**Container won't start:**
```bash
# Check logs
docker-compose logs web
docker-compose logs db

# Restart containers
docker-compose restart

# Rebuild containers
docker-compose up --build
```

**Database connection errors:**
```bash
# Check database status
docker-compose exec db psql -U portfolio_user -d portfolio_db

# Reinitialize database
docker-compose exec web python populate_db.py
```

**Port already in use:**
```bash
# Find process using port 5000
netstat -tulpn | grep :5000

# Kill process (Linux/macOS)
sudo kill -9 $(lsof -ti:5000)

# Or change port in docker-compose.yml
```

#### Application Issues

**Admin login not working:**
- Verify admin user exists: Check database
- Reset password: Run `populate_db.py` again
- Check ADMIN_PASSWORD environment variable

**Styles not loading:**
- Check Tailwind CSS CDN accessibility
- Clear browser cache
- Verify static files are being served

**Database errors:**
- Check PostgreSQL is running
- Verify DATABASE_URL is correct
- Ensure database exists and user has permissions

### Log Analysis

**View application logs:**
```bash
# All logs
docker-compose logs

# Web service logs only
docker-compose logs web

# Follow logs in real-time
docker-compose logs -f web

# Last 50 lines
docker-compose logs --tail=50 web
```

**Common log patterns:**
- `Worker failed to boot`: Check app.py for syntax errors
- `relation "table" does not exist`: Run populate_db.py
- `duplicate key value`: Database already initialized

## 📈 Performance Optimization

### Production Optimizations

1. **Database Indexing:**
```sql
-- Add indexes for better performance
CREATE INDEX idx_projects_order ON projects("order");
CREATE INDEX idx_skills_category ON skills(category);
CREATE INDEX idx_experiences_order ON experiences("order");
```

2. **Static File Caching:**
```nginx
# In Nginx configuration
location /static/ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

3. **Gunicorn Configuration:**
```bash
# Adjust worker count based on CPU cores
gunicorn --bind 0.0.0.0:5000 --workers 4 --worker-class sync app:app
```

### Monitoring

**Health Check Endpoint:**
```bash
# Check application health
curl http://localhost:5000/

# Check database connectivity
docker-compose exec web python -c "from models import db; print('DB OK' if db.engine.execute('SELECT 1') else 'DB Error')"
```

## 🔄 Backup & Recovery

### Database Backup

**Create backup:**
```bash
# Backup database
docker-compose exec db pg_dump -U portfolio_user portfolio_db > backup_$(date +%Y%m%d_%H%M%S).sql

# Compress backup
gzip backup_*.sql
```

**Restore backup:**
```bash
# Stop application
docker-compose down

# Restore database
docker-compose up -d db
docker-compose exec -T db psql -U portfolio_user portfolio_db < backup_file.sql

# Restart application
docker-compose up -d
```

### Automated Backups

**Create backup script (`backup.sh`):**
```bash
#!/bin/bash
BACKUP_DIR="/path/to/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/portfolio_backup_$DATE.sql"

# Create backup
docker-compose exec -T db pg_dump -U portfolio_user portfolio_db > $BACKUP_FILE

# Compress backup
gzip $BACKUP_FILE

# Remove backups older than 30 days
find $BACKUP_DIR -name "portfolio_backup_*.sql.gz" -mtime +30 -delete

echo "Backup completed: $BACKUP_FILE.gz"
```

**Schedule backups (crontab):**
```bash
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * /path/to/backup.sh
```

## 📚 Additional Resources

### Documentation Links
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

### Security Resources
- [OWASP Flask Security](https://owasp.org/www-project-flask-security/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.3.x/security/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)

## 🤝 Contributing

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make changes and test locally**
4. **Commit changes:**
   ```bash
   git commit -m "Add: your feature description"
   ```
5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

### Code Standards

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Test all changes locally before submitting

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 💬 Support

### Getting Help

- **Issues**: Create a GitHub issue for bugs or feature requests
- **Documentation**: Check this README and inline code comments
- **Community**: Join discussions in GitHub Discussions

### Contact Information

- **Website**: [Your Portfolio URL]
- **Email**: [Your Email]
- **LinkedIn**: [Your LinkedIn Profile]

---

**Built with Flask and ❤️ for Network and System Engineers**

*Last updated: October 2025*