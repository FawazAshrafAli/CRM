function loadDealDetails(dealId){
    $.ajax({
        url: '/deals/detail/' + dealId,
        type: 'GET',
        dataType: 'json',
        success: function(deal) {						
            if (deal.id != null && deal.id != "") {
                $('.deal-id').each(function() {  
                    $(this).html(deal.id);
                });
            };

            if (deal.name != null && deal.name != "") {
                $('.deal-name').each(function (){
                    $(this).html(deal.name);
                });
            };

            if (deal.company != null && deal.company != "") {
                $('.deal-company').each(function (){
                    $(this).html(deal.company);
                });
            };

            if (deal.category != null && deal.category != "") {
                $('.deal-category').each(function (){
                    $(this).html(deal.category);
                });
            };

            if (deal.probability_of_winning != null && deal.probability_of_winning != "") {
                $('.deal-probability-of-winning').each(function (){
                    $(this).html(deal.probability_of_winning);
                });
            };

            if (deal.forecast_close_date != null && deal.forecast_close_date != "") {
                $('.deal-forecast-close-date').each(function (){
                    $(this).html(deal.forecast_close_date);
                });
            };

            if (deal.actual_close_date != null && deal.actual_close_date != "") {
                $('.deal-actual-close-date').each(function (){
                    $(this).html(deal.actual_close_date);
                });
            };

            if (deal.user_responsible != null && deal.user_responsible != "") {
                $('.deal-user_responsible').each(function (){
                    $(this).html(deal.user_responsible);
                });
            };
            

            if (deal.deal_value != null && deal.deal_value != "") {
                $('.deal-value').each(function (){
                    $(this).html(deal.deal_value);
                });
            };

            if (deal.bid_amount != null && deal.bid_amount != "") {
                $('.deal-bid-amount').each(function (){
                    $(this).html(deal.bid_amount);
                });
            };

            if (deal.bid_type != null && deal.bid_type != "") {
                $('.deal-bid-type').each(function (){
                    $(this).html(deal.bid_type);
                });
            };

            if (deal.description != null && deal.description != "") {
                $('.deal-description').each(function (){
                    $(this).html(deal.description);
                });
            };

            if (deal.tag_list != null && deal.tag_list != "") {
                $('.deal-tag-list').each(function (){
                    $(this).html(deal.tag_list);
                });
            };

            if (deal.pipeline != null && deal.pipeline != "") {
                $('.deal-pipeline').each(function (){
                    $(this).html(deal.pipeline);
                });
            };

            if (deal.stages != null && deal.stages != "") {                                        
                var array = deal.stages
                if (!array.includes("Prospecting")) {                                
                    $('.deal-stage-prospecting').each(function (){ 
                        $(this).addClass("planning")
                    })                
                } else {
                    $('.deal-stage-prospecting').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }

                if (!array.includes("Qualification")) {                    
                    $('.deal-stage-qualification').each(function (){                                         
                        $(this).addClass("planning")
                    })
                } else {
                    $('.deal-stage-qualification').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }

                if (!array.includes("Needs Analysis")) {                    
                    $('.deal-stage-needs-analysis').each(function (){
                        $(this).addClass("planning")
                    })
                } else {
                    $('.deal-stage-needs-analysis').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }

                if (!array.includes("Proposal")) {                    
                    $('.deal-stage-proposal').each(function (){
                        $(this).addClass("planning")
                    })
                } else {
                    $('.deal-stage-proposal').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }

                if (!array.includes("Negotiation")) {                    
                    $('.deal-stage-negotiation').each(function (){
                        $(this).addClass("planning")
                    })
                } else {
                    $('.deal-stage-negotiation').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }

                if (!array.includes("Closed Won")) {                    
                    $('.deal-stage-closed-won').each(function (){
                        $(this).addClass("planning")
                    })
                } else {
                    $('.deal-stage-closed-won').each(function (){ 
                        $(this).removeClass("planning")
                    })
                }
            };

            if (deal.stage != null && deal.stage != "") {
                $('.deal-stage').each(function (){
                    $(this).html(deal.stage);
                });
            };

            if (deal.visibility != null && deal.visibility != "") {
                $('.deal-visibility').each(function (){
                    $(this).html(deal.visibility);
                });
            };

            if (deal.updated != null && deal.updated != "") {
                $('.deal-updated').each(function (){
                    $(this).html(deal.updated);
                });
            };
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
};