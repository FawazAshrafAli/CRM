var organizationImageInput = document.getElementById('organization-image-input');

organizationImageInput.addEventListener('change', function () {
    var imageUrl = URL.createObjectURL(organizationImageInput.files[0]);
    document.getElementById('organization-image-value').innerHTML = organizationImageInput.value;
    document.getElementById('organization-image-value').setAttribute('href', imageUrl);
})

function changeOrganizationImage(organizationId) {    
    $.ajax({
        type: 'GET',
        url: '/organizations/detail/' + organizationId,
        dataType: 'json',
        success: function (organization) {
            $('#change-organization-image').prop('action', '/organizations/change_image/' + organizationId);

            if (organization.image != null && organization.image != '') {                
                $('#organization-image-value').html(organization.image).prop('href', organization.image).prop('target', '_blank');                
            } else {
                $('#organization-image-value').html('').prop('href', '#').prop('target', '');                
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        },
    });
}