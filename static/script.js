function toggleDropdown()
{
  var dropdownContent=document.getElementById("optionsDropdown").getElementsByClassName("dropdown-content")[0];
  dropdownContent.style.display=(dropdownContent.style.display=="block")?"none":"block";
}
document.addEventListener("click",function(event){
  var optionsDropdown=document.getElementById("optionsDropdown");
  if(optionsDropdown && !optionsDropdown.contains(event.target)){
    var dropdownContent=optionsDropdown.getElementsByClassName("dropdown-content")[0];
    if(dropdownContent){
    dropdownContent.style.display="none";
  }}
  
  });
function loadPDF(pdfUrl) {
  var pdfViewerContainer = document.getElementById('pdfViewerContainer');
  pdfViewerContainer.innerHTML = '<iframe src="' + pdfUrl + '" width="100%" height="600px"></iframe>';
}


