// http request function to api server
function submit(){
    const text = document.getElementById("input");
    const buttton = document.getElementById("submit");
    //disable the text box for text
    text.disabled = true;
    //clear text
    buttton.disabled = true;
    createUserTextInMyDiv(text.value);
    sendHttpRequest('POST', 'http://localhost:5000/chat', {message: 'hello'})
    text.value = "";
    text.disabled = false;
    buttton.disabled = false;
}

function sendHttpRequest(method, url, data) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function () {
        const text = document.getElementById("input");
        const buttton = document.getElementById("submit");
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(xhr.response);
        createSystemResponseInMyDiv(xhr.response);
      } else {
        reject(xhr.statusText);
        createErrorTextInMyDiv();
      }
    };
    xhr.onerror = function () {
      reject(xhr.statusText);
    };
    xhr.send(JSON.stringify(data));
  });
    
}

function createSystemResponseInMyDiv(response) {
  const mydiv = document.getElementById("myDiv");
  const newDiv = document.createElement("div");
    newDiv.innerText = response;
    newDiv.style.background = "lightgrey";
  mydiv.appendChild(newDiv);
}

function createUserTextInMyDiv(response){
    const mydiv = document.getElementById("myDiv");
    const newDiv = document.createElement("div");
      newDiv.innerText = response;
    mydiv.appendChild(newDiv);
}

function createErrorTextInMyDiv(){
    const mydiv = document.getElementById("myDiv");
    const newDiv = document.createElement("div");
      newDiv.innerText = "Error";
      newDiv.style.background = "red";
    mydiv.appendChild(newDiv);

}

function clearElements(){
    const mydiv = document.getElementById("myDiv");
    mydiv.innerHTML = "";
}

function getHistory(){
    const mydiv = document.getElementById("myDiv");
    //get each element inside of mydiv
    const elements = mydiv.getElementsByTagName("div");
    
}