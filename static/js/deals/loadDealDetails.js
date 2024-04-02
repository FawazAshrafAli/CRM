function loadDealDetails(dealId){        
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

            $('.deal-name').each(function (){
                if (deal.name != null && deal.name != "") {
                    $(this).html(deal.name);
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

            $('.deal-company-title').each(function (){
                if (deal.company_title != null && deal.company_title != "") {
                    $(this).html(deal.company_title);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-company-phone').each(function (){
                if (deal.company_phone != null && deal.company_phone != "") {
                    $(this).html(deal.company_phone);
                } else {
                    $(this).html("None");
                }
            });

            $('.deal-company-email').each(function (){
                if (deal.company_email != null && deal.company_email != "") {
                    $(this).html(deal.company_email);
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

            $('.deal-visibility').each(function (){
                if (deal.visibility != null && deal.visibility != "") {
                    $(this).html(deal.visibility);
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
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
};