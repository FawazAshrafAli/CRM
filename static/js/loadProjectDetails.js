function loadProjectDetails(projectId) {
    $.ajax({
        type: "GET",
        url: "/projects/detail/" + projectId,
        dataType: 'json',
        success: function (project){
            $('.project-id').each(function () {                
                if (project.id != null || project.id != ""){
                    $(this).html(project.id);                
                } else {
                    $(this).html("None");
                }
            });

            $('.project-name').each(function () {
                if (project.name != null || project.name != "") {
                    $(this).html(project.name);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-status').each(function () {
                if (project.status != null || project.status != "") {
                    $(this).html(project.status);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-category').each(function () {
                if (project.category != null || project.category != "") {
                    $(this).html(project.category);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-user-responsible').each(function () {
                if (project.user_responsible != null || project.user_responsible != "") {
                    $(this).html(project.user_responsible);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-pipeline-type').each(function () {
                if (project.pipeline != null || project.pipeline != "") {
                    $(this).html(project.pipeline);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-stage').each(function () {
                if (project.stage != null || project.stage != "") {
                    $(this).html(project.stage);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-description').each(function () {
                if (project.description != null || project.description != "") {
                    $(this).html(project.description);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-tag-list').each(function () {
                if (project.tag_list != null || project.tag_list != "") {
                    $(this).html(project.tag_list);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-visibility').each(function () {
                if (project.visibility != null || project.visibility != "") {
                    $(this).html(project.visibility);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-created').each(function () {
                if (project.created != null || project.created != "") {
                    $(this).html(project.created);
                } else {
                    $(this).html("None");
                }
            });

            $('.project-updated').each(function () {
                if (project.updated != null || project.updated != "") {
                    $(this).html(project.updated);
                } else {
                    $(this).html("None");
                }
            });
        },
        error: function(error) {
            console.error(error);
        }
    })
};