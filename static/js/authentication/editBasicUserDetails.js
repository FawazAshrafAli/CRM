var profileImage = document.getElementById('profile-image')

profileImage.addEventListener('change', function() {
    if (profileImage.files[0] != null && profileImage.files[0] != '') {
        imageUrl = URL.createObjectURL(profileImage.files[0]);
        document.getElementById('profile-image-value').innerHTML = profileImage.value;
        document.getElementById('profile-image-value').setAttribute('href', imageUrl);
    } else {
        document.getElementById('profile-image-value').innerHTML = '';
        document.getElementById('profile-image-value').setAttribute('href', '#');
    }
});