from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
from models import db, Project, Skill, Testimonial, ContactMessage, Experience, SiteSettings, SocialLink
from forms import ContactForm
import os

public_bp = Blueprint('public', __name__)

def get_site_settings():
    settings = SiteSettings.query.first()
    if not settings:
        settings = SiteSettings()
        db.session.add(settings)
        db.session.commit()
    return settings

def get_social_links():
    return SocialLink.query.order_by(SocialLink.order).all()

@public_bp.route('/')
def index():
    projects = Project.query.order_by(Project.order, Project.date_created.desc()).limit(6).all()
    skills = Skill.query.order_by(Skill.category, Skill.order).all()
    experiences = Experience.query.order_by(Experience.order, Experience.id.desc()).all()
    testimonials = Testimonial.query.order_by(Testimonial.order, Testimonial.date_created.desc()).all()
    settings = get_site_settings()
    social_links = get_social_links()
    
    skills_by_category = {}
    for skill in skills:
        category = skill.category or 'Other'
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    return render_template('public/index.html', 
                         projects=projects, 
                         skills_by_category=skills_by_category,
                         experiences=experiences,
                         testimonials=testimonials,
                         settings=settings,
                         social_links=social_links)

@public_bp.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.order, Project.date_created.desc()).all()
    return render_template('public/projects.html', projects=all_projects)

@public_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Thank you! Your message has been received. I will get back to you soon.', 'success')
        return redirect(url_for('public.contact'))
    
    return render_template('public/contact.html', form=form)

@public_bp.route('/download-cv')
def download_cv():
    settings = get_site_settings()
    
    if not settings.cv_filename:
        flash('CV file not available for download.', 'info')
        return redirect(url_for('public.index'))
    
    upload_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads', 'documents')
    upload_path = os.path.join(upload_dir, settings.cv_filename)
    
    if os.path.exists(upload_path):
        return send_from_directory(upload_dir, settings.cv_filename, as_attachment=True)
    
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'documents')
    static_path = os.path.join(static_dir, settings.cv_filename)
    
    if os.path.exists(static_path):
        return send_from_directory(static_dir, settings.cv_filename, as_attachment=True)
    
    flash('CV file not found.', 'danger')
    return redirect(url_for('public.index'))
