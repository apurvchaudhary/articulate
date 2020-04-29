window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  }
  else {
    navbar.classList.remove("sticky");
  }
}
function openNav() {
  var element = document.getElementById("mySidepanel");
  element.style.width = "200px";
  element.style.borderTopRightRadius = "35px";
  element.style.borderBottomRightRadius = "35px";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
  } else {
  dropdownContent.style.display = "block";
  }
  });
}

var iframeCount = 1
function iframeFunction(embed_link) {
  var x = document.createElement("IFRAME");
  x.style.paddingLeft="20px";
  x.setAttribute("src", embed_link);
  x.setAttribute("height", "200");
  x.setAttribute("width", "315");
  x.setAttribute("frameborder", "0");
  x.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture");
  if (iframeCount == 1){
  document.body.appendChild(x);
  iframeCount++}
}

function myColorSelector(color) {
    if (color == 1){
  document.getElementById("box").style.backgroundColor = "#d1e0e0";}
    if (color == 2){
  document.getElementById("box").style.backgroundColor = "#ffffcc";}
    if (color == 3){
  document.getElementById("box").style.backgroundColor = "white";}
    if (color == 4){
  document.getElementById("box").style.backgroundColor = "#ccebff";}
}