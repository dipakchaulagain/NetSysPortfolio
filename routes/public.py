from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import db, Project, Skill, Testimonial, ContactMessage, Experience
from forms import ContactForm

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    projects = Project.query.order_by(Project.order, Project.date_created.desc()).limit(6).all()
    skills = Skill.query.order_by(Skill.category, Skill.order).all()
    experiences = Experience.query.order_by(Experience.order, Experience.id.desc()).all()
    testimonials = Testimonial.query.order_by(Testimonial.order, Testimonial.date_created.desc()).all()
    
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
                         testimonials=testimonials)

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
