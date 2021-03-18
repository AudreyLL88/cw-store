gsap.from(".item-img", { opacity: 0, duration: 1, delay: 1.5, x: -100 });
gsap.from(".item-info", { opacity: 0, duration: 1, delay: 2.5, y: -50 });
gsap.from(".size", { opacity: 0, duration: 1, delay: 3, x: -100 });
gsap.from(".quantity", { opacity: 0, duration: 1, delay: 3, x: 100 });
gsap.from(".price-title", { opacity: 0, duration: 1, delay: 3.5, y: 50 });
gsap.from(".price-button", { opacity: 0, duration: 1, delay: 3.5, y: -50 });

const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

/*SCROLL Review*/
sr.reveal('.review-header', {delay: 200})
sr.reveal('.review-total', {delay: 300})
sr.reveal('.review-average', {delay: 400})
sr.reveal('.review-btn-up', {delay: 500})
sr.reveal('.review-title-detail', {delay: 200})
sr.reveal('.review-detail', {delay: 400})