function getProgram() {
    var stateDropdownValue = document.getElementById('stateDropdown').value;
    var cityDropdownValue = document.getElementById('cityDropdown').value;
    
    if (cityDropdownValue != null && cityDropdownValue != '') {
        document.getElementById('program-dropdown').removeAttribute('disabled');
        document.getElementById('course-dropdown').setAttribute('disabled', true);
    };

    $.ajax({
        type: 'GET',
        url: '/form/get_programs/',
        dataType: 'json',
        data: {'state': stateDropdownValue, 'city': cityDropdownValue},
        success: function (data) {
            var programDropdown = $('#program-dropdown');
            programDropdown.html('<option hidden disabled selected>Select Program</option>');
            $.each(data, function(index, value) {
                programDropdown.append('<option value="' + value[0] + '">' + value[1] + '</option>');
            });
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
}
