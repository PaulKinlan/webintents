var shortUrl;

// TODO(scr) remove this when done debugging.
var printFocus = function() {
    var focused = document.querySelectorAll(':focus');
    console.log(focused);
};

var fetchData = function() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4 && xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);
            var resDiv = document.getElementById("result");
            var shortDiv = document.getElementById("short");
            var longDiv = document.getElementById("long");
	    var shortText = document.getElementById("short-text");

            shortUrl = result.id;
            shortDiv.innerText = shortUrl;
            shortDiv.href = shortUrl;

            longDiv.innerText = window.intent.data;
            resDiv.style.display = "block";

	    // Select the text for copying.
	    shortText.value = shortUrl;
	    shortText.select();
	    shortText.focus();

	    // TODO(scr) remove when done debugging.
	    setTimeout(function timer() {
			   printFocus();
			   setTimeout(timer, 1000);
		       }, 1000)
	    printFocus();
        } 
    };
    xhr.open('POST', 'https://www.googleapis.com/urlshortener/v1/url');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({'longUrl': window.intent.data}));
};

function finishIntent() {
    window.intent.postResult(shortUrl);
    window.close();
}

window.addEventListener("DOMContentLoaded", function() {
			    if(window.intent) {
				fetchData();
			    }

			    var retButton = document.getElementById("return");
			    retButton.addEventListener("click", finishIntent);
			    var shortForm = document.getElementById("short-form");
			    shortForm.addEventListener('submit', finishIntent);

			    // TODO(scr) remove when done debugging.
			    var focusButton = document.getElementById("focus");
			    focusButton.addEventListener('click', function() {
							     var shortText = document.getElementById("short-text");
							     shortText.select();
							     shortText.focus();
							 });
			}, false);
