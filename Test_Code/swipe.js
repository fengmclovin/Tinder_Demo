// static/js/main.js
$(document).ready(function() {
    $('.swipe-left').click(function() {
        handleSwipe($(this).closest('.profile-card'), 'left');
    });

    $('.swipe-right').click(function() {
        handleSwipe($(this).closest('.profile-card'), 'right');
    });

    function handleSwipe(profileCard, action) {
        const userId = profileCard.data('user-id');
        fetch(`/swipe/${userId}/${action}/`)
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Handle response (update UI, show next profile, etc.)
                // For example, remove the profile card if swiped right
                if (action === 'right') {
                    profileCard.remove();
                }
            })
            .catch(error => console.error('Error:', error));
    }
});
