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

$(document).ready(function(){
	initRegionSelector();
});