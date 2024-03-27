function completeTask(taskId) {
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {
            if (task.id != null && task.id != '') {
                $('#complete-task').prop('href', '/tasks/complete/' + task.id);                
            } else {
                $('#complete-task').prop('href', '#');
            };

            if (task.name != null && task.name != '') {
                $('#completion-task-object').html("'" + task.name + "'");
            } else {
                $('#completion-task-object').html('');
            };
        },
        error: function (error) {
            console.log(error);
        }
    });
};