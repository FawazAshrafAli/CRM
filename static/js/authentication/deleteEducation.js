function deleteEducation(educationId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/education/' + educationId,
        dataType: 'json',
        success: function (education) {
            $('#education-deletion-form').prop('action', '/authentication/delete_education/' + educationId);

            if (education.course != null && education.course != '') {
                $('#education-deletion-object').html(education.course);
            } else {
                $('#education-deletion-object').html('');
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        },
    })
}