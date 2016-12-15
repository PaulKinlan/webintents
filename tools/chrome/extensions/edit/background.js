function clickHandler(info, tab) {
  if(info.mediaType == "image" ||
     info.mediaType == "video" ||
     info.mediaType == "audio") {
     var i = new WebKitIntent({"action": "http://webintents.org/edit", "type": info.mediaType + "/*", "data": info.linkUrl });
       
     window.navigator.webkitStartActivity(i, function() {}, function() {});
   }
   else if(!!info.linkUrl) {
     var i = new WebKitIntent({"action": "http://webintents.org/edit", "type": "text/uri-list", "data": info.linkUrl });
     window.navigator.webkitStartActivity(i, function() {}, function() {});
   }
};

chrome.browserAction.onClicked.addListener(function(tab) {
  clickHandler({linkUrl: tab.url}, tab);
});

chrome.contextMenus.create({
  "title" : "Edit",
  "type" : "normal",
  "contexts" : ["image", "video", "audio"],
  "onclick" : clickHandler 
}); 
