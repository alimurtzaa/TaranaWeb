    //toggle dropdown
    const dropDownbtn = document.getElementById("dropDownbtn");
    const myDropdown = document.getElementById("myDropdown");
    const expandArrow1 = document.getElementById("expandArrow1");

    dropDownbtn.addEventListener("click", () => {
        myDropdown.classList.toggle("show");
        expandArrow1.classList.toggle('rotate-180');
    });

    window.addEventListener("click",(e)=>{
        if(!dropDownbtn.contains(e.target) && !dropDownbtn.contains(e.target) ){
            myDropdown.classList.remove("show");
            expandArrow1.classList.remove('rotate-180');
        }
    });

    // toggle hamburger
    const hamburger = document.getElementById("hamburger")
    const nav = document.getElementById("nav")
    const cutIcon = document.getElementById("cutIcon")
    const menuIcon = document.getElementById("menuIcon")

    hamburger.addEventListener("click", () => {
        nav.classList.toggle("hidden")
        if(!nav.classList.contains("hidden")){
            cutIcon.classList.remove("hidden")
            menuIcon.classList.add("hidden")
        } else {
            cutIcon.classList.add('hidden'); 
            menuIcon.classList.remove("hidden")
        }
        });

    // toggle sidebar nav
    const sidebarNav = document.getElementById("sidebarNav");
    const sidebarContent = document.getElementById("sidebarContent")
    const expandArrow2 = document.getElementById("expandArrow2")
    sidebarNav.addEventListener("click",()=>{
        sidebarContent.classList.toggle("hidden");
        expandArrow2.classList.toggle('rotate-180');
    })
    


    
// Add event listener for both click and touchstart, ensuring no double execution
// function addClickOrTouchEvent(element, callback) {
//     let isTouchDevice = false;

//     element.addEventListener("touchstart", (event) => {
//         isTouchDevice = true; // Set flag for touch device
//         callback(event);
//     });

//     element.addEventListener("click", (event) => {
//         if (!isTouchDevice) { // Prevent double firing
//             callback(event);
//         }
//     });
// }

// // Toggle sidebar nav
// const sidebarNav = document.getElementById("sidebarNav");
// const sidebarContent = document.getElementById("sidebarContent");
// const expandArrow2 = document.getElementById("expandArrow2");

// addClickOrTouchEvent(sidebarNav, (event) => {
//     event.preventDefault(); // Prevent default behavior
//     sidebarContent.classList.toggle("hidden");
//     expandArrow2.classList.toggle("rotate-180");
// });

// // Ensure dropdown works on mobile
// const dropDownbtn = document.getElementById("dropDownbtn");
// const myDropdown = document.getElementById("myDropdown");
// const expandArrow1 = document.getElementById("expandArrow1");

// addClickOrTouchEvent(dropDownbtn, (event) => {
//     event.preventDefault(); // Prevent default behavior
//     myDropdown.classList.toggle("show");
//     expandArrow1.classList.toggle("rotate-180");
// });

// // Ensure hamburger menu works on mobile
// const hamburger = document.getElementById("hamburger");
// const nav = document.getElementById("nav");
// const cutIcon = document.getElementById("cutIcon");
// const menuIcon = document.getElementById("menuIcon");

// addClickOrTouchEvent(hamburger, (event) => {
//     event.preventDefault(); // Prevent default behavior
//     nav.classList.toggle("hidden");
//     if (!nav.classList.contains("hidden")) {
//         cutIcon.classList.remove("hidden");
//         menuIcon.classList.add("hidden");
//     } else {
//         cutIcon.classList.add("hidden");
//         menuIcon.classList.remove("hidden");
//     }
// });


