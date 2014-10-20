/**
 * Created by GoldenGate on 10/19/14.
 */
/**
 * Created by GoldenGate on 10/14/14.
 */
$(document).ready(function() {
dater_id = $('.chat_area').attr('id');
user_id = $('.user').attr('id');
    function loadMessages_template() {
//        console.log("loading");
        $.ajax({
            url: '../../chat_messages_template/'+dater_id,
            type: 'GET',
            success: function (data) {
                $('.message_area').html(data)
            }
        });
    }

    loadMessages_template();
    setInterval(loadMessages_template, 500);

    $(".add_message").on("click", function () {
        content = $('#message_id').val();
        var new_message = {
            message: content,
            sender: user_id,
            recipient: dater_id
        }
        new_message = JSON.stringify(new_message)
        $.ajax({
            url: '../../new_message/',
            type: 'POST',
            dataType: 'json',
            data: new_message,
            success: function (response) {
                $('#message_id').val("");
            }
        });
    });

});
