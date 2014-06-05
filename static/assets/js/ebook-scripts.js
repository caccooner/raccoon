
jQuery(document).ready(function() {

    $("#backtotop").hide();

    $(window).scroll(function () {
		if ($(this).scrollTop() > 500) {
			$('#backtotop').fadeIn();
		} else {
			$('#backtotop').fadeOut();
		}
	});

	// scroll body to 0px on click
	$('#backtotop a').click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 800);
		return false;
	});

    $('.menu a.item').smoothScroll();


        // alias
        semantic_handler = {
            activate: function () {
                if (!$(this).hasClass('dropdown')) {
                    $(this).addClass('active').closest('.ui.menu').find('.item').not($(this)).removeClass('active');
                }
            }
        }
        ;
    $('.container .menu .dropdown').dropdown({
            on: 'hover'
        });
    $('.menu a.item, .menu .link.item').on('click', semantic_handler.activate)
    ;
    /*
        Product showcase background
    */
    $('.product-showcase').backstretch('static/assets/img/backgrounds/1-.jpg');

    /*
        Gallery
    */
    $('.gallery-images .img-wrapper').hover(
        function() {
            $(this).find('.img-background').fadeIn('fast');
        },
        function() {
            $(this).find('.img-background').fadeOut('fast');
        }
    );

    /*
        Gallery prettyPhoto
    */
    $(".gallery-images a[rel^='prettyPhoto']").prettyPhoto({social_tools: false});

    /*
        Show latest tweet

    $(".show-tweet").tweet({
        username: "anli_zaimi",
        join_text: "auto",
        count: 1,
        loading_text: "loading tweet...",
        template: "{text} {time}"
    });
*/
    /*
        Subscription form
    */
    $('form.subscribe').submit(function() {
        var postdata = $('form.subscribe').serialize();
        $.ajax({
            type: 'POST',
            url: 'assets/subscribe.php',
            data: postdata,
            dataType: 'json',
            success: function(json) {
                if(json.valid == 0) {
                    $('form.subscribe input').css('border', '1px solid #f16f35');
                }
                else {
                    var form_height = $('form.subscribe').height();
                    $('form.subscribe input').css('border', '1px solid #fff');
                    $('form.subscribe').hide();
                    $('.product-description').append('<p style="height: ' + form_height + 'px">' + json.message + '</p>');
                }
            }
        });
        return false;
    });

    /*
        Contact form
    */
    $('.contact-us form').submit(function() {
        $('.contact-us form .name').css('border-top', '0');
        $('.contact-us form .email').css('border-top', '0');
        $('.contact-us form textarea').css('border-top', '0');
        var postdata = $('.contact-us form').serialize();
        $.ajax({
            type: 'POST',
            url: 'assets/contact.php',
            data: postdata,
            dataType: 'json',
            success: function(json) {
                if(json.nameMessage != '') {
                    $('.contact-us form .name').css('border-top', '1px solid #518d8a');
                }
                if(json.emailMessage != '') {
                    $('.contact-us form .email').css('border-top', '1px solid #518d8a');
                }
                if(json.messageMessage != '') {
                    $('.contact-us form textarea').css('border-top', '1px solid #518d8a');
                }
                if(json.nameMessage == '' && json.emailMessage == '' && json.messageMessage == '') {
                    $('.contact-us form').fadeOut('fast', function() {
                        $('.contact-us').append('<p>Thanks for contacting us! We will get back to you very soon.</p>');
                    });
                }
            }
        });
        return false;
    });

    $(window).on('scroll',function(){


    })

});


