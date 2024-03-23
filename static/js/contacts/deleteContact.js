function deleteContact(contactId) {    
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId,
        dataType: 'json',
        success: function (contact) {            
            $('#delete-contact-form').prop('action', '/contacts/delete/' + contactId)
            if (contact.full_name != null && contact.full_name != '') {
                $('#deleting-contact').html(contact.full_name);
            } else {
                $('#deleting-contact').html('');
            };
        },
        error: function (error) {
            console.log(error)
        }
    });
}