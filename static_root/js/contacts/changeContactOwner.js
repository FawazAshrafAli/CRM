function changeContactOwner(contactId) {
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId,
        dataType: 'json',
        success: function (contact) {            
            $('#contact-owner-updation-form').prop('action', '/contacts/update_contact_owner/' + contactId);

            var contactOwnerValue = document.getElementById('contact-owner-value');

            if (contact.record_owner != null && contact.record_owner != '') {                                
                for (var i=0; i < contactOwnerValue.options.length; i++) {                                
                    if (contactOwnerValue.options[i].value == contact.record_owner) {                        
                        contactOwnerValue.options[i].selected = true;
                    } else {
                        contactOwnerValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i=0; i < contactOwnerValue.options.length; i++) {
                    contactOwnerValue.options[i].selected = false;
                };
            };
            
        },
        error: function (error) {
            console.log(error);
        }
    });
};