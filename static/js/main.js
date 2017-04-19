
$(window).on( 'load', function() {
        window.scroll(0 , 0);
});

$(document).ready(function(){
        $('.logo').fadeIn(2000);
        $('.mainWrap').fadeIn(2500);
        $('.slider').fadeIn(3500);

        $('#id_type_photo, #id_name, #id_email, #id_date_photo_shooting, #id_location, #id_massage, #id_info_about_my, #id_social').addClass('form-control')
        $('#id_date_photo_shooting').attr('type','date')

        $(".animation-photo").boxLoader({
	    direction:"y",
	    position: "50%",
	    effect: "fadeIn",
	    duration: "3s",
	    windowarea: "100%"
});
	    $(".quote").boxLoader({
	    direction:"y",
	    position: "50%",
	    effect: "fadeIn",
	    duration: "2s",
	    windowarea: "100%"
});
});