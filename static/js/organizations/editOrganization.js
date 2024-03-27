function editOrganization (organizationId) {
    $.ajax({
        type: 'GET',
        url: '/organizations/detail/' + organizationId,
        dataType: 'json',
        success: function(organization) {
            $('#edit-organization-form').prop('action', '/organizations/update/' + organizationId);

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
                $('#title-value').prop('value', organization.title);
            } else {
                $('#title-value').prop('value', '');
            };

            if (organization.phone != null && organization.phone != '') {
                $('#phone-value').prop('value', organization.phone);
            } else {
                $('#phone-value').prop('value', '');
            };

            if (organization.fax != null && organization.fax != '') {
                $('#fax-value').prop('value', organization.fax);
            } else {
                $('#fax-value').prop('value', '');
            };

            if (organization.website != null && organization.website != '') {
                $('#website-value').prop('value', organization.website);
            } else {
                $('#website-value').prop('value', '');
            };

            if (organization.linkedin != null && organization.linkedin != '') {
                $('#linkedin-value').prop('value', organization.linkedin);
            } else {
                $('#linkedin-value').prop('value', '');
            };

            if (organization.facebook != null && organization.facebook != '') {
                $('#facebook-value').prop('value', organization.facebook);
            } else {
                $('#facebook-value').prop('value', '');
            };

            if (organization.twitter != null && organization.twitter != '') {
                $('#twitter-value').prop('value', organization.twitter);
            } else {
                $('#twitter-value').prop('value', '');
            };

            if (organization.email_domains != null && organization.email_domains != '') {
                $('#email-domain-value').prop('value', organization.email_domains);
            } else {
                $('#email-domain-value').prop('value', '');
            };

            if (organization.billing_address != null && organization.billing_address != '') {
                $('#billing-address-value').prop('value', organization.billing_address);
            } else {
                $('#billing-address-value').prop('value', '');
            };

            if (organization.billing_city != null && organization.billing_city != '') {
                $('#billing-city-value').prop('value', organization.billing_city);
            } else {
                $('#billing-city-value').prop('value', '');
            };

            if (organization.billing_state != null && organization.billing_state != '') {
                $('#billing-state-value').prop('value', organization.billing_state);
            } else {
                $('#billing-state-value').prop('value', '');
            };
            
            if (organization.billing_postal_code != null && organization.billing_postal_code != '') {
                $('#billing-postal-code-value').prop('value', organization.billing_postal_code);
            } else {
                $('#billing-postal-code-value').prop('value', '');
            };            
            
            var billingCountryValue = document.getElementById('billing-country-value');            
            if (organization.billing_country != null && organization.billing_country != '') {                
                for (var i = 0; i < billingCountryValue.options.length; i++) {
                    if (billingCountryValue.options[i].value == organization.billing_country) {
                        billingCountryValue.options[i].selected = true;
                    } else {
                        billingCountryValue.options[i].selected = false;
                    };
                }; 
            } else {
                for (var i = 0; i < billingCountryValue.options.length; i++) {
                    billingCountryValue.options[i].selected = false;
                };
            };
                
            if (organization.shipping_address != null && organization.shipping_address != '') {
                $('#shipping-address-value').prop('value', organization.shipping_address);
            } else {
                $('#shipping-address-value').prop('value', '');
            };
            
            if (organization.shipping_city != null && organization.shipping_city != '') {
                $('#shipping-city-value').prop('value', organization.shipping_city);
            } else {
                $('#shipping-city-value').prop('value', '');
            };
            
            if (organization.shipping_state != null && organization.shipping_state != '') {
                $('#shipping-state-value').prop('value', organization.shipping_state);
            } else {
                $('#shipping-state-value').prop('value', '');
            };

            if (organization.shipping_state != null && organization.shipping_state != '') {
                $('#shipping-state-value').prop('value', organization.shipping_state);
            } else {
                $('#shipping-state-value').prop('value', '');
            };

            if (organization.shipping_postal_code != null && organization.shipping_postal_code != '') {
                $('#shipping-postal-code-value').prop('value', organization.shipping_postal_code);
            } else {
                $('#shipping-postal-code-value').prop('value', '');
            };

            var shippingCountryValue = document.getElementById('shipping-country-value')

            if (organization.shipping_country != null && organization.shipping_country != '') {
                for (var i = 0; i < shippingCountryValue.options.length; i++) {
                    if (shippingCountryValue.options[i].value == organization.shipping_country) {
                        shippingCountryValue.options[i].selected = true;
                    } else {
                        shippingCountryValue.options[i].selected = false;
                    };
                }; 
            } else {
                for (var i = 0; i < shippingCountryValue.options.length; i++) {
                    shippingCountryValue.options[i].selected = false;
                };
            };
            
            if (organization.date_to_remember != null && organization.date_to_remember != '') {
                $('#date-to-remember-value').prop('value', organization.date_to_remember);
            } else {
                $('#date-to-remember-value').prop('value', '');
            };
            
            if (organization.description != null && organization.description != '') {
                $('#description-value').prop('value', organization.description);
            } else {
                $('#description-value').prop('value', '');
            };
                        
            if (organization.tag_list != null && organization.tag_list != '') {
                $('#tag-list-value').prop('value', organization.tag_list);
            } else {
                $('#tag-list-value').prop('value', '');
            };

            var permissionValue = document.getElementById('permission-value')

            if (organization.permission != null && organization.permission != '') {
                for (var i = 0; i < permissionValue.options.length; i++) {
                    if (permissionValue.options[i].value == organization.permission) {
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
            console.error(error);
        }
    });
};