import os
import getpass
from app import create_app
from models import db, User, Project, Skill, Testimonial

def init_database():
    app = create_app()
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        admin_password = os.environ.get('ADMIN_PASSWORD')
        if admin_password:
            if len(admin_password) < 8:
                print('ADMIN_PASSWORD must be at least 8 characters. Exiting.')
                return
        else:
            print('No ADMIN_PASSWORD environment variable found.')
            admin_password = getpass.getpass('Enter a strong admin password (min 8 characters): ')
            confirm_password = getpass.getpass('Confirm admin password: ')
            
            if admin_password != confirm_password:
                print('Passwords do not match. Exiting.')
                return
            
            if len(admin_password) < 8:
                print('Password must be at least 8 characters. Exiting.')
                return
        
        admin_user = User(username='admin')
        admin_user.set_password(admin_password)
        db.session.add(admin_user)
        
        projects = [
            Project(
                title='Enterprise Network Infrastructure Redesign',
                description='Led the complete redesign of a multi-site enterprise network infrastructure supporting 2000+ users. Implemented redundant core switches, VLANs segmentation, and optimized routing protocols (OSPF/BGP). Reduced network latency by 40% and improved overall reliability.',
                image='https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800',
                technologies='Cisco Catalyst 9000, OSPF, BGP, VLAN, STP, QoS',
                link='',
                order=1
            ),
            Project(
                title='VMware vSphere Cluster Deployment',
                description='Designed and deployed a highly available VMware vSphere 7.0 cluster with vSAN storage. Configured DRS, HA, and vMotion for optimal resource utilization. Migrated 150+ VMs from legacy infrastructure with zero downtime.',
                image='https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
                technologies='VMware vSphere 7.0, vSAN, vCenter, ESXi, PowerCLI',
                link='',
                order=2
            ),
            Project(
                title='Hybrid Cloud Migration - AWS',
                description='Orchestrated migration of on-premises workloads to AWS cloud infrastructure. Implemented VPC architecture, Direct Connect, and hybrid DNS solution. Achieved 30% cost reduction while improving scalability and disaster recovery capabilities.',
                image='https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800',
                technologies='AWS EC2, VPC, Direct Connect, Route53, CloudFormation, Terraform',
                link='',
                order=3
            ),
            Project(
                title='Network Security Hardening',
                description='Implemented comprehensive security measures including next-generation firewall deployment, IDS/IPS configuration, and network segmentation. Conducted vulnerability assessments and remediation, achieving 95% security score improvement.',
                image='https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800',
                technologies='Palo Alto Firewalls, Cisco ASA, Snort, Suricata, VPN, 802.1X',
                link='',
                order=4
            ),
            Project(
                title='Linux Server Automation Framework',
                description='Developed automated deployment and configuration management system for 200+ Linux servers using Ansible. Created custom playbooks for standardized server provisioning, patch management, and compliance monitoring.',
                image='https://images.unsplash.com/photo-1629654297299-c8506221ca97?w=800',
                technologies='Ansible, Python, Bash, RHEL, Ubuntu, Git, Jenkins',
                link='',
                order=5
            ),
            Project(
                title='SD-WAN Implementation',
                description='Deployed Software-Defined WAN solution across 25 branch offices, replacing traditional MPLS circuits. Improved application performance, reduced WAN costs by 50%, and enhanced network visibility with centralized management.',
                image='https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800',
                technologies='Cisco Viptela SD-WAN, IPsec, DMVPN, Application QoS',
                link='',
                order=6
            )
        ]
        
        for project in projects:
            db.session.add(project)
        
        skills = [
            Skill(name='Cisco IOS/IOS-XE', category='Networking', proficiency=95, order=1),
            Skill(name='Juniper JunOS', category='Networking', proficiency=85, order=2),
            Skill(name='BGP/OSPF Routing', category='Networking', proficiency=90, order=3),
            Skill(name='Network Security', category='Networking', proficiency=88, order=4),
            Skill(name='SD-WAN', category='Networking', proficiency=85, order=5),
            
            Skill(name='RHEL/CentOS', category='Systems', proficiency=92, order=6),
            Skill(name='Ubuntu/Debian', category='Systems', proficiency=90, order=7),
            Skill(name='Windows Server', category='Systems', proficiency=85, order=8),
            Skill(name='Active Directory', category='Systems', proficiency=87, order=9),
            Skill(name='PowerShell', category='Systems', proficiency=80, order=10),
            
            Skill(name='VMware vSphere', category='Virtualization', proficiency=92, order=11),
            Skill(name='Docker', category='Virtualization', proficiency=85, order=12),
            Skill(name='Kubernetes', category='Virtualization', proficiency=75, order=13),
            
            Skill(name='AWS', category='Cloud', proficiency=88, order=14),
            Skill(name='Azure', category='Cloud', proficiency=80, order=15),
            Skill(name='GCP', category='Cloud', proficiency=70, order=16),
            
            Skill(name='Ansible', category='Automation', proficiency=90, order=17),
            Skill(name='Terraform', category='Automation', proficiency=85, order=18),
            Skill(name='Python', category='Automation', proficiency=82, order=19),
            Skill(name='Bash Scripting', category='Automation', proficiency=88, order=20),
        ]
        
        for skill in skills:
            db.session.add(skill)
        
        testimonials = [
            Testimonial(
                name='Michael Chen',
                role='IT Director',
                company='TechCorp Solutions',
                message='Outstanding network engineer who transformed our aging infrastructure into a modern, highly available system. Their expertise in Cisco technologies and VMware virtualization was instrumental in our digital transformation. Delivered on time and under budget.',
                order=1
            ),
            Testimonial(
                name='Sarah Johnson',
                role='CTO',
                company='Global Finance Inc',
                message='Exceptional technical skills combined with excellent communication. Successfully migrated our critical systems to AWS cloud with zero downtime. Their thorough planning and risk mitigation strategies were impressive. Highly recommended!',
                order=2
            ),
            Testimonial(
                name='David Rodriguez',
                role='VP of Operations',
                company='Manufacturing Pro',
                message='Led the implementation of our SD-WAN project across 25 sites. Not only did they deliver technical excellence, but also provided valuable insights on cost optimization. Our WAN costs dropped by 50% while performance improved significantly.',
                order=3
            )
        ]
        
        for testimonial in testimonials:
            db.session.add(testimonial)
        
        db.session.commit()
        print('Database initialized successfully!')
        print('Admin credentials:')
        print('Username: admin')
        print('Password: (set securely)')

if __name__ == '__main__':
    init_database()
