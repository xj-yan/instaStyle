
function error_cb(error) {
    console.log(error);
}

/*
 *
 *    Likes
 *
 */

function create_like(success_cb, error_cb) {
    var post_pk = $(this).siblings('.hidden-data').find('.post-pk').text();
    console.log(post_pk);

    $.ajax({
        type: "POST",
        url: '/like',
        data: {
            post_pk: post_pk
        },
        success: function(data) { success_cb(data); },
        error: function(error) { error_cb(error); }
    });
}
  
function like_update_view(data) {
    console.log(data);

    // toggle heart
    var $hiddenData = $('.hidden-data.' + data.post_pk);
    if (data.result) {
      $hiddenData.siblings('.submit-like').removeClass('fa-heart-o').addClass('fa-heart');
    } else {
      $hiddenData.siblings('.submit-like').removeClass('fa-heart').addClass('fa-heart-o');
    }
  
    // update like count
    var difference = data.result ? 1 : -1;
    var $post = $('.view-update.' + data.post_pk);
    var $likes = $post.find('.likes');
    var likes = parseInt($likes.text());
    likes = likes + difference;
  
    console.log('likes', likes);
  
    if (likes == null || isNaN(likes)) {
      $likes.text('1 like');
    } else if (likes === 0) {
      $likes.text('');
    } else if (likes === 1) {
      $likes.text('1 like');
    } else {
      $likes.text(likes + ' likes');
    }
}
 
$('.submit-like').on('click', function() {
    create_like.call(this, like_update_view, error_cb);
});
