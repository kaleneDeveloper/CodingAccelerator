$(document).ready(function (){
    // Open Modal
    $('#openModal').click(function() {
        $('#modalToOpen').css(
            {
                'display': 'block'
            }
        );
    });

    // Close Modal
    $('#closeModal').click(function() {
        $('#modalToOpen').css(
            {
                'display': 'none'
            }
        );
    });
    $('#closeModalCancel').click(function() {
        $('#modalToOpen').css(
            {
                'display': 'none'
            }
        );
    });

    // send mail with ajax
    $('#sendEmail').click(function(e){
		e.preventDefault();
		var data = {
			email: $('#email').val(),
            name: $('#name').val(),
            subject: $('#subject').val(),
			message: $('#message').val()
		};
		$.ajax({
			url: "mail.php",
			type: 'POST',
			data: data,
			success: function(data) {
				$('#js_alert_success').css({'display' : 'block'});
				setTimeout(function(){
					$('#js_alert_success').css({'display' : 'none'});
					$('#email').val("");
                    $('#name').val("");
                    $('#subject').val("");
					$('#message').val("")
				}, 3000);
			},
			error: function(data) {
				$('#js_alert_danger').css({'display' : 'block'});
				setTimeout(function(){
					$('#js_alert_danger').css({'display' : 'none'});
					$('#email').val("");
                    $('#name').val("");
                    $('#subject').val("");
					$('#message').val("")
				}, 3000);
			}
		});
	});
});
