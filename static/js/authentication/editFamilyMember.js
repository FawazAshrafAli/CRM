function editFamilyMember(memberId) {
    $.ajax({
        type: 'GET',
        url: '/authentication/family_member/' + memberId,
        dataType: 'json',
        success: function (member) {
            $('#member-updation-form').prop('action', '/authentication/edit_family_member/' + memberId)

            if (member.name != null || member.name != '') {
                $('#name-value').prop('value', member.name)
            } else {
                $('#name-value').prop('value', '')
            };

            if (member.relationship != null || member.relationship != '') {
                $('#relationship-value').prop('value', member.relationship)
            } else {
                $('#relationship-value').prop('value', '')
            };

            if (member.dob != null || member.dob != '') {
                $('#dob-value').prop('value', member.dob)
            } else {
                $('#dob-value').prop('value', '')
            };

            if (member.phone != null || member.phone != '') {
                $('#phone-value').prop('value', member.phone)
            } else {
                $('#phone-value').prop('value', '')
            };
        },
        error: function (error) {
            console.error('Error: ', error);
        }
    });
};