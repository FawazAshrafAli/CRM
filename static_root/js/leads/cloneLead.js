function cloneLead(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#clone-lead-form').prop('action', '/leads/clone_lead/' + leadId);

            if (lead.full_name != null && lead.full_name != '') {
                $('#cloning-lead-object').html(lead.full_name);
            } else {
                $('#cloning-lead-object').html('');
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};