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
                    if (lead.lead_status == "Not Contacted") {                        
                        $('#not-contacted-status').addClass('active');                        
                    } else {
                        $('#not-contacted-status').removeClass('active');                        
                    }
                    if (lead.lead_status == "Attempted Contact") {
                        $('#attempted-contact-status').addClass('active');
                    } else {
                        $('#attempted-contact-status').removeClass('active');
                    }
                    if (lead.lead_status == "Contacted") {
                        $('#contacted-status').addClass('active');
                    } else {
                        $('#contacted-status').removeClass('active');
                    }
                    if (lead.lead_status == "Converted") {
                        $('#converted-status').addClass('active');
                    } else {
                        $('#converted-status').removeClass('active');
                    }
                }              
            });
            
            $('.lead-user-responsible').each(function() {
                if (lead.user_responsible != null && lead.user_responsible != ""){
                    $(this).html(lead.user_responsible); 
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-rating').each(function() {
                if (lead.lead_rating != null && lead.lead_rating != ""){
                    $(this).html(lead.lead_rating); 
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-email').each(function() {  
                if (lead.email != null && lead.email != ""){                  
                    $(this).html(lead.email); 
                } else {
                    $(this).html('None'); 
                };
            });
            
            $('.lead-email-opted-out').each(function() {								
                if (lead.email_opted_out != null && lead.email_opted_out != ""){							
                    $(this).html('Yes');
                } else {
                    $(this).html('No');
                };
            });

            $('.lead-phone').each(function() {
                if (lead.phone != null && lead.phone != ""){
                    $(this).html(lead.phone); 
                } else {
                    $(this).html('None'); 
                };
            });
                        
            $('.lead-mobile-phone').each(function() {
                if (lead.mobile_phone != null && lead.mobile_phone != ""){                    
                    $(this).html(lead.mobile_phone); 
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-fax').each(function() {
                if (lead.fax != null && lead.fax != ""){
                    $(this).html(lead.fax);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-website').each(function() {
                if (lead.website != null && lead.website != ""){
                    $(this).html(lead.website);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-industry').each(function() {
                if (lead.industry != null && lead.industry != ""){
                    $(this).html(lead.industry);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-number-of-employees').each(function() {
                if (lead.number_of_employees != null && lead.number_of_employees != ""){
                    $(this).html(lead.number_of_employees);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-source').each(function() {
                if (lead.lead_source != null && lead.lead_source != ""){
                    $(this).html(lead.lead_source);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-mailing-address').each(function() {
                if (lead.mailing_address != null && lead.mailing_address != ""){
                    $(this).html(lead.mailing_address);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-description').each(function() {
                if (lead.description != null && lead.description != ""){
                    $(this).html(lead.description);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-tag-list').each(function() {
                if (lead.tag_list != null && lead.tag_list != ""){							
                    $(this).html(lead.tag_list);
                } else {
                    $(this).html('None'); 
                };						
            });

            $('.lead-permission').each(function() {
                if (lead.permission != null && lead.permission != ""){							
                    $(this).html(lead.permission);
                } else {
                    $(this).html('None'); 
                };						
            });

            $('.lead-created').each(function() {
                if (lead.created != null && lead.created != ""){							
                    $(this).html(lead.created);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-updated').each(function() {
                if (lead.updated != null && lead.updated != ""){							
                    $(this).html(lead.updated);
                } else {
                    $(this).html('None'); 
                };
            });

            $('.lead-owner').each(function() {
                if (lead.lead_owner != null && lead.lead_owner != ""){							
                    $(this).html(lead.lead_owner);
                } else {
                    $(this).html('None'); 
                };
            });
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}