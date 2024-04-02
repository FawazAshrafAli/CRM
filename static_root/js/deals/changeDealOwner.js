function changeDealOwner (dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {
            $('#change-deal-owner-form').prop('action', '/deals/update_owner/' + dealId);

            var recordOwnerSelect = document.getElementById('record-owner-select');
                        
            if (deal.record_owner_id != null && deal.record_owner_id != '') {
                for (var i = 0; i < recordOwnerSelect.options.length; i++) {
                    if (recordOwnerSelect.options[i].value == deal.record_owner_id) {
                        recordOwnerSelect.options[i].selected = true;
                    } else {
                        recordOwnerSelect.options[i].selected = false;
                    };
                }
            } else {
                for (var i = 0; i < recordOwnerSelect.options.length; i++) {
                    recordOwnerSelect.options[i].selected = false;
                };
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        },
    });
};