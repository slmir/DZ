$(function(){
  $("#toggleP").on("click",function() {
    $("#hidethis").toggle(!this.checked);
  });
});