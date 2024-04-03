function editProject(projectId) {
    $.ajax({
        type: 'GET',
        url: '/projects/detail/' + projectId,
        dataType: 'json',
        success: function (project) {
            $('#edit_project_form').prop('action', '/projects/update/' + projectId);

            if (project.name != null && project.name != '') {
                $('#name-value').prop('value', project.name);
            } else {
                $('#name-value').prop('value', '');
            };

            var statusSelect = document.getElementById('status-select');
            if (project.status != null && project.status != '') {
                for (var i = 0; i < statusSelect.options.length; i++) {
                    if  (statusSelect.options[i].value == project.status) {
                        statusSelect.options[i].selected = true;
                    } else {
                        statusSelect.options[i].selected = false;
                    }; 
                };
            } else {
                for (var i = 0; i < statusSelect.options.length; i++) {
                    statusSelect.options[i].selected = false;
                };
            };

            var categorySelect = document.getElementById('category-select')
            if (project.category != null && project.category != '') {                
                for (var i = 0; i < categorySelect.options.length; i++) {
                    if (categorySelect.options[i].value == project.category) {
                        categorySelect.options[i].selected = true;
                    } else {
                        categorySelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < categorySelect.options.length; i++) {
                    categorySelect.options[i].selected = false;
                }
            };

            var userResponsibleSelect = document.getElementById('user-responsible-select');
            if (project.user_responsible_id != null && project.user_responsible_id != '') {
                for (var i = 0; i < userResponsibleSelect.options.length; i++) {
                    if (userResponsibleSelect.options[i].value == project.user_responsible_id) {
                        userResponsibleSelect.options[i].selected = true;  
                    } else {
                        userResponsibleSelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < userResponsibleSelect.options.length; i++) {
                    userResponsibleSelect.options[i].selected = false;
                };
            };

            var pipelineSelect = document.getElementById('pipeline-select');
            if (project.pipeline != null && project.pipeline != '') {
                for (var i = 0; i < pipelineSelect.options.length; i++) {
                    if (pipelineSelect.options[i].value == project.pipeline) {
                        pipelineSelect.options[i].selected = true;
                    } else {
                        pipelineSelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < pipelineSelect.options.length; i++) {
                    pipelineSelect.options[i].selected = false;
                }
            };

            var stageSelect = document.getElementById('stage-select');
            var stage_array = project.stage_id
            if (stage_array != null && stage_array != '') {
                for (var i = 0; i < stageSelect.options.length; i++) {                    
                    if (stage_array.includes(parseInt(stageSelect.options[i].value))) {
                        stageSelect.options[i].selected = true;
                    } else {
                        stageSelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < stageSelect.options.length; i++) {
                    stageSelect.options[i].selected = false;
                };
            };

            if (project.description != null && project.description != '') {
                $('#description-value').prop('value', project.description);
            } else {
                $('#description-value').prop('value', '');
            };

            if (project.tag_list != null && project.tag_list != '') {
                $('#tag-list-value').prop('value', project.tag_list);
            } else {
                $('#tag-list-value').prop('value', '');
            };
            
            var visibilitySelect = document.getElementById('visibility-select');
            if (project.visibility != null && project.visibility != '') {
                for (var i = 0; i < visibilitySelect.options.length; i++) {
                    if (visibilitySelect.options[i].value == project.visibility) {
                        visibilitySelect.options[i].selected = true;
                    } else {
                        visibilitySelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < visibilitySelect.options.length; i++) {
                    visibilitySelect.options[i].selected = false;
                };
            };

        },
        error: function (error) {
            console.log('Error: ', error);
        }
    })
}