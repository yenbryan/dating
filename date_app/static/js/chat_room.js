/**
 * Created by GoldenGate on 10/19/14.
 */
/**
 * Created by GoldenGate on 10/14/14.
 */
$(document).ready(function() {
dater_id = $('.chat_area').attr('id');
user_id = $('.user').attr('id');
    function loadMessages() {
//        console.log("loading");
        $.ajax({
            url: '../../chat_messages/'+dater_id,
            type: 'GET',
            success: function (data) {
                var res_str ="";
                for(var i=0; i < data.length; i++){
                 res_str += data[i].fields.message + "<br>";
                }
                $('.message_area').html(res_str);
            }
        });
    }

    loadMessages();
    setInterval(loadMessages, 500);

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

//
//$.ajax({
//    url: '/new_pokemon/',
//    type: 'POST',
//    dataType: 'json',
//    data: pokemonData,
//    success: function(response) {
//    },
//    error: function(response) {
//    }