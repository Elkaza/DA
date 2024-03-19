// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Collapsible Sections
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("main section h2").forEach(section => {
        section.addEventListener("click", function() {
            var content = this.nextElementSibling;
            content.style.display = content.style.display === "none" ? "block" : "none";
        });
    });
});
