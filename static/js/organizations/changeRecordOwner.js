function changeRecordOwner(organizationId) {
    $.ajax({
        type: 'GET',
        url: '/organizations/detail/' + organizationId,
        dataType: 'json',
        success: function (organization) {
            $('#change-organization-owner-form').prop('action', '/organizations/change_owner/' + organizationId);

            var recordOwnerValue = document.getElementById('record-owner-value')

            if (organization.record_owner != null && organization.record_owner != '') {                
                for (var i = 0; i < recordOwnerValue.options.length; i++) {
                    if (recordOwnerValue.options[i].value == organization.record_owner) {
                        recordOwnerValue.options[i].selected = true;
                    } else {
                        recordOwnerValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < recordOwnerValue.options.length; i++) {
                    recordOwnerValue.options[i].selected = false;
                };
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};