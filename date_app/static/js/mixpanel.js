/**
 * Created by GoldenGate on 10/23/14.
 */
$(document).ready(function() {
    $("#login-nav-button").click(function () {
        mixpanel.track("Login Nav Button Clicked");
        console.log("mix")
    });
});