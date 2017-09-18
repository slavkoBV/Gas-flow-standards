function initRegionSelector() {
	// look up select element with regions and attach our even handler
	// on field "change" event
	$('#region-selector select').change(function(event){
		// get value of currently selected region option
		var regionSel = $(this).val();

		if (regionSel) {
			// set cookie with expiration date 1 year since now;
			// cookie creation function takes period in days
			$.cookie('current_region', regionSel, {'path': '/', 'expires': 365});
		} else {
			// otherwise we delete the cookie
			$.removeCookie('current_region', {'path': '/'});
		}

		// and reload a page
		location.reload(true);
		return true;
	});
}

function initFlowstandPage() {
	$('a.flowstand_show-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				if (status != 'success'){
					alert('Server error. Please try later.');
					return false;
				}
				var modal = $('#myModal');
				html = $(data), table = html.find('.content table');
				modal.find('.modal-title').html(html.find('.title h2').text());
				modal.find('.modal-body').html(table);
				modal.modal({
				    'backdrop': false,
				    'show': true
				});
			},
			'error': function(){
				alert('Server error. try later');
				return false;
			}
		});
		return false;
	});
}

function scrollUp(){
	$('#scrollup img').mouseover( function(){
		$( this ).animate({opacity: 0.65},100);
	}).mouseout( function(){
		$( this ).animate({opacity: 1},100);
	}).click(function(){
		$('html').animate({ scrollTop: 0 }, 700);
		return false;
       });

	$(window).scroll(function(){
		if ( $(document).scrollTop() > 0 ) {
			$('#scrollup').fadeIn('fast');
		} else {
			$('#scrollup').fadeOut('fast');
		}
	});
}


$(document).ready(function(){
	scrollUp();
	initRegionSelector();
	initFlowstandPage();
});