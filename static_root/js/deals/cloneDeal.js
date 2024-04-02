function cloneDeal (dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {
            $('#clone-deal-form').prop('action', '/deals/clone_deal/' + dealId);

            if (deal.name != null && deal.name != '') {
                $('#cloning-deal-object').html(deal.name);
            } else {
                $('#cloning-deal-object').html('');
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        },
    });
};