function changeLeadToDeal(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#lead-to-deal-form').prop('action', '/leads/covert_to_deal/' + leadId);

            if (lead.full_name != null && lead.full_name != '') {
                $('#converting-lead-to-deal-object').html(lead.full_name);                
            } else {
                $('#converting-lead-to-deal-object').html('');
            };
        },
        error: function (error) {
            console.log('Error: ', error);
        },
    });
};