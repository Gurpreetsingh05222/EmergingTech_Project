$(document).ready(function(){
    $(".isa_error").delay(1000).fadeOut(5000);
    $(".isa_success").delay(1000).fadeOut(5000);
    if( document.getElementsByClassName("validation-error")[0] != null) {
        document.getElementsByClassName("validation-error")[0].innerHTML = '';
    }
    $(".validation-error").hide();
    $(".btn-register").click(function(){
        if($(".first-name-container, .last-name-container, .email-container, .password2-container").is(":visible")==false){
            $(".first-name-container, .last-name-container, .email-container, .password2-container").css({'display':'flex'});
            $(".sign-in-bg").css("height","725px")
        }
        else{
            var error_message = "";
            var firstname = $(".first-name-container input").val();
            var lastname = $(".last-name-container input").val();
            var email = $(".email-container input").val();
            var password2 = $(".password2-container input").val();
            var password1 = $(".password-container input").val();
            var username = $(".user-name-container input").val();
            if(firstname!="" && lastname!="" && email!="" && password1!="" && password2!="" && username!=""){
                if(password2==password1){
                    $(".contact-form").submit();
                }
                else{
                    error_message = "Password does not match!"
                }
            }
            else{
                error_message = "Please fill out the entire form!"
            }
            if(error_message!=""){
                var child = document.createTextNode(error_message);
                document.getElementsByClassName("validation-error")[0].appendChild(child);
                $(".validation-error").show();
                $(".validation-error").delay(1000).fadeOut(5000, function(){
                    document.getElementsByClassName("validation-error")[0].innerHTML = '';
                });

            }

        }

    });

});