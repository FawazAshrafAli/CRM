function loadCrmUserDetails(userId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/detail/' + userId,
        dataType: 'json',
        success: function (user) {
            $('.user-id').each(function () {
                if (user.id != null || user.id != "") {
                    $(this).html(user.id);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-name').each(function () {
                if (user.name != null || user.name != "") {
                    $(this).html(user.name);
                } else {
                    $(this).html("None");
                }
            });

        },
        error: function (error) {
            console.log("Error: ", error);
        }
    });
};