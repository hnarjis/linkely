$(function() {
    $('#add_url')
        .form({
            on: 'submit',
            fields: {
                url: {
                    identifier : 'url',
                    rules: [
                        {
                            type : 'regExp[/^http(s?):\/\/.+[.][a-zA-Z]{2,}.*/]',
                            prompt : 'Please enter a url'
                        }
                    ]
                }
            },
            onFailure: function(formErrors, fields) {
                console.log(formErrors, fields);
                $('#url').transition('shake');
                return false;
            }
        });
});
