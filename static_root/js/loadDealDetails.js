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
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
};