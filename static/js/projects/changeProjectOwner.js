function changeProjectOwner(projectId) {
    $.ajax({
        type: 'GET',
        url: '/projects/detail/' + projectId,
        dataType: 'json',
        success: function (project) {
            $('#change_project_owner_form').prop('action', '/projects/update_owner/' + projectId);

            var recordOwnerSelect = document.getElementById('record-owner-select');
            if (project.record_owner_id != null && project.record_owner_id != '') {
                for (var i = 0; i < recordOwnerSelect.options.length; i++) {                    
                    if (recordOwnerSelect.options[i].value == project.record_owner_id) {
                        recordOwnerSelect.options[i].selected = true;
                    } else {
                        recordOwnerSelect.options[i].selected = false;
                    };
                };
            } else {                
                for (var i = 0; i < recordOwnerSelect.options.length; i++) {
                    recordOwnerSelect.options[i].selected = false;
                };
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
};