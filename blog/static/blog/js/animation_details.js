gsap.from(".blog-title", { opacity: 0, duration: 1, delay: 1.5, x: -100 });
gsap.from(".blog-author", { opacity: 0, duration: 1, delay: 2.5, y: -50 });
gsap.from(".blog-date", { opacity: 0, duration: 1, delay: 3, x: -100 });
gsap.from(".blog-crud", { opacity: 0, duration: 1, delay: 3.5, x: -100 });
gsap.from(".blog-img", { opacity: 0, duration: 1, delay: 3, x: 100 });
gsap.from(".blog-content", { opacity: 0, duration: 1, delay: 3.5, y: 50 });

const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

sr.reveal('.comment-header', {delay: 200})
sr.reveal('.comment-total', {delay: 300})
sr.reveal('.comment-average', {delay: 400})
sr.reveal('.comment-btn-up', {delay: 500})
sr.reveal('.comment-title-detail', {delay: 200})
sr.reveal('.comment-detail', {delay: 400})