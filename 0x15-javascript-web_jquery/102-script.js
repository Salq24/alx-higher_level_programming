$(document).ready(function() {
            $('#btn_translate').click(function() {
                let langCode = $('#language_code').val();
                let apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

                $.get(apiUrl, function(data) {
                    $('#hello').text(data.hello);
                });
            });
        });
