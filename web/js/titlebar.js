// Titlebar JS for ZerolfieWM
window.onload = (e)=>{
    // Find the titlebar to initialize
    let titlebar=document.getElementById("titlebar");

    // Initialize the titlebar
    titlebar.querySelector("button#close").addEventListener("click", function(){
        pywebview.api.closeWindow();
    });
    titlebar.querySelector("button#minimize").addEventListener("click", function(){
        pywebview.api.minimizeWindow();
    });
    titlebar.querySelector("button#maximize").addEventListener("click", function(){
        pywebview.api.maximizeWindow();
    });
}