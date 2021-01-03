$(function() {

    // See https://docs.djangoproject.com/en/1.11/ref/csrf/
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#add_url')
        .form({
            keyboardShortcuts: false,
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
                console.log("form error", formErrors, fields);
                $('#url').parent().transition('shake');
                return false;
            }
        })
        .on('submit', function(e) {
            e.preventDefault();
            var $url = $('#url');
            if ($url.prop("disabled") || !$('#add_url').form('is valid')) {
                return;
            }
            $url.prop("disabled", true);
            $url.parent().addClass('loading');
            var enable = function enable() {
                $url.prop("disabled", false);
                $url.parent().removeClass('loading');
            };

            var onError = function onError(errorResponse) {
                console.log("errorResponse", errorResponse);
                message = errorResponse.responseJSON.message
                if (message) {
                    alert(message);
                }
                console.error('Error adding article', errorResponse.responseJSON);
                enable();
                $url.parent().transition('shake');
            };

            $.ajax({
                url: '/links/add',
                method: 'POST',
                data: JSON.stringify({ 'url': $url.val() }),
                dataType: 'json'
            })
                .done(function addArticleSuccess(data, textStatus, jqXHR) {
                    if (data.status == "ok") {
                        $url.val('');
                        $list = $('div.ui.main.container div.ui.items');
                        if ($list.length) {
                            $list.prepend(data.html);
                        }
                        var $icon = $url.parent().find('i.icon');
                        enable();
                        $icon.removeClass('linkify');
                        $icon.addClass('checkmark');
                        setTimeout(function() {
                            $icon.removeClass('checkmark');
                            $icon.addClass('linkify');
                        }, 2000);
                    } else {
                        onError();
                    }
                })
                .fail(function addArticleFail(jqXHR, textStatus, errorThrown) {
                    onError(jqXHR);
                });
        });
});
