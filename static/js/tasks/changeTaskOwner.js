function changeTaskOwner(taskId){
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {            
            $('#update-task-owner-form').prop('action', '/tasks/update_task_owner/' + taskId);
            
            var recordOwnerDropdown = document.getElementById('record-owner-dropdown');
            console.log(task.record_owner)
            console.log(task.record_owner_id)
            for (var i = 0; i < recordOwnerDropdown.options.length; i++) {
                if (task.record_owner_id != null && task.record_owner_id != '' && recordOwnerDropdown.options[i].value == task.record_owner_id) {
                    window.alert(recordOwnerDropdown.options[i])
                } else {
                    recordOwnerDropdown.options[i].selected = false;
                };
            };

        },
        error: function (error) {
            console.log(error)
        }
    });
}