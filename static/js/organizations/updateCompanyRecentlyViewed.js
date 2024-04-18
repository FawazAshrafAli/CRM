function updateCompanyRecentlyViewed (organizationId) {
    $.ajax({
        type: 'GET',
        url: '/organizations/update_recently_viewed/' + organizationId,
        dataType: 'json',
        success: function (data) {
            console.log(data.message, 'Recently Viewed Company Updated')
        },
        error: function (error) {
            console.error('Error: ', error);
        },
    });
};