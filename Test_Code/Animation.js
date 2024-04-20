$(document).ready(function () {
    $('.swipe-btn').click(function () {
        var action = $(this).data('action');
        var card = $(this).closest('.card');

        if (action === 'reject') {
            card.animate({
                left: '-100%',
                opacity: 0
            }, 300, function () {
                card.remove();
            });
        } else if (action === 'accept') {
            card.animate({
                left: '100%',
                opacity: 0
            }, 300, function () {
                card.remove();
            });
        }
    });
});
