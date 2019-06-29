/* Functionality for check all button */

/* Create dataTable and handle searching */
$(document).ready(function () {

  var dataTableInstance = $('#myTable').DataTable({
      "searching": true,
      "sort": false,
      "paging": false,
  });
    
  $('#myTable thead th').not('#checkbox').each(function () {
    $(this).append('<input class="filter" type="text" placeholder="search">');
  });
  
  

  dataTableInstance.columns().every(function (item, index, arr){
    
    var datatableColumn = this;
   
	  
    $(this.header()).find('input:text').on('keyup change', function () {
      datatableColumn.search(this.value).draw();
    });
    

  });
	
 
$('.selectall').click(function() {
  if ($(this).is(':checked')) {
    $('input:checkbox:visible').prop('checked', true);
  } else {
  $('input:checkbox:visible').prop('checked', false);
  }
});





$('.proghide').click(function() {

  if($('.prog').is(":visible")){
    $('.prog').hide()
  }
  else{
      $('.prog').show()
  }
});
$('.toolhide').click(function() {

  if($('.tool').is(":visible")){
    $('.tool').hide()
  }
  else{
      $('.tool').show()
  }
});
$('.enrichhide').click(function() {
  if($('.ea').is(":visible")){
    $('.ea').hide()
  }
  else{
      $('.ea').show()
  }
});
$('.lessonhide').click(function() {
  if($('.lesson').is(":visible")){
    $('.lesson').hide()
  }
  else{
      $('.lesson').show()
  }
});


});
