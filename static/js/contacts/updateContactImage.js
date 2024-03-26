var contactImageInput = document.getElementById('contact-image-input');

contactImageInput.addEventListener( 'change', function () {
    var imageUrl = URL.createObjectURL(contactImageInput.files[0]);
    document.getElementById('current-contact-image').innerHTML = contactImageInput.value;
    document.getElementById('current-contact-image').setAttribute('href', imageUrl);
});

function updateContactImage(contactId) {    
    $.ajax({
        type: 'GET',
        url: '/contacts/detail/' + contactId,
        dataType: 'json',
        success: function (contact) {
            $('#contact-image-updation-form').prop('action', '/contacts/update_image/' + contactId)
            if (contact.image != null && contact.image != "") {                
                $('#current-contact-image').html(contact.image);
                $('#current-contact-image').prop('href', contact.image).prop('target', "_blank");
            } else {
                $('#current-contact-image').html('');
                $('#current-contact-image').prop('href', '#').prop('target', '');
            };
        },
        error: function (error) {
            console.log(error);
        }
    });
};