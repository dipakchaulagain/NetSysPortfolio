document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.querySelector('.hamburger');
    const closeIcon = document.querySelector('.close');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            const isOpen = mobileMenu.classList.contains('active');
            
            if (isOpen) {
                // Close menu
                mobileMenu.classList.remove('active');
                setTimeout(() => {
                    mobileMenu.classList.add('hidden');
                }, 300);
            } else {
                // Open menu
                mobileMenu.classList.remove('hidden');
                setTimeout(() => {
                    mobileMenu.classList.add('active');
                }, 10);
            }
            
            hamburgerIcon.classList.toggle('hidden');
            closeIcon.classList.toggle('hidden');
        });
        
        // Close mobile menu when clicking a link
        const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                setTimeout(() => {
                    mobileMenu.classList.add('hidden');
                }, 300);
                hamburgerIcon.classList.remove('hidden');
                closeIcon.classList.add('hidden');
            });
        });
    }
    
    // Smooth Scroll for Navigation Links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Scroll Animation Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const scrollObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Observe all elements with scroll-fade class
    const scrollFadeElements = document.querySelectorAll('.scroll-fade');
    scrollFadeElements.forEach(element => {
        scrollObserver.observe(element);
    });
    
    // Flash Messages
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 500);
        }, 5000);
    });
    
    // Skill Bar Animation on Scroll
    const skillBars = document.querySelectorAll('.scroll-fade');
    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBars = entry.target.querySelectorAll('[style*="width"]');
                progressBars.forEach(bar => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.transition = 'width 1s ease-out';
                        bar.style.width = width;
                    }, 100);
                });
            }
        });
    }, observerOptions);
    
    skillBars.forEach(element => {
        skillObserver.observe(element);
    });
});
