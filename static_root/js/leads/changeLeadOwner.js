function changeLeadOwner(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#change-lead-owner-form').prop('action', '/leads/update_owner/' + leadId);

            var recordOwnerValue = document.getElementById('record-owner-value');

            if (lead.record_owner != null && lead.record_owner != '') {                
                for (var i = 0; i < recordOwnerValue.options.length; i++) {
                    if (recordOwnerValue.options[i].value == lead.record_owner) {
                        recordOwnerValue.options[i].selected = true;
                    } else {
                        recordOwnerValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < recordOwnerValue.options.length; i++) {
                    recordOwnerValue.options[i].selected = false;
                }
            };
        }, 
        error: function (error) {
            console.error("Error: ", error)
        }
    })
}