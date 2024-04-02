function deleteOrganization(organizationId) {
    $.ajax({
        type: 'GET',
        url: '/organizations/detail/' + organizationId,
        dataType: 'json',
        success: function (organization) {
            $('#delete-organization-form').prop('action', '/organizations/delete/' + organization.id);

            if (organization.name != null && organization.name != '') {                
                $('#deleting-organization').html(organization.name);
            } else {
                $('#deleting-organization').html('');
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    })
};