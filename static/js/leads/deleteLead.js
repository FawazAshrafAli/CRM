function deleteLead(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#lead-deletion-form').prop('action', '/leads/delete/' + leadId);

            if (lead.full_name != null && lead.full_name != '') {
                $('#deleting-lead-object').html(lead.full_name);
            } else {
                $('#deleting-lead-object').html('');
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};