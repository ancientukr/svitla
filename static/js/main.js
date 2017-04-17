
$(window).on( 'load', function() {
        window.scroll(0 , 0);
});

$(document).ready(function(){
        $('.logo').fadeIn(2000);
        $('.mainWrap').fadeIn(2500);
        $('.slider').fadeIn(3500);

        $('#id_type_photo, #id_name, #id_email, #id_date_photo_shooting, #id_location, #id_massage, #id_info_about_my').addClass('form-control')
        $('#id_date_photo_shooting').attr('type','date')
});