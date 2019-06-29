function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

$(document).ready(function() {
  $('#submitbutton').click(function() {
          $("#tableview").show();
  });
  if($('#tableview').length == 0) {
    $('#Lesson').show();
  }
  else {
    $('#Lesson').hide();
    $("#tbl_tab").show();
    $('#tbl_tab').addClass('active');
    $('#lesson_tab').removeClass('active');
  }
});

var lastChecked = null;

$(document).ready(function() {
  var $chkboxes = $('.chkbox');
  $chkboxes.click(function(e) {
    if (!lastChecked) {
      lastChecked = this;
      return;
    }

    if (e.shiftKey) {
      var start = $chkboxes.index(this);
      var end = $chkboxes.index(lastChecked);

      $chkboxes.slice(Math.min(start, end), Math.max(start, end) + 1).prop('checked', this.checked);

    }

    lastChecked = this;
  });
});

// $(document).ready(function() {
//   var outerwidth = $('.lesson-prof-body').outerWidth()
//   var outerwidth2 = outerwidth/8.5*11;
//   $('.lesson-prof-body').height(outerwidth2);
//   $('#print_js').html(outerwidth2);
// });

$(document).ready(function() {
    $('#lesson_tab, #meta_tab').click(function() {
      $('#tableview').hide();
    });
    $('#tbl_tab').click(function() {
      $('#tableview').show();
      $('#tbl_tab').addClass('active');
    })
  });

$(document).ready(function () {

  if(document.location.pathname.indexOf("/duplicate") == 0) {
    $('#Home').removeClass('active');
    $('#Search').removeClass('active');
    $('#Create').addClass('active');
  }
  else if (document.location.pathname.indexOf("/table") == 0 || document.location.pathname.indexOf("/export") == 0 || document.location.pathname.indexOf("/Delete") == 0 || document.location.pathname.indexOf("/modify") == 0) {
    $('#Home').removeClass('active');
    $('#Create').removeClass('active');
    $('#Search').addClass('active');
  }
  else {
    $('#Home').addClass('active');
    $('#Search').removeClass('active');
    $('#Create').removeClass('active');
  }
});


/* Add new row to table */
$(document).ready(function(){
  $("#addrowbutton").on("click", function() {
     addedRowString = '<tr>';
     $("#myTable thead th").each(function() {
     addedRowString += '<td><input type="text" class="form-control"/></td>'
     })
     addedRowString += '</tr>';
     $('#myTable tr:last').after(addedRowString);
  })
});

/* Create dataTable and handle searching */
$(document).ready(function () {

  $('#myTable thead td').each( function (i) {
      var title = $('#myTable thead th').eq( $(this).index() ).text();
      if($(this).className == "fixed-col") {
        $(this).html( '<input type="text" class="fixed-col form-control" data-index="'+i+'" />' );
      }
      else {
        $(this).html( '<input type="text" class="form-control" placeholder="Search column" data-index="'+i+'" />' );
      }
    });

    $('#myTable tbody tr').filter(
      function(){
          return $(this).find('td').length - 5 == $(this).find('td').not('.id').filter(function(){
          	return $(this).text().trim() == '';
          }).length;
      }).remove();

  var columncount = $("#myTable thead th").not(".fixed-col").length;
  if(columncount < 7) {
    columncount = 7;
  }
  var myTableWidth = columncount*(100/7)+"vw";
  $("#myTable").width(myTableWidth);

if(document.location.pathname.indexOf("/table") == 0)
{
  var table = $('#myTable').DataTable({
      pagingType: "full_numbers",
      autoWidth: false,
      orderCellsTop: true,
      scrollX : "500px",
      scrollY : "420px",
      scrollCollapse: true,
      deferRender: true,
      pageLength: 50,
      // order: [[1, 'asc'], [2, 'asc'], [3, 'asc'], [4, 'asc']],
      // rowCallback: function (row, data, index) {
      //     if (data["DepthOfKnowledge"] === null) {
      //       $(row).remove();
      //     }
      // },
      //fixedHeader: true,
      fixedColumns: {
        leftColumns: 5,
      }
    });
    // $('#myTable').wrap('.dataTables_scroll');
    var table_fixed_width = $('.dataTables_scrollHeadInner').width();
    $('#myTable').width(table_fixed_width);
  }
  else if(document.location.pathname.indexOf("/modify") == 0)
  {
    var table = $('#myTable').DataTable({
        pagingType: "full_numbers",
        autoWidth: false,
        orderCellsTop: true,
        scrollX : "500px",
        scrollY : "420px",
        scrollCollapse: true,
        deferRender: true,
        pageLength: 50,
        // order: [[1, 'asc'], [2, 'asc'], [3, 'asc'], [4, 'asc']],
        // rowCallback: function (row, data, index) {
        //     if (data["DepthOfKnowledge"] === null) {
        //       $(row).remove();
        //     }
        // },
        //fixedHeader: true,
        // fixedColumns: {
        //   leftColumns: 5,
        // }
      });
  }

    $( table.table().container() ).on( 'keyup', 'thead input', function () {
    table
        .column( $(this).data('index') )
        .search( this.value )
        .draw();
    });
});

$(document).ready(function() {
  $('#TableEdit1_te input').each(function(e,i){
      if(this.value !== "") {
        $(this).parents('tr').addClass("editDelete");
      }
      else {
        $(this).parents('tr').addClass("add");
        $(this).attr("placeholder", "Add Value");
      }
      $(this).addClass("form-control");
      $(this).attr("ID", "detail-input")
  });
});

$(document).ready(function(){
  $(".search-meta, .search-meta-B").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".metadata-column").find("label[data-filter]").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  $("#search-grade").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".grade-column").find("label[data-filter]").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  $("#search-version").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".version-column").find("label[data-filter]").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  $("#search-unit").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".unit-column").find("label[data-filter]").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  $("#search-sublesson").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".sublesson-column").find("label[data-filter]").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function(){
  $("#selectall-Version, #selectall-Grade, #selectall-Unit, #selectall-Lesson").on("click", function() {
    var buttonClicked = $(this).attr('id').split('-')[1];
    $('input[name="'+buttonClicked+'"]').prop('checked', true);
    });
});

$(document).ready(function(){
  $("#unselectall-Version, #unselectall-Grade, #unselectall-Unit, #unselectall-Lesson").on("click", function() {
    var buttonClicked = $(this).attr('id').split('-')[1];
    $('input[name="'+buttonClicked+'"]').prop('checked', false);
    });
});



// $(document).ready(function(){
//   $("#search-unit").on("keyup", function() {
//     var value = $(this).val().toLowerCase();
//     $(".unit-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) > -1
//     }).slice(0,9).show();
//     $(".unit-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) > -1
//     }).slice(9).hide();
//     $(".unit-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) <= -1
//     }).hide()
//   });
// });
//
// $(document).ready(function(){
//   $("#search-sublesson").on("keyup", function() {
//     var value = $(this).val().toLowerCase();
//     $(".sublesson-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) > -1
//     }).slice(0,9).show();
//     $(".sublesson-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) > -1
//     }).slice(9).hide();
//     $(".sublesson-column").find("label[data-filter]").filter(function() {
//       return $(this).text().toLowerCase().indexOf(value) <= -1
//     }).hide();
//   });
// });

$(document).ready(function(){
  $(".faq").click(function() {
    $(this).toggleClass('expanded');
  });
});

$(function() {

$('.metadata-column').click(function() {
	var features = [];
  var featuresB = [];
	var text, i;
	$('#metadata-column-1 input[type="checkbox"]:checked, #metadata-column-1 input[type="radio"]:checked, #metadata-column-1a input[type="radio"]:checked').each(function() {
	features.push($(this).val());
	});
  $('#metadata-column-2 input[type="radio"]:checked, #metadata-column-2a input[type="radio"]:checked').each(function() {
	featuresB.push($(this).val());
	});
  // $('.metadata-column input[type="radio"]:checked').each(function() {
  // features.push($(this).val());
  // });
	if (features.length === 0) {
		$('#selectedMeta, #selectedMetaB').html("No Metadata Selected");
		// $('#selectedMetaB').html("No Metadata Selected");
    $('#submitbutton, #submitButtonB').removeClass("buttonReady");
    // $('#submitbuttonB').removeClass("buttonReady");
	}
	else {
  $('#submitbutton, #submitbuttonB').addClass("buttonReady");
  // $('#submitbuttonB').addClass("buttonReady");
	$('#selectedMeta, #selectedMetaB').html(features.join(','));
	// $('#selectedMetaB').html(features.join(','));
	$('#selectedMeta, #selectedMetaB').each(function(key, val) {
		var values = $(val).html().split(',');
		$(val).html('<ul>' + $.map(values, function(v) {
			return '<li>' + v + '</li>';
		}).join('') + '</ul>');
		});

	// $('#selectedMetaB').each(function(key, val) {
	// 		var values = $(val).html().split(',');
	// 		$(val).html('<ul>' + $.map(values, function(v) {
	// 			return '<li>' + v + '</li>';
	// 		}).join('') + '</ul>');
	// 		});
	}
  if (featuresB.length === 0) {
    $('#selectedMetaC').html("No Metadata Selected");
    $('.view-table').removeClass("buttonReady");
  }
  else {
    $('.view-table').addClass("buttonReady");
  	$('#selectedMetaC').html(featuresB.join(','));
  	// $('#selectedMetaB').html(features.join(','));
  	$('#selectedMetaC').each(function(key, val) {
  		var values = $(val).html().split(',');
  		$(val).html('<ul>' + $.map(values, function(v) {
  			return '<li>' + v + '</li>';
  		}).join('') + '</ul>');
  		});
  }
}).trigger('click');
});

$(function() {
  $("#duplicate_submit").submit(function( event ){
    if ( $('#selectedVersions').html() != "No Version" && $('#selectedGrades').html() != "No Grades" && $('#selectedUnits').html() != "No Units" && $('#selectedLessons').html() != "No Lessons") {
      if( confirm("Are you sure? Please verify your lesson selections & renamed version")) {
        return;
      }
    }
    else {
    alert("Error: Please select at least one Version, Grade, Unit, and Lesson")
    event.preventDefault();
    }
  });
});

$(function() {
  $("#delete_submit").submit(function( event ){
    if ( $('#selectedVersions').html() != "No Version" && $('#selectedGrades').html() != "No Grades" && $('#selectedUnits').html() != "No Units" && $('#selectedLessons').html() != "No Lessons") {
      if( confirm("Are you sure? Please verify your lesson selections")) {
        return;
      }
    }
    else {
    alert("Error: Please select at least one Version, Grade, Unit, and Lesson")
    event.preventDefault();
    }
  });
});

$(function() {
  $("#export_submit").submit(function( event ){
    if ( $('#selectedMeta').html() != "No Metadata Selected") {
        return;
    }
    else {
    alert("Error: Please select metadata to be exported")
    event.preventDefault();
    }
  });
});

$(function() {
  $("#table_submit").submit(function( event ){
    if ( $('#selectedMeta').html() != "No Metadata Selected") {
        return;
    }
    else {
    alert("Error: Please select metadata to be searched")
    event.preventDefault();
    }
  });
});

$(function() {
  $("#upload_submit").submit(function( event ){
    if ( $('#selectedMeta').html() != "No Metadata Selected") {
        return;
    }
    else {
    alert("Error: Please select bubble of metadata to be uploaded")
    event.preventDefault();
    }
  });
});

$(function() {

$('.lesson-column-1').click(function() {
	var features = [];
	$('.lesson-column-1 input[type="checkbox"]:checked').each(function() {
		features.push($(this).val());
	});
  $('.lesson-column-1 input[type="radio"]:checked').each(function() {
		features.push($(this).val());
	});
	if (features.length === 0 && (document.location.pathname.indexOf("/duplicate") == 0 || document.location.pathname.indexOf("/Delete") == 0)) {
     $('#selectedVersions').html("No Version");
    }
  else if (features.length === 0) {
	 	$('#selectedVersions').html("All Versions");
	 	$('#selectedVersionsB').html("All Versions");
  }
	else {
	$('#selectedVersions, #selectedVersionsB').html(features.join(','));
	$('#selectedVersions').each(function(key, val) {
		var values = $(val).html().split(',');
		$(val).html('<ul>' + $.map(values, function(v) {
			return '<li>' + v + '</li>';
		}).join('') + '</ul>');
		});
	// $('#selectedVersionsB').html(features.join(','));
	if (document.location.pathname.indexOf("/duplicate") !== 0) {
    $('#selectedVersionsB').each(function(key, val) {
			var values = $(val).html().split(',');
			$(val).html('<ul>' + $.map(values, function(v) {
				return '<li>' + v + '</li>';
			}).join('') + '</ul>');
			});
    }
	}
}).trigger('click');
	});

	$(function() {
	$('.grade-column').click(function() {
		var features = [];
		$('.grade-column input[type="checkbox"]:checked').each(function() {
			features.push($(this).val());
		});
		if (features.length === 0 && (document.location.pathname.indexOf("/duplicate") == 0 || document.location.pathname.indexOf("/Delete") == 0)) {
      $('#selectedGrades').html("No Grades");
    }
    else if (features.length === 0) {
			$('#selectedGrades').html("All Grades");
			$('#selectedGradesB').html("All Grades");
		}
		else {
		$('#selectedGrades, #selectedGradesB').html(features.join(','));
		$('#selectedGrades, #selectedGradesB').each(function(key, val) {
			var values = $(val).html().split(',');
			$(val).html('<ul>' + $.map(values, function(v) {
				return '<li>' + v + '</li>';
			}).join('') + '</ul>');
			});
		}
  }).trigger('click');
		});

	$(function() {
		$('.unit-column').click(function() {
			var features = [];
			$('.unit-column input[type="checkbox"]:checked').each(function() {
				features.push($(this).val());
			});
			if (features.length === 0 && (document.location.pathname.indexOf("/duplicate") == 0 || document.location.pathname.indexOf("/Delete") == 0)) {
        $('#selectedUnits').html("No Units");
      }
      else if (features.length === 0) {
				$('#selectedUnits, #selectedUnitsB').html("All Units");
			}
			else {
			$('#selectedUnits, #selectedUnitsB').html(features.join(','));
			$('#selectedUnits, #selectedUnitsB').each(function(key, val) {
				var values = $(val).html().split(',');
				$(val).html('<ul>' + $.map(values, function(v) {
					return '<li>' + v + '</li>';
				}).join('') + '</ul>');
				});
			}
			}).trigger('click');
			});

	$(function() {
			$('.sublesson-column').click(function() {
				var features = [];
				$('.sublesson-column input[type="checkbox"]:checked').each(function() {
					features.push($(this).val());
				});
				if (features.length === 0 && (document.location.pathname.indexOf("/duplicate") == 0 || document.location.pathname.indexOf("/Delete") == 0)) {
          $('#selectedLessons').html("No Lessons");
        }
        else if (features.length === 0) {
					$('#selectedLessons, #selectedLessonsB').html("All Lessons");
				}
				else {
				$('#selectedLessons, #selectedLessonsB').html(features.join(','));
				$('#selectedLessons, #selectedLessonsB').each(function(key, val) {
					var values = $(val).html().split(',');
					$(val).html('<ul>' + $.map(values, function(v) {
						return '<li>' + v + '</li>';
					}).join('') + '</ul>');
					});
				}
				}).trigger('click');
				});
