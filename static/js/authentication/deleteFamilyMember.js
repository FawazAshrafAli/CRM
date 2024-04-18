function deleteFamilyMember(memberId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/family_member/' + memberId,
        dataType: 'json',
        success: function (member) {
            $('#member-deletion-form').prop('action', '/authentication/delete_family_member/' + memberId);

            if (member.name != null && member.name != '') {
                $('#deletion-family-object').html(member.name);
            } else {
                $('#deletion-family-object').html('');
            };
        }
    });
};