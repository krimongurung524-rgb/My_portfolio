// =========================================================
// MOBILE NAVIGATION
// =========================================================

const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", () => {

    navLinks.classList.toggle("active");

});


// Close mobile menu when clicking a link

const navItems = document.querySelectorAll(".nav-links a");

navItems.forEach((link) => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

    });

});


// =========================================================
// CONTACT FORM
// =========================================================

const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();

    const email = document.getElementById("email").value.trim();

    const message = document.getElementById("message").value.trim();


    if (name === "" || email === "" || message === "") {

        alert("Please fill in all the fields.");

        return;

    }


    alert(
        `Thank you, ${name}! Your message has been received.`
    );


    contactForm.reset();

});


// =========================================================
// NAVBAR SCROLL EFFECT
// =========================================================

const header = document.querySelector(".header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        header.style.background =
            "rgba(8, 17, 31, 0.95)";

    } else {

        header.style.background =
            "rgba(8, 17, 31, 0.82)";

    }

});


// =========================================================
// ACTIVE NAVIGATION
// =========================================================

const sections = document.querySelectorAll("section");

window.addEventListener("scroll", () => {

    let currentSection = "";

    sections.forEach((section) => {

        const sectionTop = section.offsetTop - 150;

        const sectionHeight = section.offsetHeight;

        if (
            window.scrollY >= sectionTop &&
            window.scrollY < sectionTop + sectionHeight
        ) {

            currentSection = section.getAttribute("id");

        }

    });


    navItems.forEach((link) => {

        link.classList.remove("active");

        if (
            link.getAttribute("href") ===
            `#${currentSection}`
        ) {

            link.classList.add("active");

        }

    });

});


// =========================================================
// SCROLL REVEAL ANIMATION
// =========================================================

const revealElements = document.querySelectorAll(
    ".section-title, .about-container, .education-card, .skill-card, .project-card, .contact-container"
);


const observer = new IntersectionObserver(
    (entries) => {

        entries.forEach((entry) => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

                observer.unobserve(entry.target);

            }

        });

    },
    {
        threshold: 0.12
    }
);


revealElements.forEach((element) => {

    element.classList.add("reveal");

    observer.observe(element);

});