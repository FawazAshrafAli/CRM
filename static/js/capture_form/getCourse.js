function getCourse() {
    var stateDropdownValue = document.getElementById('stateDropdown').value;
    var cityDropdownValue = document.getElementById('cityDropdown').value;
    var programDropdownValue = document.getElementById('program-dropdown').value;
    
    if (programDropdownValue != null && programDropdownValue != '') {
        document.getElementById('course-dropdown').removeAttribute('disabled')
    }

    $.ajax({
        type: 'GET',
        url: '/form/get_course/',
        dataType: 'json',
        data: {'state': stateDropdownValue, 'city': cityDropdownValue, 'program': programDropdownValue},
        success: function (data) {
            var courseDropdown = $('#course-dropdown');
            courseDropdown.html('<option hidden disabled selected>Select Course</option>');
            $.each(data, function(index, value) {
                courseDropdown.append('<option value="' + value[0] + '">' + value[1] + '</option>');
            });
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
}
