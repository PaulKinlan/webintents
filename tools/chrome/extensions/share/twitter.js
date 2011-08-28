

var addIntent = function() {
  // Always add the intent in.
  var intentEl = document.createElement("intent");
  intentEl.setAttribute("action", "http://webintents.org/share");
  intentEl.setAttribute("type", "text/uri-list");
  intentEl.setAttribute("href", document.location.href);
  document.head.appendChild(intentEl);
};

var checkIntent = function() {
    if (!window.intent)
      return;

    setTimeout(function() {
      var se = document.getElementsByClassName('twitter-anywhere-tweet-box-editor')[0];
      se.value = window.intent.data;
      se.focus();
    }, 2000);
}

if(document.readyState == "complete") {
  addIntent();
  checkIntent();
}
else {
  window.addEventListener("load", addIntent, false);
  window.addEventListener("load", checkIntent, false);
}
