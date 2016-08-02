$(window).load(function() {
  $(window).bind('scroll', function() {
         if ($(window).scrollTop() > 100) {
             //$('header').addClass('fixed');
             //$('#category-list').addClass('category-list-fixed');
             $('#cart').addClass('cart-fixed');
         }
         else {
             //$('header').removeClass('fixed');
             //$('#category-list').removeClass('category-list-fixed');
             $('#cart').removeClass('cart-fixed');
         }
    });
});

$(document).ready(function() {
	$('#search-button').click(function () {
		v = $('#search-text').val().trim();
		if(v == '') return false;
		url = $(this).attr('href');
		url = url.replace('00', v);
		window.location = url;
		return false;
	});
	$('#search-text').keypress(function (e) {
		if(e.keyCode == 13) {
			$('#search-button').trigger('click');
			return false;
		}
		return true;
	});
	
	$('.get-product').click(function() {
		return true;
		$.ajaxSetup({async:false});
		var url = $(this).attr('href');
		$.get(url, function( data ) {
			$('#product-detail').html( data );
		});
		$.ajaxSetup({async:true});
		
		l = $(window).width();
        l /= 2;
        l -= 330;
        $('#product-detail').css({left: l + 'px'});
        $('html, body').css({
            'overflow': 'hidden',
            'height': '100%'
        });
        $('#product-detail').fadeIn('slow');
        $('#product-detail-wrapper').show();
        
        $('#product-detail-close').click(function() {
            $('html').css({
                'overflow': 'auto',
                'height': 'auto'
            });
            $('#product-detail').fadeOut('slow');
            $('#product-detail-wrapper').hide();
        });
        bind_controls();
        FB.XFBML.parse();
        return false;
    });
	$('#product-detail-wrapper').click(function () {
		$('#product-detail-close').trigger('click');
	});
	
	$('nav ul li').hover(
		function () {	
			$('ul', this).stop().slideDown(100);
		}, 
		function () {
			$('ul', this).stop().slideUp(100);			
		}
	);
	
	bind_controls();
	reload_cart();
	
});

function reload_cart(){
	if (!$('#cart').length){
        return false;
    }
	$.ajaxSetup({async:false});
	$.get('/tienda/cart/get/', function( data ) {
	//$.get('/cart/get/', function( data ) {
		$('#cart').html( data );
		get_total();
	});
	$.ajaxSetup({async:true});
	
	$('.item a.plus').click(function () {
		url = $(this).attr('href');
		v = $(this).parent().children('input').val();
		if(parseInt(v) + 1 == 100) return false;
		i = $(this).parent().children('input');
		$.get(url , function( data ) {
			if(data == 'true') {
				i.val(parseInt(v) + 1);
				get_total();
			}
			else {
				alert('No hay más stock disponible.');
			}
		});
		return false;
	});
	$('.item a.minus').click(function () {
		url = $(this).attr('href');
		v = $(this).parent().children('input').val();
		if(v - 1 == 0) return false;
		$(this).parent().children('input').val(parseInt(v) - 1)
		$.get(url , function( data ) {
			if(data == 'true') {
				if(data == 'true') get_total();
				else alert('error');
			}
		});
		return false;
	});
	$('.delete').click(function () {
		url = $(this).attr('href');
		$.get(url , function( data ) {
			if(data = 'true') {
				reload_cart();
			}
		});
		return false;
	});	
	$('.cart-quantity-input').keypress(function (e) {
		if(e.keyCode >= 37 && e.keyCode <= 40) return true;
		if(e.keyCode == 8) return true;
		if($(this).val().length == 2) return false;
		if(e.charCode >= 48 && e.charCode <= 57) return true;
		return false;
	});
	$('.cart-quantity-input').keyup(function () {
		v = $(this).val();
		if(v == '') return false;
		url = $(this).attr('data-href');
		url = url.replace('00', v);
		$.get(url , function( data ) {
			if(data == 'true') get_total();
			else {
				alert('No hay más stock disponible.');
				reload_cart();
			}
		});
	});      	
}

function get_total() {
	$.ajaxSetup({async:false});
	$.get('/tienda/cart/total/', function( data ) {
	//$.get('/cart/total/', function( data ) {
		if(data != 'false') $('#cart-total-value').html(data);
	});
	$.ajaxSetup({async:true});
}

function bind_controls() {
	$('.plus').click(function () {
		v = $(this).parent().children('input').val();
		if(v < 99) $(this).parent().children('input').val(parseInt(v) + 1)
		return false;
	});
	$('.minus').click(function () {
		v = $(this).parent().children('input').val();
		if(v > 1) $(this).parent().children('input').val(parseInt(v) - 1)
		return false;
	});
	$('.add').click(function () {
		v = $(this).parent().children('input').val();
		if(v == '') return false;
		url = $(this).attr('href');
		url = url.replace('00', v);
		$.get(url , function( data ) {
			if(data == 'true') reload_cart();
			else alert('No hay más stock disponible.');
		});
		return false;
	});
	$('.quantity-input').keypress(function (e) {
		if(e.keyCode >= 37 && e.keyCode <= 40) return true;
		if(e.keyCode == 8) return true;
		if($(this).val().length == 2) return false;
		if(e.charCode >= 48 && e.charCode <= 57) return true;
		return false;
	});
}
