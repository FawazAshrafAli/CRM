function editDeal (dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {
            $('#edit-deal-form').prop('action', '/deals/update/'+ deal.id);

            if (deal.name != null && deal.name != '') {
                $('#name-value').prop('value', deal.name);
            } else {
                $('#name-value').prop('value', '');
            };
            
            var companySelect = document.getElementById('company-select');                        
            if (deal.company_id != null && deal.company_id != '') {
                for (var i = 0; i < companySelect.options.length; i++) {
                    if (companySelect.options[i].value == deal.company_id) {
                        companySelect.options[i].selected = true;
                    } else {
                        companySelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < companySelect.options.length; i++) {
                    companySelect.options[i].selected = false;
                };
            };


            var categorySelect = document.getElementById('category-select');
            if (deal.category != null && deal.category != '') {
                for (var i = 0; i < categorySelect.options.length; i++) {
                    if (categorySelect.options[i].value == deal.category) {
                        categorySelect.options[i].selected = true;
                    } else {
                        categorySelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < categorySelect.options.length; i++) {
                    categorySelect.options[i].selected = false;
                };
            };
            
            if (deal.probability_of_winning != null && deal.probability_of_winning != '') {
                $('#probability-of-winning-value').prop('value', deal.probability_of_winning);
            } else {
                $('#probability-of-winning-value').prop('value', '');
            };
            
            if (deal.forecast_close_date != null && deal.forecast_close_date != '') {
                $('#forecast-close-date-value').prop('value', deal.forecast_close_date);
            } else {
                $('#forecast-close-date-value').prop('value', '');
            };
            
            if (deal.actual_close_date != null && deal.actual_close_date != '') {
                $('#actual-close-date-value').prop('value', deal.actual_close_date);
            } else {
                $('#actual-close-date-value').prop('value', '');
            };
            
            var userResponsibleSelect = document.getElementById('user-responsible-select')
            if (deal.user_responsible_id != null && deal.user_responsible_id != '') {
                for  (var i = 0; i < userResponsibleSelect.options.length; i++) {
                    if (userResponsibleSelect.options[i].value == deal.user_responsible_id) {
                        userResponsibleSelect.options[i].selected = true;
                    } else {
                        userResponsibleSelect.options[i].selected = false;
                    };
                }
            } else {
                for  (var i = 0; i < userResponsibleSelect.options.length; i++) {
                    userResponsibleSelect.options[i].selected = false;
                };
            };
            
            var dealValueSelect = document.getElementById('deal-value-select')
            if (deal.deal_value != null && deal.deal_value != '') {
                for  (var i = 0; i < dealValueSelect.options.length; i++) {
                    if (dealValueSelect.options[i].value == deal.deal_value) {
                        dealValueSelect.options[i].selected = true;
                    } else {
                        dealValueSelect.options[i].selected = false;
                    };
                }
            } else {
                for  (var i = 0; i < dealValueSelect.options.length; i++) {
                    dealValueSelect.options[i].selected = false;
                };
            };
            
            if (deal.bid_amount != null && deal.bid_amount != '') {
                $('#bid-amount-value').prop('value', deal.bid_amount);
            } else {
                $('#bid-amount-value').prop('value', '');
            };
            
            var bidTypeSelect = document.getElementById('bid-type-select');
            if (deal.bid_type != null && deal.bid_type != '') {
                for (var i = 0; i < bidTypeSelect.options.length; i++) {
                    if  (bidTypeSelect.options[i].value == deal.bid_type) {
                        bidTypeSelect.options[i].selected = true;
                    } else {
                        bidTypeSelect.options[i].selected = false;
                    };
                };
            }else {
                for (var i = 0; i < bidTypeSelect.options.length; i++) {
                    bidTypeSelect.options[i].selected = false;
                };
            };
            
            if (deal.description != null && deal.description != '') {
                $('#description-value').prop('value', deal.description);
            } else {
                $('#description-value').prop('value', '');
            };
            
            if (deal.tag_list != null && deal.tag_list != '') {
                $('#tag-list-value').prop('value', deal.tag_list);
            } else {
                $('#tag-list-value').prop('value', '');
            };
            
            var pipelineSelect = document.getElementById( 'pipeline-select' );
            if (deal.pipeline != null && deal.pipeline != '') {
                for (var i = 0; i < pipelineSelect.options.length; i++) {
                    if (pipelineSelect.options[i].value == deal.pipeline) {
                        pipelineSelect.options[i].selected = true;
                    } else {
                        pipelineSelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < pipelineSelect.options.length; i++) {
                    pipelineSelect.options[i].selected = false;
                };
            };
                        
            var stageSelect = document.getElementById( 'stage-select' );            
            var array = deal.stages_id;
            if (array != null && array != '') {
                for (var i = 0; i < stageSelect.options.length; i++) {                                        
                    if (array.includes(parseInt(stageSelect.options[i].value))) {
                        stageSelect.options[i].selected = true;
                    } else {
                        stageSelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < stageSelect.options.length; i++) {
                    stageSelect.options[i].selected = false;
                };
            };
            
            var visibilitySelect = document.getElementById( 'visibility-select');
            if (deal.visibility != null && deal.visibility != '') {                
                for (var i = 0; i < visibilitySelect.options.length; i++) {
                    if (visibilitySelect.options[i].value == deal.visibility) {
                        visibilitySelect.options[i].selected = true;
                    } else {
                        visibilitySelect.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < visibilitySelect.options.length; i++) {
                    visibilitySelect.options[i].selected = false;
                };
            };

        },
        error: function (error) {
            console.error('Error: ', error);
        }
    })
}