// Toggle dropdown
const dropDownbtn = document.getElementById("dropDownbtn");
const myDropdown = document.getElementById("myDropdown");
const expandArrow1 = document.getElementById("expandArrow1");

if (dropDownbtn && myDropdown && expandArrow1) {
    dropDownbtn.addEventListener("click", () => {
        myDropdown.classList.toggle("show");
        expandArrow1.classList.toggle("rotate-180");
    });

    window.addEventListener("click", (e) => {
        if (!dropDownbtn.contains(e.target)) {
            myDropdown.classList.remove("show");
            expandArrow1.classList.remove("rotate-180");
        }
    });
}

// Toggle hamburger menu
const hamburger = document.getElementById("hamburger");
const nav = document.getElementById("nav");
const cutIcon = document.getElementById("cutIcon");
const menuIcon = document.getElementById("menuIcon");

if (hamburger && nav && cutIcon && menuIcon) {
    hamburger.addEventListener("click", () => {
        nav.classList.toggle("hidden");
        if (!nav.classList.contains("hidden")) {
            cutIcon.classList.remove("hidden");
            menuIcon.classList.add("hidden");
        } else {
            cutIcon.classList.add("hidden");
            menuIcon.classList.remove("hidden");
        }
    });
}

// Toggle sidebar navigation (if sidebar exists)
const sidebarNav = document.getElementById("sidebarNav");
const sidebarContent = document.getElementById("sidebarContent");
const expandArrow2 = document.getElementById("expandArrow2");

if (sidebarNav && sidebarContent && expandArrow2) {
    sidebarNav.addEventListener("click", () => {
        sidebarContent.classList.toggle("hidden");
        expandArrow2.classList.toggle("rotate-180");
    });
}

    


    
