function loadCrmUserDetails(userId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/detail/' + userId,
        dataType: 'json',
        success: function (user) {
            $('.user-id').each(function () {
                if (user.id != null && user.id != "") {
                    $(this).html(user.id);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-name').each(function () {
                if (user.name != null && user.name != "") {
                    $(this).html(user.name);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-title').each(function () {                
                if (user.title != null && user.title != "") {
                    $(this).html(user.title);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-email').each(function () {
                if (user.email != null && user.email != "") {
                    $(this).html(user.email);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-birthday').each(function () {
                if (user.birthday != null && user.birthday != "") {
                    $(this).html(user.birthday);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-address').each(function () {
                if (user.address != null && user.address != "") {
                    $(this).html(user.address);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-address-city').each(function () {
                if (user.address_city != null && user.address_city != "") {
                    $(this).html(user.address_city);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-address-state').each(function () {
                if (user.address_state != null && user.address_state != "") {
                    $(this).html(user.address_state);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-postal-code').each(function () {
                if (user.address_postal_code != null && user.address_postal_code != "") {
                    $(this).html(user.address_postal_code);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-address-country').each(function () {
                if (user.address_country != null && user.address_country != "") {
                    $(this).html(user.address_country);
                } else {
                    $(this).html("None");
                }
            });            

            $('.user-phone').each(function () {
                if (user.phone != null && user.phone != "") {
                    $(this).html(user.phone);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-birthday').each(function () {
                if (user.birthday != null && user.birthday != "") {
                    $(this).html(user.birthday);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-created').each(function () {
                if (user.created != null && user.created != "") {
                    $(this).html(user.created);
                } else {
                    $(this).html("None");
                }
            });

            $('.user-updated').each(function () {
                if (user.updated != null && user.updated != "") {
                    $(this).html(user.updated);
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