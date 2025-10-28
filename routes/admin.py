from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse, urljoin
from werkzeug.utils import secure_filename
from models import db, User, Project, Skill, Testimonial, ContactMessage, Experience, SiteSettings, SocialLink
from forms import LoginForm, ProjectForm, SkillForm, TestimonialForm, ExperienceForm, SiteSettingsForm, SocialLinkForm
import os

admin_bp = Blueprint('admin', __name__)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page and is_safe_url(next_page):
                return redirect(next_page)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('admin/login.html', form=form)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('public.index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    project_count = Project.query.count()
    skill_count = Skill.query.count()
    testimonial_count = Testimonial.query.count()
    experience_count = Experience.query.count()
    message_count = ContactMessage.query.filter_by(status='unread').count()
    total_messages = ContactMessage.query.count()
    
    return render_template('admin/dashboard.html',
                         project_count=project_count,
                         skill_count=skill_count,
                         testimonial_count=testimonial_count,
                         experience_count=experience_count,
                         message_count=message_count,
                         total_messages=total_messages)

@admin_bp.route('/projects')
@login_required
def projects():
    all_projects = Project.query.order_by(Project.order, Project.date_created.desc()).all()
    return render_template('admin/projects.html', projects=all_projects)

@admin_bp.route('/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            image=form.image.data,
            technologies=form.technologies.data,
            link=form.link.data,
            order=form.order.data
        )
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('admin.projects'))
    
    return render_template('admin/project_form.html', form=form, title='Add Project')

@admin_bp.route('/projects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        project.image = form.image.data
        project.technologies = form.technologies.data
        project.link = form.link.data
        project.order = form.order.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin.projects'))
    
    return render_template('admin/project_form.html', form=form, title='Edit Project')

@admin_bp.route('/projects/delete/<int:id>', methods=['POST'])
@login_required
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin.projects'))

@admin_bp.route('/skills')
@login_required
def skills():
    all_skills = Skill.query.order_by(Skill.category, Skill.order).all()
    return render_template('admin/skills.html', skills=all_skills)

@admin_bp.route('/skills/add', methods=['GET', 'POST'])
@login_required
def add_skill():
    form = SkillForm()
    if form.validate_on_submit():
        skill = Skill(
            name=form.name.data,
            category=form.category.data,
            proficiency=form.proficiency.data,
            order=form.order.data
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('admin.skills'))
    
    return render_template('admin/skill_form.html', form=form, title='Add Skill')

@admin_bp.route('/skills/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_skill(id):
    skill = Skill.query.get_or_404(id)
    form = SkillForm(obj=skill)
    
    if form.validate_on_submit():
        skill.name = form.name.data
        skill.category = form.category.data
        skill.proficiency = form.proficiency.data
        skill.order = form.order.data
        db.session.commit()
        flash('Skill updated successfully!', 'success')
        return redirect(url_for('admin.skills'))
    
    return render_template('admin/skill_form.html', form=form, title='Edit Skill')

@admin_bp.route('/skills/delete/<int:id>', methods=['POST'])
@login_required
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted successfully!', 'success')
    return redirect(url_for('admin.skills'))

@admin_bp.route('/testimonials')
@login_required
def testimonials():
    all_testimonials = Testimonial.query.order_by(Testimonial.order, Testimonial.date_created.desc()).all()
    return render_template('admin/testimonials.html', testimonials=all_testimonials)

@admin_bp.route('/testimonials/add', methods=['GET', 'POST'])
@login_required
def add_testimonial():
    form = TestimonialForm()
    if form.validate_on_submit():
        testimonial = Testimonial(
            name=form.name.data,
            role=form.role.data,
            company=form.company.data,
            message=form.message.data,
            order=form.order.data
        )
        db.session.add(testimonial)
        db.session.commit()
        flash('Testimonial added successfully!', 'success')
        return redirect(url_for('admin.testimonials'))
    
    return render_template('admin/testimonial_form.html', form=form, title='Add Testimonial')

@admin_bp.route('/testimonials/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_testimonial(id):
    testimonial = Testimonial.query.get_or_404(id)
    form = TestimonialForm(obj=testimonial)
    
    if form.validate_on_submit():
        testimonial.name = form.name.data
        testimonial.role = form.role.data
        testimonial.company = form.company.data
        testimonial.message = form.message.data
        testimonial.order = form.order.data
        db.session.commit()
        flash('Testimonial updated successfully!', 'success')
        return redirect(url_for('admin.testimonials'))
    
    return render_template('admin/testimonial_form.html', form=form, title='Edit Testimonial')

@admin_bp.route('/testimonials/delete/<int:id>', methods=['POST'])
@login_required
def delete_testimonial(id):
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Testimonial deleted successfully!', 'success')
    return redirect(url_for('admin.testimonials'))

@admin_bp.route('/experiences')
@login_required
def experiences():
    all_experiences = Experience.query.order_by(Experience.order, Experience.id.desc()).all()
    return render_template('admin/experiences.html', experiences=all_experiences)

@admin_bp.route('/experiences/add', methods=['GET', 'POST'])
@login_required
def add_experience():
    form = ExperienceForm()
    if form.validate_on_submit():
        experience = Experience(
            title=form.title.data,
            company=form.company.data,
            location=form.location.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            description=form.description.data,
            order=form.order.data
        )
        db.session.add(experience)
        db.session.commit()
        flash('Experience added successfully!', 'success')
        return redirect(url_for('admin.experiences'))
    
    return render_template('admin/experience_form.html', form=form, title='Add Experience')

@admin_bp.route('/experiences/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_experience(id):
    experience = Experience.query.get_or_404(id)
    form = ExperienceForm(obj=experience)
    
    if form.validate_on_submit():
        experience.title = form.title.data
        experience.company = form.company.data
        experience.location = form.location.data
        experience.start_date = form.start_date.data
        experience.end_date = form.end_date.data
        experience.description = form.description.data
        experience.order = form.order.data
        db.session.commit()
        flash('Experience updated successfully!', 'success')
        return redirect(url_for('admin.experiences'))
    
    return render_template('admin/experience_form.html', form=form, title='Edit Experience')

@admin_bp.route('/experiences/delete/<int:id>', methods=['POST'])
@login_required
def delete_experience(id):
    experience = Experience.query.get_or_404(id)
    db.session.delete(experience)
    db.session.commit()
    flash('Experience deleted successfully!', 'success')
    return redirect(url_for('admin.experiences'))

@admin_bp.route('/messages')
@login_required
def messages():
    all_messages = ContactMessage.query.order_by(ContactMessage.date_received.desc()).all()
    return render_template('admin/messages.html', messages=all_messages)

@admin_bp.route('/messages/view/<int:id>')
@login_required
def view_message(id):
    message = ContactMessage.query.get_or_404(id)
    if message.status == 'unread':
        message.status = 'read'
        db.session.commit()
    return render_template('admin/message_view.html', message=message)

@admin_bp.route('/messages/delete/<int:id>', methods=['POST'])
@login_required
def delete_message(id):
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    flash('Message deleted successfully!', 'success')
    return redirect(url_for('admin.messages'))

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    site_settings = SiteSettings.query.first()
    if not site_settings:
        site_settings = SiteSettings()
        db.session.add(site_settings)
        db.session.commit()
    
    form = SiteSettingsForm()
    
    if form.validate_on_submit():
        site_settings.header_title = form.header_title.data
        site_settings.page_title = form.page_title.data
        site_settings.profile_name = form.profile_name.data
        site_settings.position = form.position.data
        site_settings.tagline = form.tagline.data
        site_settings.about_me = form.about_me.data
        
        if form.profile_image.data:
            image_file = form.profile_image.data
            filename = secure_filename(image_file.filename)
            timestamp = str(int(__import__('time').time()))
            filename = f"{timestamp}_{filename}"
            
            upload_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads', 'images')
            os.makedirs(upload_folder, exist_ok=True)
            
            filepath = os.path.join(upload_folder, filename)
            image_file.save(filepath)
            
            site_settings.profile_image = f"/static/uploads/images/{filename}"
        
        if form.cv_file.data:
            cv_file = form.cv_file.data
            filename = secure_filename(cv_file.filename)
            timestamp = str(int(__import__('time').time()))
            filename = f"{timestamp}_{filename}"
            
            upload_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads', 'documents')
            os.makedirs(upload_folder, exist_ok=True)
            
            filepath = os.path.join(upload_folder, filename)
            cv_file.save(filepath)
            
            site_settings.cv_filename = filename
        
        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('admin.settings'))
    
    form.header_title.data = site_settings.header_title
    form.page_title.data = site_settings.page_title
    form.profile_name.data = site_settings.profile_name
    form.position.data = site_settings.position
    form.current_image.data = site_settings.profile_image
    form.tagline.data = site_settings.tagline
    form.about_me.data = site_settings.about_me
    form.current_cv.data = site_settings.cv_filename
    
    social_links = SocialLink.query.order_by(SocialLink.order).all()
    return render_template('admin/settings.html', form=form, social_links=social_links, settings=site_settings)

@admin_bp.route('/social-links/add', methods=['GET', 'POST'])
@login_required
def add_social_link():
    form = SocialLinkForm()
    if form.validate_on_submit():
        social_link = SocialLink(
            platform=form.platform.data,
            url=form.url.data,
            icon_class=form.icon_class.data,
            order=form.order.data
        )
        db.session.add(social_link)
        db.session.commit()
        flash('Social link added successfully!', 'success')
        return redirect(url_for('admin.settings'))
    
    return render_template('admin/social_link_form.html', form=form, title='Add Social Link')

@admin_bp.route('/social-links/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_social_link(id):
    social_link = SocialLink.query.get_or_404(id)
    form = SocialLinkForm(obj=social_link)
    
    if form.validate_on_submit():
        social_link.platform = form.platform.data
        social_link.url = form.url.data
        social_link.icon_class = form.icon_class.data
        social_link.order = form.order.data
        db.session.commit()
        flash('Social link updated successfully!', 'success')
        return redirect(url_for('admin.settings'))
    
    return render_template('admin/social_link_form.html', form=form, title='Edit Social Link')

@admin_bp.route('/social-links/delete/<int:id>', methods=['POST'])
@login_required
def delete_social_link(id):
    social_link = SocialLink.query.get_or_404(id)
    db.session.delete(social_link)
    db.session.commit()
    flash('Social link deleted successfully!', 'success')
    return redirect(url_for('admin.settings'))
