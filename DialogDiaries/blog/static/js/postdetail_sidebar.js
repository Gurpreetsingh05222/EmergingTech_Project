$(document).ready(function(){
    $("#addLike, #addComment").click(function(e){
        e.preventDefault();
        var slug = $('#post').val();
        var isAuthenticated = $("#is_authenticated").val();
        data = {'post_slug': slug };
        if(isAuthenticated == "True"){
            $.ajax({
              type: "POST",
              url: $(this).data('url'),
              data: {
                        content: data,
                        'csrfmiddlewaretoken': $('#token').val()
                    },
              success: function(data, status, xhr) {
                console.log(xhr.getResponseHeader('Location'));
              }
            });
        }
        else{
            window.location.href = "sign-in.html?next=" + $(this).data('url') + '&post='+ slug;
        }
    });
});