function editLead(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#lead-edition-form').prop('action', '/leads/update/' + lead.id);

            if (lead.prefix != null && lead.prefix != '') {
                $('#prefix-value').prop('value', lead.prefix);
            } else {
                $('#prefix-value').prop('value', '');
            };

            if (lead.first_name != null && lead.first_name != '') {
                $('#first-name-value').prop('value', lead.first_name);
            } else {
                $('#first-name-value').prop('value', '');
            };

            if (lead.last_name != null && lead.last_name != '') {
                $('#last-name-value').prop('value', lead.last_name);
            } else {
                $('#last-name-value').prop('value', '');
            };

            var organizationValue = document.getElementById('organization-value')

            if (lead.organization != null && lead.organization != '') {
                for (var i = 0; i < organizationValue.options.length; i++) {
                    if (organizationValue.options[i].value == lead.organization) {
                        organizationValue.options[i].selected = true;                        
                    } else {
                        organizationValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < organizationValue.options.length; i++) {
                    organizationValue.options[i].selected = false;
                };
            };

            if (lead.title != null && lead.title != '') {
                $('#title-value').prop('value', lead.title);
            } else {
                $('#title-value').prop('value', '');
            };

            var leadStatusValue = document.getElementById('lead-status-value')

            if (lead.lead_status != null && lead.lead_status != '') {
                for (var i = 0; i < leadStatusValue.options.length; i++) {
                    if (leadStatusValue.options[i].value == lead.lead_status) {
                        leadStatusValue.options[i].selected = true;                        
                    } else {
                        leadStatusValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < leadStatusValue.options.length; i++) {
                    leadStatusValue.options[i].selected = false;
                };
            };

            var userResponsibleValue = document.getElementById('user-responsible-value')

            if (lead.user_responsible != null && lead.user_responsible != '') {
                for (var i = 0; i < userResponsibleValue.options.length; i++) {
                    if (userResponsibleValue.options[i].value == lead.user_responsible) {
                        userResponsibleValue.options[i].selected = true;                        
                    } else {
                        userResponsibleValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < userResponsibleValue.options.length; i++) {
                    userResponsibleValue.options[i].selected = false;
                };
            };

            if (lead.lead_rating != null && lead.lead_rating != '') {
                $('#lead-rating-value').prop('value', lead.lead_rating);
            } else {
                $('#lead-rating-value').prop('value', '');
            };
            
            var leadOwnerValue = document.getElementById('lead-owner-value')
            if (lead.lead_owner != null && lead.lead_owner != '') {
                for (var i = 0; i < leadOwnerValue.options.length; i++) {
                    if (leadOwnerValue.options[i].value == lead.lead_owner) {
                        leadOwnerValue.options[i].selected = true;                        
                    } else {
                        leadOwnerValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < leadOwnerValue.options.length; i++) {
                    leadOwnerValue.options[i].selected = false;
                };
            };

            if (lead.email != null && lead.email != '') {
                $('#email-value').prop('value', lead.email);
            } else {
                $('#email-value').prop('value', '');
            };

            if (lead.email_opted_out != null && lead.email_opted_out != '') {
                $('#email-opted-out-value').prop('checked', true);
            } else {
                $('#email-opted-out-value').prop('checked', false);
            };

            if (lead.phone != null && lead.phone != '') {
                $('#phone-value').prop('value', lead.phone);
            } else {
                $('#phone-value').prop('value', '');
            };

            if (lead.mobile_phone != null && lead.mobile_phone != '') {
                $('#mobile-phone-value').prop('value', lead.mobile_phone);
            } else {
                $('#mobile-phone-value').prop('value', '');
            };

            if (lead.fax != null && lead.fax != '') {
                $('#fax-value').prop('value', lead.fax);
            } else {
                $('#fax-value').prop('value', '');
            };

            if (lead.website != null && lead.website != '') {
                $('#website-value').prop('value', lead.website);
            } else {
                $('#website-value').prop('value', '');
            };

            if (lead.industry != null && lead.industry != '') {
                $('#industry-value').prop('value', lead.industry);
            } else {
                $('#industry-value').prop('value', '');
            };

            if (lead.number_of_employees != null && lead.number_of_employees != '') {
                $('#number-of-employees-value').prop('value', lead.number_of_employees);
            } else {
                $('#number-of-employees-value').prop('value', '');
            };

            var leadSourceValue = document.getElementById('lead-source-value')

            if (lead.lead_source != null && lead.lead_source != '') {
                for (var i = 0; i < leadSourceValue.options.length; i++) {
                    if (leadSourceValue.options[i].value == lead.lead_source) {
                        leadSourceValue.options[i].selected = true;                        
                    } else {
                        leadSourceValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < leadSourceValue.options.length; i++) {
                    leadSourceValue.options[i].selected = false;
                };
            };

            if (lead.mailing_address != null && lead.mailing_address != '') {
                $('#mailing-address-value').prop('value', lead.mailing_address);
            } else {
                $('#mailing-address-value').prop('value', '');
            };

            if (lead.mailing_city != null && lead.mailing_city != '') {
                $('#mailing-city-value').prop('value', lead.mailing_city);
            } else {
                $('#mailing-city-value').prop('value', '');
            };

            if (lead.mailing_state != null && lead.mailing_state != '') {
                $('#mailing-state-value').prop('value', lead.mailing_state);
            } else {
                $('#mailing-state-value').prop('value', '');
            };

            if (lead.mailing_postal_code != null && lead.mailing_postal_code != '') {
                $('#mailing-postal-code-value').prop('value', lead.mailing_postal_code);
            } else {
                $('#mailing-postal-code-value').prop('value', '');
            };

            var mailingCountryValue = document.getElementById('mailing-country-value')

            if (lead.mailing_country != null && lead.mailing_country != '') {
                for (var i = 0; i < mailingCountryValue.options.length; i++) {
                    if (mailingCountryValue.options[i].value == lead.mailing_country) {
                        mailingCountryValue.options[i].selected = true;                        
                    } else {
                        mailingCountryValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < mailingCountryValue.options.length; i++) {
                    mailingCountryValue.options[i].selected = false;
                };
            };

            if (lead.description != null && lead.description != '') {
                $('#description-value').prop('value', lead.description);
            } else {
                $('#description-value').prop('value', '');
            };

            if (lead.tag_list != null && lead.tag_list != '') {
                $('#tag-list-value').prop('value', lead.tag_list);
            } else {
                $('#tag-list-value').prop('value', '');
            };

            var permissionValue = document.getElementById('permission-value')

            if (lead.permission != null && lead.permission != '') {
                for (var i = 0; i < permissionValue.options.length; i++) {
                    if (permissionValue.options[i].value == lead.permission) {
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
            console.error('Error: ', error);
        }
    });
};