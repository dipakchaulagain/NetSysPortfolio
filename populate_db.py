from app import create_app
from models import db, User, Project, Skill, Experience, Testimonial, SiteSettings, SocialLink
from werkzeug.security import generate_password_hash
import os

def populate_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables first
        print("Creating database tables...")
        db.create_all()
        
        # Check if demo data should be populated
        populate_demo = os.environ.get('POPULATE_DEMO_DATA', 'false').lower() in ('true', '1', 'yes')
        
        if populate_demo:
            print("Clearing existing data...")
            User.query.delete()
            Project.query.delete()
            Skill.query.delete()
            Experience.query.delete()
            Testimonial.query.delete()
            SocialLink.query.delete()
            db.session.commit()
        else:
            print("Skipping demo data population (POPULATE_DEMO_DATA=false)")
            # Only create admin user if it doesn't exist
            if User.query.filter_by(username='admin').first():
                print("Admin user already exists, skipping user creation.")
                return
        
        print("Creating admin user...")
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        admin = User(username='admin')
        admin.set_password(admin_password)
        db.session.add(admin)
        
        if populate_demo:
            print("Adding skills...")
            skills = [
                Skill(name='Cisco Networking', category='Networking', proficiency=95, order=1),
                Skill(name='Juniper Networks', category='Networking', proficiency=90, order=2),
                Skill(name='BGP/OSPF/EIGRP', category='Networking', proficiency=92, order=3),
                Skill(name='VPN/MPLS', category='Networking', proficiency=88, order=4),
                
                Skill(name='VMware vSphere', category='Virtualization', proficiency=93, order=1),
                Skill(name='Docker', category='Virtualization', proficiency=85, order=2),
                Skill(name='Kubernetes', category='Virtualization', proficiency=80, order=3),
                
                Skill(name='Linux (RHEL/Ubuntu)', category='Systems', proficiency=95, order=1),
                Skill(name='Windows Server', category='Systems', proficiency=88, order=2),
                Skill(name='Active Directory', category='Systems', proficiency=90, order=3),
                Skill(name='PowerShell', category='Systems', proficiency=85, order=4),
                
                Skill(name='AWS', category='Cloud Platforms', proficiency=87, order=1),
                Skill(name='Azure', category='Cloud Platforms', proficiency=83, order=2),
                Skill(name='Google Cloud Platform', category='Cloud Platforms', proficiency=78, order=3),
                
                Skill(name='Ansible', category='Automation', proficiency=90, order=1),
                Skill(name='Terraform', category='Automation', proficiency=85, order=2),
                Skill(name='Python', category='Automation', proficiency=88, order=3),
                Skill(name='Bash Scripting', category='Automation', proficiency=92, order=4),
                
                Skill(name='Firewall Management', category='Security', proficiency=90, order=1),
                Skill(name='IDS/IPS', category='Security', proficiency=85, order=2),
                Skill(name='SSL/TLS', category='Security', proficiency=88, order=3),
            ]
            db.session.bulk_save_objects(skills)
            
            print("Adding experience...")
            experiences = [
                Experience(
                    title='Senior Network Engineer',
                    company='TechCorp Solutions',
                    location='San Francisco, CA',
                    start_date='Jan 2020',
                    end_date='Present',
                    description='Leading network infrastructure projects for enterprise clients. Designed and implemented multi-site MPLS networks serving 5000+ users. Managed network security including firewall policies, VPN configurations, and IDS/IPS systems. Reduced network downtime by 40% through proactive monitoring and automation.',
                    order=1
                ),
                Experience(
                    title='Network & Systems Administrator',
                    company='Global Tech Services',
                    location='New York, NY',
                    start_date='Jun 2017',
                    end_date='Dec 2019',
                    description='Administered hybrid cloud infrastructure across AWS and on-premises data centers. Deployed and maintained VMware vSphere clusters hosting 200+ virtual machines. Implemented automated backup solutions reducing backup windows by 60%. Managed Windows and Linux servers supporting critical business applications.',
                    order=2
                ),
                Experience(
                    title='Junior Network Engineer',
                    company='DataNet Inc',
                    location='Austin, TX',
                    start_date='Aug 2015',
                    end_date='May 2017',
                    description='Configured and maintained Cisco routers and switches for enterprise network. Implemented network monitoring using SNMP and Syslog. Assisted with network troubleshooting and incident response. Documented network configurations and standard operating procedures.',
                    order=3
                ),
            ]
            db.session.bulk_save_objects(experiences)
            
            print("Adding projects...")
            projects = [
                Project(
                    title='Multi-Site MPLS Network Deployment',
                    description='Designed and deployed a comprehensive MPLS network solution connecting 15 branch offices across North America. Implemented QoS policies, redundant connections, and centralized management. Project resulted in 99.9% uptime and 35% reduction in WAN costs.',
                    image='https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800',
                    technologies='Cisco IOS, MPLS, BGP, OSPF, QoS',
                    link='',
                    order=1
                ),
                Project(
                    title='Enterprise Cloud Migration',
                    description='Led migration of on-premises infrastructure to AWS cloud for a Fortune 500 client. Migrated 150+ servers, implemented auto-scaling, and configured hybrid cloud connectivity. Achieved 40% cost reduction and improved application performance.',
                    image='https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800',
                    technologies='AWS EC2, VPC, Direct Connect, CloudFormation, Terraform',
                    link='',
                    order=2
                ),
                Project(
                    title='Network Security Hardening',
                    description='Conducted comprehensive security audit and implemented security improvements across enterprise network. Deployed next-gen firewalls, implemented network segmentation, and established security monitoring with SIEM integration.',
                    image='https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800',
                    technologies='Palo Alto Networks, Cisco ASA, Splunk, VPN, IDS/IPS',
                    link='',
                    order=3
                ),
                Project(
                    title='VMware Private Cloud Infrastructure',
                    description='Built a private cloud platform using VMware vSphere for a healthcare organization. Designed highly available architecture with automated failover, implemented storage tiering, and integrated backup solutions.',
                    image='https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800',
                    technologies='VMware vSphere, vCenter, vSAN, NSX, Veeam Backup',
                    link='',
                    order=4
                ),
                Project(
                    title='Network Automation Platform',
                    description='Developed Python-based network automation platform for configuration management and compliance checking. Automated routine tasks reducing manual effort by 70% and eliminated configuration errors.',
                    image='https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a?w=800',
                    technologies='Python, Ansible, Netmiko, Git, Jenkins',
                    link='',
                    order=5
                ),
                Project(
                    title='SD-WAN Implementation',
                    description='Deployed software-defined WAN solution replacing traditional MPLS circuits. Implemented intelligent traffic routing, improved application performance, and reduced WAN costs by 50%.',
                    image='https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=800',
                    technologies='Cisco SD-WAN, VeloCloud, IPsec, Application QoS',
                    link='',
                    order=6
                ),
            ]
            db.session.bulk_save_objects(projects)
            
            print("Adding testimonials...")
            testimonials = [
                Testimonial(
                    name='Sarah Johnson',
                    role='IT Director',
                    company='TechCorp Solutions',
                    message='Outstanding network engineer with deep expertise in both traditional and modern networking. Successfully led our multi-site MPLS deployment and cloud migration projects. Highly recommended!',
                    order=1
                ),
                Testimonial(
                    name='Michael Chen',
                    role='CTO',
                    company='Global Tech Services',
                    message='Excellent problem-solver with strong automation skills. Reduced our operational overhead significantly through smart automation and infrastructure optimization. A valuable asset to any team.',
                    order=2
                ),
                Testimonial(
                    name='Emily Rodriguez',
                    role='VP of Engineering',
                    company='DataNet Inc',
                    message='Reliable and knowledgeable engineer with great communication skills. Always willing to share knowledge and mentor junior team members. Would definitely work with again.',
                    order=3
                ),
            ]
            db.session.bulk_save_objects(testimonials)
            
            print("Adding social media links...")
            social_links = [
                SocialLink(platform='LinkedIn', url='https://linkedin.com/in/yourprofile', icon_class='fab fa-linkedin', order=1),
                SocialLink(platform='GitHub', url='https://github.com/yourprofile', icon_class='fab fa-github', order=2),
                SocialLink(platform='Twitter', url='https://twitter.com/yourprofile', icon_class='fab fa-twitter', order=3),
            ]
            db.session.bulk_save_objects(social_links)
        
        print("Setting up site settings...")
        existing_settings = SiteSettings.query.first()
        if not existing_settings:
            site_settings = SiteSettings(
                header_title='NetSysEng',
                page_title='Network & System Engineer',
                profile_name='John Anderson',
                position='Network & System Engineer',
                profile_image='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop',
                tagline='Building robust infrastructure | Optimizing networks | Securing systems',
                about_me='Experienced Network and System Engineer specializing in designing, implementing, and maintaining complex IT infrastructure. With expertise in network architecture, system administration, virtualization, and cloud technologies, I deliver scalable and secure solutions for enterprise environments.\n\nMy background includes extensive work with Cisco and Juniper networking equipment, VMware virtualization platforms, Linux and Windows Server environments, and various cloud platforms including AWS, Azure, and GCP.\n\nI\'m passionate about automation, security best practices, and staying current with emerging technologies in the infrastructure and networking space.',
                cv_filename='John_Anderson_CV.pdf'
            )
            db.session.add(site_settings)
        
        db.session.commit()
        print("\nDatabase populated successfully!")
        print("\nAdmin credentials:")
        print("Username: admin")
        print(f"Password: {admin_password}")

if __name__ == '__main__':
    populate_database()
