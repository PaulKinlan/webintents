var shortUrl;
var fetchData = function() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4 && xhr.status == 200) {
            var result = JSON.parse(xhr.responseText);
            var resDiv = document.getElementById("result");
            var shortDiv = document.getElementById("short");
            var longDiv = document.getElementById("long");

            shortUrl = result.id;
            shortDiv.innerText = shortUrl;
            shortDiv.href = shortUrl;

            longDiv.innerText = window.intent.data;
            resDiv.style.display = "block";
        } 
    };
    xhr.open('POST', 'https://www.googleapis.com/urlshortener/v1/url');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({'longUrl': window.intent.data}));
};

window.addEventListener("DOMContentLoaded", function() {
			    if(window.intent) {
				fetchData();
			    }

			    var retButton = document.getElementById("return");
			    retButton.addEventListener("click", function() {
							   window.intent.postResult(shortUrl);
							   window.close();
						       });
			}, false);
