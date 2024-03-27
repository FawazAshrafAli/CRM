function loadOrganizationDetails(organizationId) {
    $.ajax({
        url: '/organizations/detail/' + organizationId,  // Update the URL to match your actual URL
        type: 'GET',
        dataType: 'json',
        success: function(organization) {										
            // Handle the JSON response
            $('.organization-id').each(function() {
                if (organization.id != null && organization.id != ""){
                    $(this).html(organization.id);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-name').each(function() {
                if (organization.name != null && organization.name != ""){
                    $(this).html(organization.name); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-organization').each(function() {
                if (organization.organization != null && organization.organization != ""){
                    $(this).html(organization.organization); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-title').each(function() {
                if (organization.title != null && organization.title != ""){
                    $(this).html(organization.title); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-phone').each(function() {
                if (organization.phone != null && organization.phone != ""){
                    $(this).html(organization.phone); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-fax').each(function() {  
                if (organization.fax != null && organization.fax != ""){                  
                    $(this).html(organization.fax); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-website').each(function() {
                if (organization.website != null && organization.website != ""){
                    $(this).html(organization.website); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-linkedin').each(function() {
                if (organization.linkedin != null && organization.linkedin != ""){
                    $(this).html(organization.linkedin); 
                } else {
                    $(this).html("None");
                }
            });
                        
            $('.organization-facebook').each(function() {
                if (organization.facebook != null && organization.facebook != ""){                    
                    $(this).html(organization.facebook); 
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-twitter').each(function() {
                if (organization.twitter != null && organization.twitter != ""){
                    $(this).html(organization.twitter); 
                } else {
                    $(this).html("None");
                }       
            });
                
            $('.organization-email-domains').each(function() {
                if (organization.email_domains != null && organization.email_domains != ""){
                    $(this).html(organization.email_domains);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-billing-address').each(function() {
                if (organization.billing_address != null && organization.billing_address != ""){
                    $(this).html(organization.billing_address);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-date-to-remember').each(function() {
                if (organization.date_to_remember != null && organization.date_to_remember != ""){
                    $(this).html(organization.date_to_remember);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-description').each(function() {
                if (organization.description != null && organization.description != ""){
                    $(this).html(organization.description);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-tag-list').each(function() {
                if (organization.tag_list != null && organization.tag_list != ""){
                    $(this).html(organization.tag_list);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-shipping-address').each(function() {
                if (organization.shipping_address != null && organization.shipping_address != ""){
                    $(this).html(organization.shipping_address);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-created-at').each(function() {
                if (organization.created != null && organization.created != ""){
                    $(this).html(organization.created);
                } else {
                    $(this).html("None");
                }
            });

            $('.organization-updated-at').each(function() {
                if (organization.updated != null && organization.updated != ""){							
                    $(this).html(organization.updated);
                } else {
                    $(this).html("None");
                }
            });
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
}