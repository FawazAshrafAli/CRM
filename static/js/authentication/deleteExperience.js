function deleteExperience(experienceId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/experience/' + experienceId,
        dataType: 'json',
        success: function (experience) {
            $('#experience-deletion-form').prop('action', '/authentication/delete_experience/' + experienceId);

            if (experience.designation != null && experience.designation != '' && experience.company != null && experience.company != '') {
                $('#experience-deletion-object').html(experience.designation + ' at ' + experience.company);
            } else {
                $('#experience-deletion-object').html('');
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        }
    })
}