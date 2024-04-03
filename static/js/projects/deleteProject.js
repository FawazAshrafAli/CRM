function deleteProject(projectId) {
    $.ajax({
        type: 'GET',
        url: '/projects/detail/' + projectId,
        dataType: 'json',
        success: function (project) {
            $('#delete_project_form').prop('action', '/projects/delete/' + projectId);

            if (project.name != null && project.name != '') {
                $('#deleting-project-object').html(project.name);
            } else {
                $('#deleting-project-object').html('');
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
};