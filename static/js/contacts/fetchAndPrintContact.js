function fetchAndPrintContact(contactId, contactDiv) {	
    $.ajax({
        url: '/contacts/detail/' + contactId,  // Update the URL to match your actual URL
        type: 'GET',
        dataType: 'json',
        success: function(contact) {													
            // Handle the JSON response
            $('.contact-id').each(function() {
                if (contact.id != null && contact.id != ""){
                    $(this).html(contact.id);
                } else {
                    $(this).html("None");
                };
            });
            
            $('.contact-full-name').each(function() {
                if (contact.full_name != null && contact.full_name != ""){
                    $(this).html(contact.full_name);
                } else {
                    $(this).html("None");
                };
            });
            
            $('.contact-organization').each(function() {
                if (contact.organization != null && contact.organization != ""){
                    $(this).html(contact.organization); 
                } else {
                    $(this).html("None");
                };
            });
            
            $('.contact-title').each(function() {
                if (contact.title != null && contact.title != ""){
                    $(this).html(contact.title); 
                } else {
                    $(this).html("None");
                };
            });
            
            $('.contact-email').each(function() {  
                if (contact.email != null && contact.email != ""){                  
                    $(this).html(contact.email); 
                } else {
                    $(this).html("None");
                };
            });
            
            $('.contact-email-opted-out').each(function() {
                if (contact.email_opted_out != null && contact.email_opted_out != ""){							
                    if (contact.email_opted_out == true) {
                        $(this).html(true);
                    } else {
                        $(this).html(false);
                    }
                } else {
                    $(this).html(false);
                }
            });

            $('.contact-phone').each(function() {
                if (contact.phone != null && contact.phone != ""){
                    $(this).html(contact.phone); 
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-home-phone').each(function() {
                if (contact.home_phone != null && contact.home_phone != ""){
                    $(this).html(contact.home_phone); 
                } else {
                    $(this).html("None");
                };
            });
                        
            $('.contact-mobile-phone').each(function() {
                if (contact.mobile_phone != null && contact.mobile_phone != ""){                    
                    $(this).html(contact.mobile_phone); 
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-other-phone').each(function() {
                if (contact.other_phone != null && contact.other_phone != ""){
                    $(this).html(contact.other_phone); 
                } else {
                    $(this).html("None");
                };
            });
                
            $('.contact-assistant-phone').each(function() {
                if (contact.assistant_phone != null && contact.assistant_phone != ""){
                    $(this).html(contact.assistant_phone);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-assistant-name').each(function() {
                if (contact.assistant_name != null && contact.assistant_name != ""){
                    $(this).html(contact.assistant_name);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-fax').each(function() {
                if (contact.fax != null && contact.fax != ""){
                    $(this).html(contact.fax);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-linkedin').each(function() {
                if (contact.linkedin != null && contact.linkedin != ""){
                    $(this).html(contact.linkedin);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-facebook').each(function() {
                if (contact.facebook != null && contact.facebook != ""){
                    $(this).html(contact.facebook);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-twitter').each(function() {
                if (contact.twitter != null && contact.twitter != ""){
                    $(this).html(contact.twitter);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-mailing-address').each(function() {
                if (contact.mailing_address != null && contact.mailing_address != ""){
                    $(this).html(contact.mailing_address);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-mailing-country').each(function() {
                if (contact.mailing_country != null && contact.mailing_country != ""){
                    $(this).html(contact.mailing_country);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-other-address').each(function() {
                if (contact.other_address != null && contact.other_address != ""){
                    $(this).html(contact.other_address);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-other-country').each(function() {
                if (contact.other_country != null && contact.other_country != ""){
                    $(this).html(contact.other_country);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-due-date').each(function() {
                if (contact.due_date != null && contact.due_date != ""){							
                    $(this).html(contact.due_date);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-date-of-birth').each(function() {
                if (contact.date_of_birth != null && contact.date_of_birth != ""){							
                    $(this).html(contact.date_of_birth);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-description').each(function() {
                if (contact.description != null && contact.description != ""){							
                    $(this).html(contact.description);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-permission').each(function() {
                if (contact.permission != null && contact.permission != ""){							
                    $(this).html(contact.permission);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-tag-list').each(function() {
                if (contact.tag_list != null && contact.tag_list != ""){							
                    $(this).html(contact.tag_list);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-created').each(function() {
                if (contact.created != null && contact.created != ""){							
                    $(this).html(contact.created);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-updated').each(function() {
                if (contact.updated != null && contact.updated != ""){							
                    $(this).html(contact.updated);
                } else {
                    $(this).html("None");
                };
            });

            $('.contact-owner').each(function() {
                if (contact.record_owner_name != null && contact.record_owner_name != ""){							
                    $(this).html(contact.record_owner_name);
                } else {
                    $(this).html("None");
                };
            });

            var printWindow = window.open('', '_blank');
            printWindow.document.open();
            printWindow.document.write('<html><head><title>Print</title></head><body>');

            // Wait for stylesheets to load
            var stylesheetsLoaded = 0;
            var stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
            stylesheets.forEach(function(stylesheet) {
                var link = document.createElement('link');
                link.rel = 'stylesheet';
                link.href = stylesheet.href;
                link.onload = function() {
                    stylesheetsLoaded++;
                    if (stylesheetsLoaded === stylesheets.length) {
                        // All stylesheets are loaded, write task details to print window
                        printWindow.document.write(document.getElementById(contactDiv).innerHTML);
                        printWindow.document.write('</body></html>');
                        printWindow.document.close();
                        printWindow.print();
                        printWindow.close();
                        resolve();
                    }
                };
                printWindow.document.head.appendChild(link);
            });
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
}