function editEducation(educationId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/education/' + educationId,
        dataType: 'json',
        success: function (education) {
            $('#education-updation-form').prop('action', '/authentication/edit_education/' + educationId);

            if (education.institution != null && education.institution != '') {
                $('#institution-value').prop('value', education.institution);
            } else {
                $('#institution-value').prop('value', '');
            };

            if (education.course != null && education.course != '') {
                $('#course-value').prop('value', education.course);
            } else {
                $('#course-value').prop('value', '');
            };

            if (education.started_year != null && education.started_year != '') {
                $('#started-year-value').prop('value', education.started_year);
            } else {
                $('#started-year-value').prop('value', '');
            };

            if (education.completed_year != null && education.completed_year != '' && education.completed_year != 'Present') {
                $('#completed-year-value').prop('value', education.completed_year);
                $('#education-update-checkbox').prop("checked", false);
            } else {
                $('#completed-year-value').prop('value', '');
                $('#education-update-checkbox').prop("checked", true);
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};

$('#completed-year-value').on('input', function () {
    if (this.value != null && this.value != '') {
        $('#education-update-checkbox').prop("checked", false);
    } else {
        $('#education-update-checkbox').prop("checked", true);
    };
});

var currentValue = '';

$('#education-update-checkbox').click(function () {
    if ($(this).prop('checked') == true) {
        currentValue = $('#completed-year-value').val();
        $('#completed-year-value').val('');
    } else {
        $('#completed-year-value').val(currentValue);
    };
});