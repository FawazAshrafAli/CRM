function editTask(taskId) {
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {
            $('#update-task-form').prop('action', '/tasks/update/' + taskId)

            if (task.name != null && task.name != ''){
                $('#task-name-value').prop('value', task.name);
            } else {
                $('#task-name-value').prop('value', '');
            };
            
            if (task.assigned_to != null && task.assigned_to != ''){
                $('#task-assigned-to-' + task.assigned_to_pk).prop('selected', true);
            } else {
                $('#task-assigned-to-' + task.assigned_to_pk).prop('selected', false);
            };

            
            var categoryValue = document.getElementById("category-value");
            if (task.category != null && task.category != ''){
                for (var i = 0; i < categoryValue.options.length; i++) {
                    if (categoryValue.options[i].value === task.category) {
                        categoryValue.options[i].selected = true;                        
                    } else {
                        categoryValue.options[i].selected = false;
                    };
                }                
            } else {
                for (var i = 0; i < selectElement.options.length; i++) {                    
                    selectElement.options[i].selected = false;
                }
            };
            
            if (task.due_date != null && task.due_date != "") {
                $('#due-date-value').prop('value', task.due_date);    
            } else {
                $('#due-date-value').prop('value','');
            };

            if (task.start_date != null && task.start_date != "") {
                $('#start-date-value').prop('value', task.start_date);    
            } else {
                $('#start-date-value').prop('value','');
            };

            if (task.reminder_date != null && task.reminder_date != "") {
                $('#reminder-date-value').prop('value', task.reminder_date);    
            } else {
                $('#reminder-date-value').prop('value','');
            };

            if (task.progress != null && task.progress != "") {
                $('#progress-value').prop('value', task.progress);    
            } else {
                $('#progress-value').prop('value','');
            };
            
            var priorityValue = document.getElementById('priority-value');    
            if (task.priority != null && task.priority != '') {                          
                for(var i=0; 1 < priorityValue.options.length; i++) {
                    if (priorityValue.options[i].value === task.priority) {
                        priorityValue.options[i].selected = true;
                        break;
                    } else {
                        priorityValue.options[i].selected = false;
                    };                                        
                };                
            } else {
                for(var i=0; 1 < priorityValue.options.length; i++) {
                    priorityValue.options[i].selected = false;                    
                };                
            };            

            var statusValue = document.getElementById('status-value');
            if (task.status != null && task.status != ''){                
                for (var i = 0; i < statusValue.options.length; i++) {                    
                    if (statusValue.options[i].value === task.status) {
                        statusValue.options[i].selected = true;
                        break;
                    } else {
                        statusValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < statusValue.options.length; i++) {                    
                    statusValue.options[i].selected = false;                    
                };
            };

            var relatedToValue = document.getElementById('related-to-value');
            if (task.related_to != null && task.related_to != '') {                
                for (var i = 0; i < relatedToValue.options.length; i++) {
                    if (relatedToValue.options[i].value === task.related_to) {
                        relatedToValue.options[i].selected = true;
                    } else {
                        relatedToValue.options[i].selected = false;
                    };                    
                };
            } else {
                for (var i = 0; i < relatedToValue.options.length; i++) {
                    relatedToValue.options[i].selected = false;                    
                };
            };
            
            if (task.description != null && task.description != '') {
                $('#description-value').html(task.description);                
            } else {
                $('#description-value').html('');
            };
            
            var permissionValue = document.getElementById('permission-value');
            if (task.permission != null && task.permission != '') {                
                for (var i = 0; i < permissionValue.options.length; i++) {
                    if (permissionValue.options[i].value === task.permission) {
                        permissionValue.options[i].selected = true;
                    } else {
                        permissionValue.options[i].selected = false;
                    };                    
                };
            } else {
                for (var i = 0; i < permissionValue.options.length; i++) {
                    permissionValue.options[i].selected = false;                    
                };
            };
            
        },
        error: function (error) {
            console.log(error);
        }
    })
}