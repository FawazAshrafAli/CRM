function loadLeadDetails(leadId) {	
    $.ajax({
        url: '/leads/detail/' + leadId,  // Update the URL to match your actual URL
        type: 'GET',
        dataType: 'json',
        success: function(lead) {										
            // Handle the JSON response
            $('.lead-id').each(function() {
                if (lead.id != null && lead.id != ""){
                    $(this).html(lead.id);
                } else {
                    $(this).html('None');
                };
            });
            
            $('.lead-full-name').each(function() {
                if (lead.full_name != null && lead.full_name != ""){
                    $(this).html(lead.full_name);
                } else {
                    $(this).html('None');
                };
            });
            
            $('.lead-organization').each(function() {
                if (lead.organization != null && lead.organization != ""){
                    $(this).html(lead.organization); 
                } else {
                    $(this).html('None');
                };
            });
            
            $('.lead-title').each(function() {
                if (lead.title != null && lead.title != ""){
                    $(this).html(lead.title); 
                } else {
                    $(this).html('None');
                };
            });

            $('.lead-status').each(function() {
                if (lead.lead_status != null && lead.lead_status != ""){
                    $(this).html(lead.lead_status);
                    $('#lead-status-' + leadId).html(lead.lead_status);
                } else {
                    $(this).html('None');
                };
            });

            $('.lead-status-indicator').each(function() {								
                if (lead.lead_status != null && lead.lead_status != ""){
                    $(this).prop('value', lead.id);								
                    if (lead.lead_status === $(this).text().trim()) {
                        $(this).addClass('active');
                    } else {
                        $(this).removeClass('active');
                    }
                } else {
                    $(this).removeClass('active');
                }
            });									
            
            if (lead.user_responsible != null && lead.user_responsible != ""){
                $('.lead-user-responsible').each(function() {
                    $(this).html(lead.user_responsible); 
                });
            };

            if (lead.lead_rating != null && lead.lead_rating != ""){
                $('.lead-rating').each(function() {
                    $(this).html(lead.lead_rating); 
                });
            };

            if (lead.email != null && lead.email != ""){                  
                $('.lead-email').each(function() {  
                    $(this).html(lead.email); 
                });
            };	
            var email_opted_out = '' + lead.email_opted_out + ''
            if (email_opted_out != null && email_opted_out != ""){							
                $('.lead-email-opted-out').each(function() {								
                    $(this).html(email_opted_out);																
                });
            };

            if (lead.phone != null && lead.phone != ""){
                $('.lead-phone').each(function() {
                    $(this).html(lead.phone); 
                });
            };							
                        
            if (lead.mobile_phone != null && lead.mobile_phone != ""){                    
                $('.lead-mobile-phone').each(function() {
                    $(this).html(lead.mobile_phone); 
                });
            };								

            if (lead.fax != null && lead.fax != ""){
                $('.lead-fax').each(function() {
                    $(this).html(lead.fax);
                });
            };

            if (lead.website != null && lead.website != ""){
                $('.lead-website').each(function() {
                    $(this).html(lead.website);
                });
            };

            if (lead.industry != null && lead.industry != ""){
                $('.lead-industry').each(function() {
                    $(this).html(lead.industry);
                });
            };

            if (lead.number_of_employees != null && lead.number_of_employees != ""){
                $('.lead-number-of-employees').each(function() {
                    $(this).html(lead.number_of_employees);
                });
            };

            if (lead.lead_source != null && lead.lead_source != ""){
                $('.lead-source').each(function() {
                    $(this).html(lead.lead_source);
                });
            };

            if (lead.mailing_address != null && lead.mailing_address != ""){
                $('.lead-mailing-address').each(function() {
                    $(this).html(lead.mailing_address);
                });
            };

            if (lead.description != null && lead.description != ""){
                $('.lead-description').each(function() {
                    $(this).html(lead.description);
                });
            };

            if (lead.tag_list != null && lead.tag_list != ""){							
                $('.lead-tag-list').each(function() {
                    $(this).html(lead.tag_list);
                });
            };						

            if (lead.permission != null && lead.permission != ""){							
                $('.lead-permission').each(function() {
                    $(this).html(lead.permission);
                });
            };						

            if (lead.created != null && lead.created != ""){							
                $('.lead-created').each(function() {
                    $(this).html(lead.created);
                });
            };

            if (lead.updated != null && lead.updated != ""){							
                $('.lead-updated').each(function() {
                    $(this).html(lead.updated);
                });
            };
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
}