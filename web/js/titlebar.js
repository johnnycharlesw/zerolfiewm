// Titlebar JS for ZerolfieWM
window.onload = (e)=>{
    // Find the titlebar to initialize
    let titlebar=document.getElementById("titlebar");

    // Initialize the titlebar
    titlebar.children.namedItem("close").addEventListener("click", function(){
        pywebview.api.closeWindow();
    });
    titlebar.children.namedItem("minimize").addEventListener("click", function(){
        pywebview.api.minimizeWindow();
    });
    titlebar.children.namedItem("maximize").addEventListener("click", function(){
        pywebview.api.maximizeWindow();
    });
}