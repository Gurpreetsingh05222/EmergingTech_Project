$(document).ready(function(){
    $("#addLike, #addComment").click(function(e){
        e.preventDefault();
        var slug = $('#post').val();
        var isAuthenticated = $("#is_authenticated").val();
        if(isAuthenticated == "True"){
            $.ajax({
              type: "POST",
              url: $(this).data('url') + '?post=' + slug,
              data: {
                        content: '',
                        'csrfmiddlewaretoken': $('#token').val()
                    },
              success: function(data) {
                $("#likes").text(data.total_likes);
                $("#comments").text(data.total_comments);
              }
            });
        }
        else{
            window.location.href = "sign-in.html?next=" + $(this).data('url') + '&post='+ slug;
        }
    });
});