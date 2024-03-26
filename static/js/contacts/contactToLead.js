function contactToLead(contactId) {
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId,
        dataType: 'json',
        success: function (contact) {
            $('#lead-convertion-form').prop('action', '/contacts/lead_convertion/' + contactId);

            if (contact.full_name != null && contact.full_name != '') {
                $('#converting-contact').html(contact.full_name);
            } else {
                $('#converting-contact').html('');
            };

        },
        error: function (error) {
            console.error(error);
        }
    });
};