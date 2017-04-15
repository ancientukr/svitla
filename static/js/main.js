
$(window).on( 'load', function() {
        window.scroll(0 , 0);
});

$(document).ready(function(){
        $('.logo').fadeOut(1);
        $('.mainWrap').fadeOut(1);
        $('.logo').fadeIn(1500);
        $('.mainWrap').fadeIn(1500);



        $('.button_ton').click(function () {
            window.scroll(0, 0, 5000)
        })

        $('#id_type_photo, #id_name, #id_email, #id_date_photo_shooting, #id_location, #id_massage, #id_info_about_my').addClass('form-control')
        $('#id_date_photo_shooting').attr('type','date')
});