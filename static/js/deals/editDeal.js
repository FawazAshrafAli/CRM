function editDeal (dealId) {
    $.ajax({
        type: 'GET',
        url: '/deals/detail/' + dealId,
        dataType: 'json',
        success: function (deal) {              
            $('#edit-deal-form').prop('action', '/deals/update/'+ deal.id);

            if (deal.prefix != null && deal.prefix != '') {
                $('#prefix-value').prop('value', deal.prefix);
            } else {
                $('#prefix-value').prop('value', '');
            };

            if (deal.first_name != null && deal.first_name != '') {
                $('#first-name-value').prop('value', deal.first_name);
            } else {
                $('#first-name-value').prop('value', '');
            };
            
            if (deal.last_name != null && deal.last_name != '') {
                $('#last-name-value').prop('value', deal.last_name);
            } else {
                $('#last-name-value').prop('value', '');
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

            if (deal.title != null && deal.title != '') {
                $('#title-value').prop('value', deal.title);
            } else {
                $('#title-value').prop('value', '');
            };

            if (deal.email != null && deal.email != '') {
                $('#email-value').prop('value', deal.email);
            } else {
                $('#email-value').prop('value', '');
            };

            if (deal.email_opted_out != null && deal.email_opted_out != '') {
                $('#email-opted-out-value').prop('checked', true);
            } else {
                $('#email-opted-out-value').prop('checked', '');
            };

            if (deal.phone != null && deal.phone != '') {
                $('#phone-value').prop('value', deal.phone);
            } else {
                $('#phone-value').prop('value', '');
            };

            if (deal.mobile_phone != null && deal.mobile_phone != '') {
                $('#mobile-phone-value').prop('value', deal.mobile_phone);
            } else {
                $('#mobile-phone-value').prop('value', '');
            };

            if (deal.fax != null && deal.fax != '') {
                $('#fax-value').prop('value', deal.fax);
            } else {
                $('#fax-value').prop('value', '');
            };

            if (deal.website != null && deal.website != '') {
                $('#website-value').prop('value', deal.website);
            } else {
                $('#website-value').prop('value', '');
            };

            if (deal.industry != null && deal.industry != '') {
                $('#industry-value').prop('value', deal.industry);
            } else {
                $('#industry-value').prop('value', '');
            };

            if (deal.number_of_employees != null && deal.number_of_employees != '') {
                $('#number-of-employees-value').prop('value', deal.number_of_employees);
            } else {
                $('#number-of-employees-value').prop('value', '');
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

            if (deal.mailing_address != null && deal.mailing_address != '') {
                $('#mailing-address-value').prop('value', deal.mailing_address);
            } else {
                $('#mailing-address-value').prop('value', '');
            };

            if (deal.mailing_city != null && deal.mailing_city != '') {
                $('#mailing-city-value').prop('value', deal.mailing_city);
            } else {
                $('#mailing-city-value').prop('value', '');
            };

            if (deal.mailing_state != null && deal.mailing_state != '') {
                $('#mailing-state-value').prop('value', deal.mailing_state);
            } else {
                $('#mailing-state-value').prop('value', '');
            };

            if (deal.mailing_postal_code != null && deal.mailing_postal_code != '') {
                $('#mailing-postal-code-value').prop('value', deal.mailing_postal_code);
            } else {
                $('#mailing-postal-code-value').prop('value', '');
            };
            
            var mailingCountryValue = document.getElementById('mailing-country-value');

            if (deal.mailing_country != null && deal.mailing_country != '') {
                for (var i = 0; i < mailingCountryValue.options.lenght; i++) {
                    if (mailingCountryValue.options[i].value == deal.mailing_country) {
                        mailingCountryValue.options[i].selected = true;
                    } else {
                        mailingCountryValue.options[i].selected = false;
                    };
                };
            } else {
                for (var i = 0; i < mailingCountryValue.options.lenght; i++) {
                    mailingCountryValue.options[i].selected = false;
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