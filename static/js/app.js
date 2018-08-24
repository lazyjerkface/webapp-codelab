// Adds a link to view individual patients to each row.
function linkifyRows() {
  var patientTable = document.getElementById('patient-table');
  var patientRows = patientTable.getElementsByClassName('patient-row');
  for (var i = 0; i < patientRows.length; i++) {
    var elem = patientRows[i];
    elem.onclick = function() {
      //window.location.href = '/view/' + this.id;
      alert('Redirect me to /view/' + this.id);
      // HINT: window.location.href
    }
  }
}
// Functions that run after the page loads.
window.onload = function(e) {
  linkifyRows();
}