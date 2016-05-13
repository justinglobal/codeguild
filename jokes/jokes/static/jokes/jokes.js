// js file for jokes project

'use strict';


function makeVisible(id) {
  $('#punchlines_' + id).toggle('slow');
}

// .css() to 'toggle' "visibility" instead of using 'display'
// function makeVisible(id) {
//   document.getElementById('punchlines_' + id).style.visibility='visible';
// }
