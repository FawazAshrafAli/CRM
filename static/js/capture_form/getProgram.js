function getProgram() {
    var stateDropdownValue = document.getElementById('stateDropdown').value;
    var cityDropdownValue = document.getElementById('cityDropdown').value;
    window.alert('Working')
    $.ajax({
        type: 'POST',
        url: '/capture_form/get_program/',
        dataType: 'json',
        data: {'state': stateDropdownValue, 'city': cityDropdownValue},
        success: function (data) {
            
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    })

}