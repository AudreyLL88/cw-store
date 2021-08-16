// On scroll animation of review form.
const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
});
sr.reveal('.review-header', {delay: 400});
sr.reveal('.review-form', {delay: 600, interval: 200});