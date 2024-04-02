function deleteDeal (dealId) {    
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId, 
        dataType: 'json',
        success: function (deal) {
            $('#delete-deal-form').prop('action', '/deals/delete/' + dealId);

            if (deal.name != null && deal.name != '') {                
                $('#deleting-deal-object').html(deal.name);
            } else {
                $('#deleting-deal-object').html('');
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};