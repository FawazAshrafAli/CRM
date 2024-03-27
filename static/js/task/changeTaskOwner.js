function changeTaskOwner(taskId){
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {            
            $('#update-task-owner-form').prop('action', '/tasks/update_task_owner/' + taskId);
            
            if (task.task_owner != null && task.task_owner != '') {
                $('#task-owner-value').prop('value', task.task_owner);
            } else {
                $('#task-owner-value').prop('value', '');
            };

        },
        error: function (error) {
            console.log(error)
        }
    });
}