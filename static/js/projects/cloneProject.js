function cloneProject(projectId) {
    $.ajax({
        type: 'GET',
        url: '/projects/detail/' + projectId,
        dataType: 'json',
        success: function (project) {
            $('#clone_project_form').prop('action', '/projects/clone/' + projectId);            

            if (project.name != null && project.name != '') {
                $('#cloning-project-object').html(project.name);
            } else {
                $('#cloning-project-object').html('');
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        },
    });
};