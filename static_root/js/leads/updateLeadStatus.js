function updateLeadStatus(leadId, newStatus) {    
    $.ajax({
        type: 'POST',
        url: `/leads/update_lead_status/${leadId}`,
        data: {
            new_status: newStatus,
            // csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function(response) {
            loadLeadDetails(leadId)									            
        },
        error: function(error) {
            console.error('Error updating lead status:', error);            
        }
    });
}