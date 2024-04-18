var updateEducationForm = document.getElementById('update-education-form');    

var completedYear = updateEducationForm.completed_year
var presentCheckbox = updateEducationForm.present

var current_completion_year_value = ''

completedYear.addEventListener(('input'), function() {
    var completedYearvalue = updateEducationForm.completed_year.value;
    if (completedYearvalue != null && completedYearvalue != '') {
        presentCheckbox.removeAttribute('checked')
    } else {
        presentCheckbox.setAttribute('checked', true);
    };
});

presentCheckbox.addEventListener('click', function () {    
    if (presentCheckbox.checked == true) {
        current_completion_year_value = completedYear.value
        completedYear.value = '';
    } else {
        completedYear.value = current_completion_year_value        
    };
});
