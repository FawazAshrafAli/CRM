function cloneContact(contactId) {    
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId,
        dataType: 'json',
        success: function (contact) {
            $('#clone-contact').prop('href', '/contacts/clone/' + contactId);
            if (contact.full_name != null && contact.full_name != '') {                
                $('#cloning-contact-object').html(contact.full_name);
            } else {
                $('#cloning-contact-object').html('');
            }
        }, 
        error: function (error) {
            console.log(error);
        }
    });
};