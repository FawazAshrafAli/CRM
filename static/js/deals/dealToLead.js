function dealToLead(dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {
            $('#deal-to-lead-form').prop('action', '/deals/convert_to_lead/' + dealId);

            if (deal.name != null && deal.name != '') {
                $('#converting-deal-object').html(deal.name);
            } else {
                $('#converting-deal-object').html('');
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    })
}