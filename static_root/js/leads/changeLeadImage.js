var imageInput = document.getElementById('image-input');

imageInput.addEventListener('change', function () {    
    var imageUrl = URL.createObjectURL(imageInput.files[0]);
    document.getElementById('image-value').innerHTML = imageInput.value;
    document.getElementById('image-value').setAttribute('href', imageUrl);
});

function changeLeadImage(leadId) {
    $.ajax({
        type: 'GET',
        url: '/leads/detail/' + leadId,
        dataType: 'json',
        success: function (lead) {
            $('#change-lead-image-form').prop('action', '/leads/update_image/' + leadId);

            if (lead.image != null && lead.image != '') {
                $('#image-value').html(lead.image).prop('href', lead.image)
            } else {
                $('#image-value').html('').prop('href', '#')
            };

        },
        error: function (error) {
            console.error('Error: ', error)
        }
    })
}