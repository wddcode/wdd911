var httpRequest;

if (window.XMLHttpRequest) { // Mozilla, Safari, ...
	httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 8 and older
	httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
};

httpRequest.onreadystatechange = function() {
	
	var state = httpRequest.readyState;

	if(state == 4) {
		
		if (httpRequest.status === 200) {
		
			var result = httpRequest.responseText;		
			// var result = JSON.parse(result);
			
		} else {
			alert('error: ' + httpRequest.status);
		}
		
	}
	
};

var url = 'the url!';
// httpRequest.open('GET', url);
// httpRequest.send();
