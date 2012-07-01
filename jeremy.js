$(document).ready(function() {
    $("#jeremy")
	.delay(1000)
	.animate( { "height": "400px" },
		  { "duration": 1750,
		    "easing": "easeOutBounce" } )
	.delay(1000)
	.animate( { "width": "426px" },
		  { "duration": 3000,
		    "easing": "easeOutBounce" } );
})
