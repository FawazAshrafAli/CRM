function cloneTask(taskId) {
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {
            if (task.id != null && task.id != '') {
                $('#clone-task').prop('href', '/tasks/clone/' + task.id);                
            } else {
                $('#clone-task').prop('href', '#');
            };

            if (task.name != null && task.name != '') {
                $('#cloning-task-object').html("'" + task.name + "'");
            } else {
                $('#cloning-task-object').html('');
            };
        },
        error: function (error) {
            console.log(error);
        }
    });
};