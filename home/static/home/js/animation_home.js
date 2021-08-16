// Hero section animation taken from 
TweenMax.to(".home__primary", 2, {width: "100%", ease: Expo.easeInOut});
gsap.from('.home__title', {opacity: 0, duration: 2, delay: 1.5, y: 100});
gsap.from('.home__img img', {opacity: 0, duration: 2, delay:1.5, y: -100});
gsap.from('.btn__hero', {opacity: 0, duration: 2, delay:1.5, y: -100});
   
TweenMax.to(".home__secondary", 2.5, {width: "100%",ease: Expo.easeInOut});
gsap.from('.home__sub', {opacity: -1, duration: 1.5, delay: 1.5, x: 100});


// On scroll animation
const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
});

// Featured section.
sr.reveal('.featured-title', {delay: 200});
sr.reveal('.featured-card', {delay: 300});

// About section.
sr.reveal('.media-about', {delay: 200});
sr.reveal('.media-text', {delay: 400});
sr.reveal('.media-icon', {delay: 500, interval: 200});

// Security section.
sr.reveal('.security-icon', {delay: 200, interval: 200});
sr.reveal('.security-text', {delay: 400, interval: 200});