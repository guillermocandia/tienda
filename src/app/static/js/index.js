$(document).ready(function() {
	$.ajaxSetup({async:false});
	//$.getJSON('http://localhost:10001/util/slide/', function( json ) {
	$.getJSON('http://tienda.ejemplo.com/tienda/util/slide/', function( json ) {
		$.each(json, function(k, v) {
			$('#slide').append('<li>'
					+ '<div class="product-section">'
					+ '<a href="' + v['fields']['enlace'] + '">' 
					+ '<img width="1000" height="400" src="http://static.ejemplo.com/' + v['fields']['file'] 
					+ '" title="' + v['fields']['mensaje'] + '" />' 
					+ '</a>'
					+ '</div>'
					+ '</li>');
		});
	});
	
	//$.get('http://localhost:10001/po/', function( data ) {
	$.get('http://tienda.ejemplo.com/tienda/po/', function( data ) {
		$('#po').prepend( data );
	});
	
	$('#slide').bxSlider({
		width: 1000,
		mode: 'horizontal',  
        auto: true,
        ease: 'ease',
        pager: false,
        controls: true,
        speed: 500,
        pause: 5000,
        captions: true
	});
});