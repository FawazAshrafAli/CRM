function deleteTask(taskId) {
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {
            if (task.id != null && task.id != '') {
                $('#delete-task').prop('href', '/tasks/delete/' + task.id);                
            } else {
                $('#delete-task').prop('href', '#');
            };

            if (task.name != null && task.name != '') {
                $('#deletion-task-object').html("'" + task.name + "'");
            } else {
                $('#deletion-task-object').html('');
            };
        },
        error: function (error) {
            console.log(error);
        }
    });
};