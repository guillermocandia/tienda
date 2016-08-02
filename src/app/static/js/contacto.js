function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function bindform() {
	$('#contacto-form form').submit(function () {
//		var csrftoken = getCookie('csrftoken');
//		//var csrftoken = $('#contacto-form form input[name="csrfmiddlewaretoken"]').val();
//		alert(csrftoken);
//		$.ajaxSetup({
//		    beforeSend: function (xhr) {
//		    	xhr.setRequestHeader("X-CSRFToken", csrftoken );   
//		    }
//		}); 
		var form = $('#contacto-form form').serialize();
		
		$.post( $('#contacto-form form').attr('action'), form, function(data) {
			$('#contacto-form').html( data );
			bindform();
		});
		return false;
	});
}

$(document).ready(function() {
	$.ajaxSetup({async:false});
	//$.get('http://localhost:10001/contacto/', function( data ) {
	$.get('http://tienda.ejemplo.com/tienda/contacto/', function( data ) {
		$('#contacto-form').html( data );
	});
	$.ajaxSetup({async:true});
	bindform();
});