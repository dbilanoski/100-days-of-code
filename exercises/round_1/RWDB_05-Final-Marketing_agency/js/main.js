/* Navbar toggle */
const toggleOpen = document.querySelector(".toggle");
const toggleClosed = document.querySelector(".toggle-close");
const navbar = document.querySelector(".nav-items");

toggleOpen.addEventListener("click", function() {
  navbar.classList.add("active");
 
  /* Listen for close event */
  toggleClosed.addEventListener("click", () => {
    navbar.classList.remove("active");
  })
})