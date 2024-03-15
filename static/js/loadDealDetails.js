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
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
};