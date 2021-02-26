let GPA = document.getElementById("GPA");
let Cred = document.getElementById("Credit");
let computeBtn = document.getElementById("ComputeBtn");



chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "compute") {
        GPA.innerText = request.GPA_res;
        Cred.innerText = request.Credits_res;
    }
  });
  
  function onWindowLoad() {
  
    // var message = document.querySelector('#message');
  
    chrome.tabs.executeScript(null, {
      file: "compute.js"
    }, function() {
      // If you try and inject into an extensions page or the webstore/NTP you'll get an error
      if (chrome.runtime.lastError) {
        // message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
      }
    });
  
  }
  
  window.onload = onWindowLoad;
