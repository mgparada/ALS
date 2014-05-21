function validate() {
	if (isEmptyForm()) {
		alert("that form is empty motherfucker");
		return false;
	} else {
		return true;
	}
}

function isEmptyForm() {
	var x = document.getElementById("frmInput");

	for ( i = 0; i < x.length; i++) {
		if ( x.elements[i].value == 'undefined' ) {
			return true;
		}
	}	
	return false;
	// var km = x['km'].value();
}