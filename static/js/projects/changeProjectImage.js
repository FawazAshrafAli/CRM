var imageInput = document.getElementById('image-input');

imageInput.addEventListener('change', function () {
    var imageUrl = URL.createObjectURL(imageInput.files[0]);
    document.getElementById('image-value').innerHTML = imageInput.value;
    document.getElementById('image-input').setAttribute('href',  imageUrl);
});

function changeProjectImage(projectId) {
    $.ajax({
        type: 'GET',
        url: '/projects/detail/' + projectId,
        dataType: 'json',
        success: function (project) {
            $('#change_project_image_form').prop('action', '/projects/update_image/' + projectId);

            if (project.image != null && project.image != '') {
                $('#image-value').html(project.image).prop('href', project.image)
            } else {
                $('#image-value').html('').prop('href', '#')
            };
        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
};