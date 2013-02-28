var httpRequest;

if (window.XMLHttpRequest) { // Mozilla, Safari, ...
	httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 8 and older
	httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
};

httpRequest.onreadystatechange = function() {
	
	var state = httpRequest.readyState;
	
	console.log(state);
	
	if (state == 4) {
		
		if(httpRequest.status == 200) {
			
			console.log('request ok!');
			
			var result = httpRequest.responseText;
			result = JSON.parse(result);				
			showComments(result);
			
		}
		
		if(httpRequest.status == 404) {
			
			console.log('not found');
			
		}
	}
	
};

var url = '/portfolio/project/2/comments/';


/* 
$.get(url, function(data, status) {
	console.log(data, status);
});
*/


var loadComments = function() {
	httpRequest.open('GET', url);
	httpRequest.send();
}


setInterval(function(){
	loadComments();
}, 5000);
loadComments();


var showComments = function(data) {

	var container = document.getElementById('comments_container');
	container.innerHTML = 'show comments...';
	
	for (i in data) {
		container.innerHTML += '<h5>' + data[i].username + '</h5>';
		container.innerHTML += '<p><small>' + data[i].text + '</small></p>';
	}
	
}






