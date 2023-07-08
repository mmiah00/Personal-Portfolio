// let welcome = document.getElementById('welcome'); 
// let scrolldown = document.getElementById('scrolldown'); 
// let buildings = document.getElementById('buildings'); 
// let leaf = document.getElementById('leaf'); 
// let hill1 = document.getElementById('hill1'); 
// let hill4 = document.getElementById('hill4'); 
// let hill5 = document.getElementById('hill5'); 

// window.addEventListener('scroll', () => { 
//     let value = window.scrollY; 

//     // welcome.style.marginTop = value * 2.5  + 'px'; // makes title move down until it is gone behind the bottom hills 
//     scrolldown.style.marginTop = value * 2.5 + 'px'; 
//     buildings.style.marginTop = value * 1.5 + 'px'; 

//     leaf.style.top = value * -1.5 + 'px'; 
//     leaf.style.left = value * 1.5 + 'px'; //lines 11 and 12 together make the leaf in the top right corner move diagonally northeast
//     hill5.style.left = value * 1.5 + 'px'; // makes hill on the right side move right until it is out of the screen
//     hill4.style.left = value * -1.5 + 'px'; // makes hill on the left side move left until out of the screen 
//     hill1.style.top = value * -1.5 + 'px'; // makes hills on top go down as text moves down 
// }); 

let welcome = document.getElementById('welcome');
let scrolldown = document.getElementById('scrolldown');
let buildings = document.getElementById('buildings');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');
let backgroundSection = document.querySelector('.background');

window.addEventListener('scroll', () => {
  let sectionOffsetTop = backgroundSection.offsetTop; // Top offset of the background section
  let sectionHeight = backgroundSection.offsetHeight; // Height of the background section
  let windowHeight = window.innerHeight; // Height of the viewport
  let scrollPosition = window.scrollY;

  let sectionEndPosition = sectionOffsetTop + sectionHeight;
  let maxScroll = sectionEndPosition - windowHeight;

  let scrollPercentage = scrollPosition / maxScroll;

  scrollPercentage = Math.max(0, Math.min(scrollPercentage, 1)); // Limit scrollPercentage between 0 and 1

//   welcome.style.marginTop = scrollPercentage * (windowHeight / 2) + 'px';
  scrolldown.style.marginTop = scrollPercentage * (windowHeight / 2) + 'px';
  buildings.style.marginTop = scrollPercentage * (windowHeight / 3) + 'px';
  leaf.style.top = scrollPercentage * (windowHeight / -2) + 'px';
  leaf.style.left = scrollPercentage * (windowHeight / 2) + 'px';
  hill5.style.left = scrollPercentage * (windowHeight / 2) + 'px';
  hill4.style.left = scrollPercentage * (windowHeight / -2) + 'px';
  hill1.style.top = scrollPercentage * (windowHeight / -2) + 'px';
});

