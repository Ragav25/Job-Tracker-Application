// Add active class to the current button (highlight it)
var header = document.getElementsByClassName("checking")[0];
var btns = header.getElementsByClassName("btn")[0];
// for (var i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function() {
//   var current = document.getElementsByClassName("active");
//   current[0].className = current[0].className.replace(" active", "");
//   this.className += " active";
//   });
// }
(document).on('click', 'btns', function(){
  $(this).addClass('active')
  console.log("working..")
})
