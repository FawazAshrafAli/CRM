function editExperience(experienceId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/experience/' + experienceId,
        dataType: 'json',
        success: function (experience) {
            $('#experience-updation-form').prop('action', '/authentication/edit_experience/' + experienceId);

            if (experience.designation != null && experience.designation != '') {
                $('#designation-value').val(experience.designation);
            } else {
                $('#designation-value').val('');
            };

            if (experience.company != null && experience.company != '') {
                $('#company-value').val(experience.company);
            } else {
                $('#company-value').val('');
            };

            if (experience.started_month_and_year != null && experience.started_month_and_year != '') {
                $('#started-month-and-year-value').val(experience.started_month_and_year);
            } else {
                $('#started-month-and-year-value').val('');
            };

            if (experience.completed_month_and_year != null && experience.completed_month_and_year != '') {
                $('#completed-month-and-year-value').val(experience.completed_month_and_year);
                $('#experience-update-checkbox').prop("checked", false);
            } else {
                $('#completed-month-and-year-value').val('');
                $('#experience-update-checkbox').prop("checked", true);
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};


$('#completed-month-and-year-value').on('input', function () {
    if (this.value != null && this.value != '') {
        $('#experience-update-checkbox').prop("checked", false);
    } else {
        $('#experience-update-checkbox').prop("checked", true);
    };
});

var currentValue = '';

$('#experience-update-checkbox').click(function () {
    if ($(this).prop('checked') == true) {
        currentValue = $('#completed-month-and-year-value').val();
        $('#completed-month-and-year-value').val('');
    } else {
        $('#completed-month-and-year-value').val(currentValue);
    };
});