function fetchAndPrintDeal(dealId, dealContentDiv){ 
    $.ajax({
        url: '/deals/detail/' + dealId,
        type: 'GET',
        dataType: 'json',
        success: function(deal) {
            $('.deal-id').each(function() {  
                if (deal.id != null && deal.id != "") {
                    $(this).html(deal.id);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-image').each(function() {  
                if (deal.image != null && deal.image != "") {
                    $(this).prop('src', deal.image);                
                } else {
                    $(this).html('src', "static/assets/img/c-logo.png");
                }
            });
            
            $('.deal-name').each(function (){
                if (deal.full_name != null && deal.full_name != "") {
                    $(this).html(deal.full_name);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-company').each(function (){
                if (deal.company != null && deal.company != "") {
                    $(this).html(deal.company);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-title').each(function (){
                if (deal.title != null && deal.title != "") {
                    $(this).html(deal.title);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-email').each(function (){
                if (deal.email != null && deal.email != "") {
                    $(this).html(deal.email);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-email-opted-out').each(function (){
                if (deal.email_opted_out != null && deal.email_opted_out != "") {
                    $(this).html('True');
                } else {
                    $(this).html('False');
                }
            });

            $('.deal-phone').each(function (){
                if (deal.phone != null && deal.phone != "") {
                    $(this).html(deal.phone);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mobile-phone').each(function (){
                if (deal.mobile_phone != null && deal.mobile_phone != "") {
                    $(this).html(deal.mobile_phone);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-fax').each(function (){
                if (deal.fax != null && deal.fax != "") {
                    $(this).html(deal.fax);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-website').each(function (){
                if (deal.website != null && deal.website != "") {
                    $(this).html(deal.website);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-industry').each(function (){
                if (deal.industry != null && deal.industry != "") {
                    $(this).html(deal.industry);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-number-of-employees').each(function (){
                if (deal.number_of_employees != null && deal.number_of_employees != "") {
                    $(this).html(deal.number_of_employees);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-category').each(function (){
                if (deal.category != null && deal.category != "") {
                    $(this).html(deal.category);
                } else {
                    $(this).html("None");
                }
            });
            
            $('.deal-probability-of-winning').each(function (){
                if (deal.probability_of_winning != null && deal.probability_of_winning != "") {
                    $(this).html(deal.probability_of_winning);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-forecast-close-date').each(function (){
                if (deal.forecast_close_date != null && deal.forecast_close_date != "") {
                    $(this).html(deal.forecast_close_date);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-actual-close-date').each(function (){
                if (deal.actual_close_date != null && deal.actual_close_date != "") {
                    $(this).html(deal.actual_close_date);
                } else {
                    $(this).html("None");
                }
            });
            
            $('.deal-user_responsible').each(function (){
                if (deal.user_responsible != null && deal.user_responsible != "") {
                    $(this).html(deal.user_responsible);
                } else {
                    $(this).html("None");
                }
            });
            

            $('.deal-value').each(function (){
                if (deal.deal_value != null && deal.deal_value != "") {
                    $(this).html(deal.deal_value);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-bid-amount').each(function (){
                if (deal.bid_amount != null && deal.bid_amount != "") {
                    $(this).html(deal.bid_amount);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-bid-type').each(function (){
                if (deal.bid_type != null && deal.bid_type != "") {
                    $(this).html(deal.bid_type);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mailing-address').each(function (){
                if (deal.mailing_address != null && deal.mailing_address != "") {
                    $(this).html(deal.mailing_address);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mailing-city').each(function (){
                if (deal.mailing_city != null && deal.mailing_city != "") {
                    $(this).html(deal.mailing_city);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mailing-state').each(function (){
                if (deal.mailing_state != null && deal.mailing_state != "") {
                    $(this).html(deal.mailing_state);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mailing-postal-code').each(function (){
                if (deal.mailing_postal_code != null && deal.mailing_postal_code != "") {
                    $(this).html(deal.mailing_postal_code);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-mailing-country').each(function (){
                if (deal.mailing_country != null && deal.mailing_country != "") {
                    $(this).html(deal.mailing_country);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-description').each(function (){
                if (deal.description != null && deal.description != "") {
                    $(this).html(deal.description);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-tag-list').each(function (){
                if (deal.tag_list != null && deal.tag_list != "") {
                    $(this).html(deal.tag_list);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-pipeline').each(function (){
                if (deal.pipeline != null && deal.pipeline != "") {
                    $(this).html(deal.pipeline);
                } else {
                    $(this).html("None");
                }
            });
            
            var array = deal.stages              
            if (array != null && array != "") {
                if (array.includes("Prospecting")) {                                
                    $('#deal-stage-prospecting').removeClass("planning")
                } else {
                    $('#deal-stage-prospecting').addClass("planning")
                };                                 

                if (array.includes("Qualification")) {                    
                    $('#deal-stage-qualification').removeClass("planning")
                } else {                    
                    $('#deal-stage-qualification').addClass("planning")
                };

                if (array.includes("Needs Analysis")) {                    
                    $('#deal-stage-needs-analysis').removeClass("planning")                    
                } else {                        
                    $('#deal-stage-needs-analysis').addClass("planning")
                };

                if (array.includes("Proposal")) {                    
                    $('#deal-stage-proposal').removeClass("planning")                    
                } else {                    
                    $('#deal-stage-proposal').addClass("planning")
                };

                if (array.includes("Negotiation")) {                    
                    $('#deal-stage-negotiation').removeClass("planning")
                } else {                    
                    $('#deal-stage-negotiation').addClass("planning")                    
                };

                if (array.includes("Closed Won")) {                    
                    $('#deal-stage-closed-won').removeClass("planning")
                } else {                    
                    $('#deal-stage-closed-won').addClass("planning")                    
                };
            } else {
                $('#deal-stage-prospecting').addClass("planning")
                $('#deal-stage-qualification').addClass("planning")
                $('#deal-stage-needs-analysis').addClass("planning")
                $('#deal-stage-proposal').addClass("planning")
                $('#deal-stage-negotiation').addClass("planning")                    
                $('#deal-stage-closed-won').addClass("planning")                    
            };

            $('.deal-stage').each(function (){
                if (deal.stage != null && deal.stage != "") {
                    $(this).html(deal.stage);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-state').each(function (){
                if (deal.deal_state != null && deal.deal_state != "") {
                    $(this).html(deal.deal_state);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-visibility').each(function (){
                if (deal.visibility != null && deal.visibility != "") {
                    $(this).html(deal.visibility);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-record-owner').each(function (){
                if (deal.record_owner != null && deal.record_owner != "") {
                    $(this).html(deal.record_owner);
                } else {
                    $(this).html("None");
                }
            });
               
            $('.deal-created').each(function (){
                if (deal.created != null && deal.created != "") {
                    $(this).html(deal.created);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-updated').each(function (){
                if (deal.updated != null && deal.updated != "") {
                    $(this).html(deal.updated);
                } else {
                    $(this).html("None");
                }
            });
function printDiv(contentDiv) {
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

                        printWindow.document.write(document.getElementById(contentDiv).innerHTML);
                        printWindow.document.write('</body></html>');
                        printWindow.document.close();
                        printWindow.print();
                        printWindow.close();
                        resolve();
                    }
                };
                printWindow.document.head.appendChild(link);
            });
        };

        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
};