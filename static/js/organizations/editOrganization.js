function editOrganization (organizationId) {
    $.ajax({
        type: 'GET',
        url: '/organizations/detail/' + organizationId,
        dataType: 'json',
        success: function(organization) {
            if (organization.name != null && organization.name != "") {
                $('#organization-name-value').prop('value', organization.name);
            } else {
                $('#organization-name-value').prop('value', '');
            };

            var organizationValue = document.getElementById('organization-value');

            if (organization.organization != null && organization.organization != '') {
                for (var i = 0; i < organizationValue.options.length; i++) {
                    if (organizationValue.options[i].value == organization.organization) {
                        organizationValue.options[i].selected = true;
                    } else {
                        organizationValue.options[i].selected = false;
                    };
                }
            } else {
                for (var i = 0; i < organizationValue.options.length; i++) {
                    organizationValue.options[i].selected = false;
                }
            };

            if (organization.title != null && organization.title != '') {
                ('#title-value').prop('value', organization.title);
            } else {
                ('#title-value').prop('value', '');
            };

            if (organization.phone != null && organization.phone != '') {
                ('#phone-value').prop('value', organization.phone);
            } else {
                ('#phone-value').prop('value', '');
            };

            if (organization.fax != null && organization.fax != '') {
                ('#fax-value').prop('value', organization.fax);
            } else {
                ('#fax-value').prop('value', '');
            };

            if (organization.website != null && organization.website != '') {
                ('#website-value').prop('value', organization.website);
            } else {
                ('#website-value').prop('value', '');
            };

            if (organization.linkedin != null && organization.linkedin != '') {
                ('#linkedin-value').prop('value', organization.linkedin);
            } else {
                ('#linkedin-value').prop('value', '');
            };

            if (organization.facebook != null && organization.facebook != '') {
                ('#facebook-value').prop('value', organization.facebook);
            } else {
                ('#facebook-value').prop('value', '');
            };

            if (organization.twitter != null && organization.twitter != '') {
                ('#twitter-value').prop('value', organization.twitter);
            } else {
                ('#twitter-value').prop('value', '');
            };

            if (organization.email_domains != null && organization.email_domains != '') {
                ('#email-domain-value').prop('value', organization.email_domains);
            } else {
                ('#email-domain-value').prop('value', '');
            };

            if (organization.billing_address != null && organization.billing_address != '') {
                ('#billing-address-value').prop('value', organization.billing_address);
            } else {
                ('#billing-address-value').prop('value', '');
            };

            if (organization.billing_city != null && organization.billing_city != '') {
                ('#billing-city-value').prop('value', organization.billing_city);
            } else {
                ('#billing-city-value').prop('value', '');
            };

            if (organization.billing_state != null && organization.billing_state != '') {
                ('#billing-state-value').prop('value', organization.billing_state);
            } else {
                ('#billing-state-value').prop('value', '');
            };
        },
        error: function (error) {
            console.error(error);
        }
    });
};