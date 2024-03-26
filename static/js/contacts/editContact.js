function editContact(contactId) {    
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId, 
        dataType: 'json',        
        success: function (contact) {
            $('#edit-contact-form').prop('action', '/contacts/update/' + contactId)
            
            if (contact.prefix != null && contact.prefix != '') {
                $('#prefix-value').prop('value', contact.prefix);
            } else {
                $('#prefix-value').prop('value', '');
            };

            if (contact.first_name != null && contact.first_name != '') {
                $('#first-name-value').prop('value', contact.first_name);
            } else {
                $('#first-name-value').prop('value', '');
            };

            if (contact.last_name != null && contact.last_name != '') {
                $('#last-name-value').prop('value', contact.last_name);
            } else {
                $('#last-name-value').prop('value', '');
            };

            var organziationValue = document.getElementById('organization-value')
            
            if (contact.organization_id != null && contact.organization_id != '') {                
                for (var i = 0; i < organziationValue.options.length; i++) {                                        
                    if (organziationValue.options[i].value == contact.organization_id) {
                        organziationValue.options[i].selected = true;
                    } else {
                        organziationValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < organziationValue.options.length; i++) {
                    organziationValue.options[i].selected = false;
                };
            };

            if (contact.title != null && contact.title != '') {
                $('#title-value').prop('value', contact.title);
            } else {
                $('#title-value').prop('value', '');
            }; 

            if (contact.email != null && contact.email != '') {
                $('#email-value').prop('value', contact.email);
            } else {
                $('#email-value').prop('value', '');
            };

            if (contact.email_opted_out != null && contact.email_opted_out != '' && contact.email_opted_out == true) {
                $('#email-opted-out-value').prop('checked', true);
            } else {
                $('#email-opted-out-value').prop('checked', false);
            }; 

            if (contact.phone != null && contact.phone != '') {
                $('#phone-value').prop('value', contact.phone);
            } else {
                $('#phone-value').prop('value', '');
            };

            if (contact.home_phone != null && contact.home_phone != '') {
                $('#home-phone-value').prop('value', contact.home_phone);
            } else {
                $('#home-phone-value').prop('value', '');
            };

            if (contact.mobile_phone != null && contact.mobile_phone != '') {
                $('#mobile-phone-value').prop('value', contact.mobile_phone);
            } else {
                $('#mobile-phone-value').prop('value', '');
            };

            if (contact.other_phone != null && contact.other_phone != '') {
                $('#other-phone-value').prop('value', contact.other_phone);
            } else {
                $('#other-phone-value').prop('value', '');
            };

            if (contact.assistant_phone != null && contact.assistant_phone != '') {
                $('#assistant-phone-value').prop('value', contact.assistant_phone);
            } else {
                $('#assistant-phone-value').prop('value', '');
            };

            if (contact.assistant_name != null && contact.assistant_name != '') {
                $('#assistant-name-value').prop('value', contact.assistant_name);
            } else {
                $('#assistant-name-value').prop('value', '');
            };

            if (contact.fax != null && contact.fax != '') {
                $('#fax-value').prop('value', contact.fax);
            } else {
                $('#fax-value').prop('value', '');
            };

            if (contact.linkedin != null && contact.linkedin != '') {
                $('#linkedin-value').prop('value', contact.linkedin);
            } else {
                $('#linkedin-value').prop('value', '');
            };

            if (contact.facebook != null && contact.facebook != '') {
                $('#facebook-value').prop('value', contact.facebook);
            } else {
                $('#facebook-value').prop('value', '');
            };

            if (contact.twitter != null && contact.twitter != '') {
                $('#twitter-value').prop('value', contact.twitter);
            } else {
                $('#twitter-value').prop('value', '');
            };

            if (contact.mailing_address != null && contact.mailing_address != '') {
                $('#mailing-address-value').prop('value', contact.mailing_address);
            } else {
                $('#mailing-address-value').prop('value', '');
            };

            if (contact.mailing_city != null && contact.mailing_city != '') {
                $('#mailing-city-value').prop('value', contact.mailing_city);
            } else {
                $('#mailing-city-value').prop('value', '');
            };

            if (contact.mailing_state != null && contact.mailing_state != '') {
                $('#mailing-state-value').prop('value', contact.mailing_state);
            } else {
                $('#mailing-state-value').prop('value', '');
            };

            if (contact.mailing_postal_code != null && contact.mailing_postal_code != '') {
                $('#mailing-postal-code-value').prop('value', contact.mailing_postal_code);
            } else {
                $('#mailing-postal-code-value').prop('value', '');
            };


            var mailingCountryValue = document.getElementById('mailing-country-value');            
            if (contact.mailing_country != null && contact.mailing_country != '') {                
                for (var i = 0; i < mailingCountryValue.options.length; i++) {                                        
                    if (mailingCountryValue.options[i].value == contact.mailing_country) {
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

            if (contact.other_address != null && contact.other_address != '') {
                $('#other-address-value').prop('value', contact.other_address);
            } else {
                $('#other-address-value').prop('value', '');
            };

            if (contact.other_city != null && contact.other_city != '') {
                $('#other-city-value').prop('value', contact.other_city);
            } else {
                $('#other-city-value').prop('value', '');
            };

            if (contact.other_state != null && contact.other_state != '') {
                $('#other-state-value').prop('value', contact.other_state);
            } else {
                $('#other-state-value').prop('value', '');
            };

            if (contact.other_postal_code != null && contact.other_postal_code != '') {
                $('#other-postal-code-value').prop('value', contact.other_postal_code);
            } else {
                $('#other-postal-code-value').prop('value', '');
            };


            var otherCountryValue = document.getElementById('other-country-value');            
            if (contact.other_country != null && contact.other_country != '') {                
                for (var i = 0; i < otherCountryValue.options.length; i++) {                                        
                    if (otherCountryValue.options[i].value == contact.other_country) {
                        otherCountryValue.options[i].selected = true;
                    } else {
                        otherCountryValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < otherCountryValue.options.length; i++) {
                    otherCountryValue.options[i].selected = false;
                };
            };

            if (contact.due_date != null && contact.due_date != '') {
                $('#due-date-value').prop('value', contact.due_date);
            } else {
                $('#due-date-value').prop('value', '');
            };

            if (contact.date_of_birth != null && contact.date_of_birth != '') {
                $('#date-of-birth-value').prop('value', contact.date_of_birth);
            } else {
                $('#date-of-birth-value').prop('value', '');
            };

            if (contact.description != null && contact.description != '') {
                $('#description-value').prop('value', contact.description);
            } else {
                $('#description-value').prop('value', '');
            };

            if (contact.tag_list != null && contact.tag_list != '') {
                $('#tag-list-value').prop('value', contact.tag_list);
            } else {
                $('#tag-list-value').prop('value', '');
            };

        },
        error: function (error) {
            console.error(error);
        }
    });
};