$(document).ready( function() {
    $.ajax(
        {
            url: "/suggestion_json",
            success: function(result) {
                $("#name").text(result.name)
                $("#email").text(result.email)
                $("#message").text(result.message)
            },
        }
    )
})

setTimeout(function(){ 
    location.href = "../"
}, 10000)