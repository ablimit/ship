$(document).ready(function() {
	
	var questionslist;

	$.getJson("localhost:8000/getQuestions",function(displayData)
	{
		questionsList = displayData;
	}	

	$('#nextbtn').click(function () {
		$.each(jsonResult,function(i,fb) {
			var linkText = fb.valueOf();
			$('#showquestion').html(linkText);
		}
	}
}
