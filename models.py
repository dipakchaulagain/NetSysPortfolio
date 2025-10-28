from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    technologies = db.Column(db.String(500))
    link = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Project {self.title}>'

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    proficiency = db.Column(db.Integer, default=50)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Skill {self.name}>'

class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(150))
    company = db.Column(db.String(150))
    message = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Testimonial from {self.name}>'

class Experience(db.Model):
    __tablename__ = 'experiences'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Experience {self.title} at {self.company}>'

class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_received = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='unread')
    
    def __repr__(self):
        return f'<ContactMessage from {self.name}>'

class SiteSettings(db.Model):
    __tablename__ = 'site_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    header_title = db.Column(db.String(100), default='NetSysEng')
    page_title = db.Column(db.String(100), default='Network & System Engineer')
    profile_name = db.Column(db.String(100), default='John Anderson')
    position = db.Column(db.String(200), default='Network & System Engineer')
    profile_image = db.Column(db.String(500), default='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop')
    tagline = db.Column(db.String(200), default='Building robust infrastructure | Optimizing networks | Securing systems')
    about_me = db.Column(db.Text, default='Experienced Network and System Engineer specializing in designing, implementing, and maintaining complex IT infrastructure. With expertise in network architecture, system administration, virtualization, and cloud technologies, I deliver scalable and secure solutions for enterprise environments.')
    cv_filename = db.Column(db.String(255), default='John_Anderson_CV.pdf')
    
    def __repr__(self):
        return f'<SiteSettings {self.profile_name}>'

class SocialLink(db.Model):
    __tablename__ = 'social_links'
    
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    icon_class = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<SocialLink {self.platform}>'
