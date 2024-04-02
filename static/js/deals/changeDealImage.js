var imageInput = document.getElementById('image-input');

imageInput.addEventListener('change', function () {
    var imageUrl = URL.createObjectURL(imageInput.files[0]);    
    document.getElementById('image-value').innerHTML = imageInput.value
    document.getElementById('image-value').setAttribute('href', imageUrl)
})

function changeDealImage (dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {
            $('#change-deal-image-form').prop('action', '/deals/update_image/' + dealId);            
            if (deal.image != null && deal.image != '') {
                $('#image-value').html(deal.image).prop('href', deal.image);
            } else {
                $('#image-value').html('').prop('href', '#');
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        },
    });
};