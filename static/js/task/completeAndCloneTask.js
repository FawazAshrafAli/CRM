function completeAndCloneTask(taskId) {
    $.ajax({
        type: 'GET',
        url: '/tasks/detail/' + taskId,
        dataType: 'json',
        success: function (task) {
            if (task.id != null && task.id != '') {
                $('#complete-clone-task').prop('href', '/tasks/complete_and_clone/' + task.id);
            } else {
                $('#complete-clone-task').prop('href', '#');
            };

            if (task.name != null && task.name != '') {
                $('#completion-cloning-task-object').html("'" + task.name + "'");
            } else {
                $('#completion-cloning-task-object').html('');
            };
        },
        error: function (error) {
            console.log(error);
        }
    });
};