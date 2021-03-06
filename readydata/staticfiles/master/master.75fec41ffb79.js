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
    $('#addrowbutton, #expand_btn').hide();
    $('#submitbutton').css('float', 'left');
  }
  else {
    $('#Upload').hide();
    $('#Lesson').hide();
    $("#tbl_tab").show();
    $('#tbl_tab').addClass('active');
    $('#lesson_tab').removeClass('active');
    $('#submitbutton').css('float', 'right');
    $('#addrowbutton, #expand_btn').show();
    $('#tbl_tab, #lesson_tab, #meta_tab').css("padding", "7px 50px").css("margin-left","50px");
    $('#table-navigation').css("padding-left", "0");
    $('#table-navigation').css("width", "75%");
    $('#table-navigation-right').css("width", "25%");
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
      $('#tableview, .dt-more-container').hide();
    });
    $('#tbl_tab').click(function() {
      $('#tableview, .dt-more-container').show();
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
  rowIndex = 0;
  var heightReset;
  $("#addrowbutton").on("click", function() {
      if($('.dataTables_scrollBody').height() < 420) {
        var heightReset = $('.dataTables_scrollBody').height() + 'px';
        $('.dataTables_scrollBody').css('max-height', heightReset);
      }
     $("#addRowSubmit").show();
     if($('#btn-example-load-more').is(':visible')){
       $(".dt-more-container").css("margin-left", "40%");
     }
     else {
       $(".dt-more-container").css("margin-left", "44.5%");
     }
     addedRowString = '<tr>';
     $("#myTable thead th").each(function(columnIndex) {
      columnid = $(this).attr('id');
      addedRowString += '<td><input type="text" class="form-control" form = "lesson-to-add" name = "' + columnid + ':' + rowIndex + "#" +columnIndex + '" placeholder="Enter value"/></td>'
     })
     addedRowString += '</tr>';
     addedRowStringLeft = '<tr><td></td><td><input type="text" form = "lesson-to-add" class="form-control" name = "version:' + rowIndex + '#0"" placeholder="Enter value"/></td><td><input type="text" form = "lesson-to-add" class="form-control" name = "grade:' + rowIndex + '#1"" placeholder="Enter value"/></td><td><input type="text" form = "lesson-to-add" class="form-control" name = "unit:' + rowIndex + '#2"" placeholder="Enter value"/></td><td><input type="text" form = "lesson-to-add" class="form-control" name = "lesson:' + rowIndex + '#3"" placeholder="Enter value"/></td></tr>'
     $('.dataTables_scroll tr:last').after(addedRowString);
     $('.DTFC_Cloned tr:last').after(addedRowStringLeft);
     rowIndex++;
     $('.dataTables_scrollBody').animate({
        scrollTop: $('.dataTables_scrollBody')[0].scrollHeight
        }, 'slow');
  })
});

//Create list of selected lessons to be used in confirmation
$(document).ready(function() {
  $('.lesson-column').on('click', function() {
    var versionToDupe = [];
    var gradeToDupe = [];
    var unitToDupe = [];
    var lessonToDupe = [];
    var vi = 0;
    var gi = 0;
    var ui = 0;
    var li = 0;
    $('.version-column input[type="radio"]:checked, .version-column input[type="checkbox"]:checked').each(function() {
      versionToDupe.push($(this).val());
    });
    $('.grade-column input[type="checkbox"]:checked').each(function() {
      gradeToDupe.push($(this).val());
    });
    $('.unit-column input[type="checkbox"]:checked').each(function() {
      unitToDupe.push($(this).val());
    });
    $('.sublesson-column input[type="checkbox"]:checked').each(function() {
      lessonToDupe.push($(this).val());
    });
    var lessonsDuplicating = [];
    var lessonToAdd;
    $(lessonToDupe).each(function() {
      ui = 0;
      $(unitToDupe).each(function() {
          gi = 0;
          $(gradeToDupe).each(function() {
              vi = 0;
              $(versionToDupe).each(function() {
                lessonToAdd = versionToDupe[vi] + "." + gradeToDupe[gi] + "." + unitToDupe[ui] + "." + lessonToDupe[li];
                lessonsDuplicating.push(lessonToAdd);
                vi++;
              });
              gi++;
          });
          ui++;
      });
      li++;
    });
    if(lessonsDuplicating.length === 0) {
      $('#selectedFullLessons').html("No Lessons Selected");
    }
    else {
    $('#selectedFullLessons').html(lessonsDuplicating.join(','));
    $('#selectedFullLessons').each(function(key, val) {
      var values = $(val).html().split(',');
      $(val).html('<ul>' + $.map(values, function(v) {
        return '<li>' + v + '</li>';
      }).join('') + '</ul>');
      });
    }
  });
});

// Make add new row button only appear when modify table is loaded

/* Edit row on same page as the table */
// $(document).ready(function() {
//   $('.edit').on('click', function() {
//     var rowNumber = $(this).parent().index();
//     addedRowString = '';
//     addedRowStringLeft = '<td></td>';
//     $("tbody tr").eq(rowNumber).find('td').each(function() {
//         addedRowString += '<td><input type="text" class="form-control" value="';
//         addedRowString += $(this).html();
//         addedRowString += '"/></td>'
//     });
//     $('.DTFC_Cloned tbody tr').eq(rowNumber).find('td:not(:first-child)').each(function() {
//         addedRowStringLeft += '<td><input type="text" class="form-control" value="';
//         addedRowStringLeft += $(this).html();
//         addedRowStringLeft += '"/></td>';
//     })
//     $('tbody tr').eq(rowNumber).html(addedRowString);
//     $('.DTFC_Cloned tbody tr').eq(rowNumber).html(addedRowStringLeft);
//   });
// });

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

    // $('#myTable tbody tr').filter(
    //   function(){
    //       return $(this).find('td').length - 5 == $(this).find('td').not('.id').filter(function(){
    //       	return $(this).text().trim() == '';
    //       }).length;
    //   }).remove();

  var columncount = $("#myTable thead th").not(".fixed-col").length;
  if(columncount < 7) {
    columncount = 7;
  }
  var myTableWidth = columncount*(100/7)+"vw";
  $("#myTable").width(myTableWidth);

if(document.location.pathname.indexOf("/table") == 0)
{
  var table = $('#myTable').DataTable({
      // pagingType: "full_numbers",
      autoWidth: false,
      orderCellsTop: true,
      scrollX : "500px",
      scrollY : "420px",
      scrollCollapse: true,
      deferRender: true,
      // paging: false,
      drawCallback: function(){
       // If there is some more data
       if($('#btn-example-load-more').is(':visible')){
          // Scroll to the "Load more" button
          $('html, body').animate({
             scrollTop: $('#btn-example-load-more').offset().top
          }, 1000);
       }
       // Show or hide "Load more" button based on whether there is more data available
       $('#btn-example-load-more').toggle(this.api().page.hasMore());
     },
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
    // Handle click on "Load more" button
    $('#btn-example-load-more').on('click', function(){
     // Load more data
     table.page.loadMore();
    });
    // var table_fixed_width = $('.dataTables_scrollHeadInner').width();
    // $('#myTable').width(table_fixed_width);
  }
  else if(document.location.pathname.indexOf("/modify") == 0)
  {
    var table = $('#myTable').DataTable({
        // pagingType: "full_numbers",
        autoWidth: false,
        orderCellsTop: true,
        scrollX : "500px",
        scrollY : "420px",
        scrollCollapse: true,
        deferRender: true,
        drawCallback: function(){
         // If there is some more data
         if($('#btn-example-load-more').is(':visible')){
            // Scroll to the "Load more" button
            $('html, body').animate({
               scrollTop: $('#btn-example-load-more').offset().top
            }, 1000);
         }
         // Show or hide "Load more" button based on whether there is more data available
         $('#btn-example-load-more').toggle(this.api().page.hasMore());
       }
        // pageLength: 50,
        // order: [[1, 'asc'], [2, 'asc'], [3, 'asc'], [4, 'asc']],
        // rowCallback: function (row, data, index) {
        //     if (data["DepthOfKnowledge"] === null) {
        //       $(row).remove();
        //     }
        // },
        //fixedHeader: true,
        // fixedColumns: {
        //   leftColumns: 5,
        //  }
      });
      // Handle click on "Load more" button
      $('#btn-example-load-more').on('click', function(){
        // Load more data
        table.page.loadMore();
      });
  }
  var lessonArray = [];
  $( table.table().container() ).on( 'keyup', 'thead input', function () {
  table
      .column( $(this).data('index') )
      .search( this.value )
      .draw();
      lessonArray = [];
      $('#myTable tbody tr').each(function() {
        lessonArray.push($(this).attr('name'));
      });
  });
  $('#expand_btn').on('click', function() {
      table.search('').columns().search('').draw();
      if($(this).html() == "Expand") {
        $(this).css("padding", "7px 15px").html("Unexpand");
        $('#myTable tbody tr, .DTFC_LeftBodyWrapper tbody tr').each(function(){
          if(lessonArray.includes($(this).attr('name'))) {
              $(this).show();
          }
          else {
              $(this).hide();
          }
        });
      }
      else {
        $(this).css("padding", "7px 25px").html("Expand");
        $('#myTable tbody tr, .DTFC_LeftBodyWrapper tbody tr').each(function() {
          $(this).show();
        })
      }
  });

    var headercounter = 0;
    $('table thead tr th:not(.fixed-col)').each(function() {
      var headertable = $(this).attr('id').replace(/[^A-Za-z]/g, '');
      var prevheadertable = $(this).prev().attr('id').replace(/[^A-Za-z]/g, '');
      if(headertable == prevheadertable) {
        var thclass = "same" + headercounter;
        $(this).addClass(thclass);
      }
      else {
        headercounter++;
        var thclass2 = "same" + headercounter;
        $(this).addClass(thclass2);
      }
    });
});

$(document).ready(function() {
  $(".version-container input").each(function() {
    if($(this).val() == "") {
      $(this).hide();
      $(this).parent().hide();
    }
  })
});

$(document).ready(function() {
  var table = $('#DuplicationTable').DataTable({
      // pagingType: "full_numbers",
      // autoWidth: false,
      orderCellsTop: true,
      // scrollX : "500px",
      scrollY : "420px",
      scrollCollapse: true,
      deferRender: true,
      // paging: false,
     //  drawCallback: function(){
     //   // If there is some more data
     //   if($('#btn-example-load-more').is(':visible')){
     //      // Scroll to the "Load more" button
     //      $('html, body').animate({
     //         scrollTop: $('#btn-example-load-more').offset().top
     //      }, 1000);
     //   }
     //   // Show or hide "Load more" button based on whether there is more data available
     //   $('#btn-example-load-more').toggle(this.api().page.hasMore());
     // },
      // order: [[1, 'asc'], [2, 'asc'], [3, 'asc'], [4, 'asc']]
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

// $(function() {
//   $("#duplicate_submit").submit(function( event ){
//     if ( $('#selectedVersions').html() != "No Version" && $('#selectedGrades').html() != "No Grades" && $('#selectedUnits').html() != "No Units" && $('#selectedLessons').html() != "No Lessons") {
//       if( confirm("Are you sure? Please verify your lesson selections & renamed version")) {
//         return;
//       }
//     }
//     else {
//     alert("Error: Please select at least one Version, Grade, Unit, and Lesson")
//     event.preventDefault();
//     }
//   });
// });

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

$('.version-column').click(function() {
	var features = [];
	$('.version-column input[type="checkbox"]:checked').each(function() {
		features.push($(this).val());
	});
  $('.version-column input[type="radio"]:checked').each(function() {
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
