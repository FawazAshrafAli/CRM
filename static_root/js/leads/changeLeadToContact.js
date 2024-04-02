function changeLeadToContact (leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#lead-to-contact-form').prop('action', '/leads/covert_to_contact/' + leadId);

            if (lead.full_name != null && lead.full_name != '') {
                $('#converting-lead-object').html(lead.full_name);
            } else {
                $('#converting-lead-object').html(' ');
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    })
}