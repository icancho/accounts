$(document).ready(function(){
	$('.sum').bind('click', function(){
		var button = $(this);
		var total = parseInt(button.attr('data-total'));
		var pk = button.attr('data-pk');

		var add = parseInt(prompt("Cuanto quieres sumar"));
		$.ajax({
			url: 'http://127.0.0.1:8000/suma/' + pk,
			type: 'POST',
			data: {
				add: add,
				csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
			},
			success: function(data){
				button.parent().find('.total_expeses').text(data.expenses_now);
				button.attr('data-total', data.expenses_now);
			},
			error: function(){
				alert('bad job');
			}
		});
	});
});