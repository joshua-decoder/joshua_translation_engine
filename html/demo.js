// Submit the form when pressing enter in the translation box 
$('#sourceTxt').keypress(function (e) {
    if (e.which == 13) {
        translate($("#sourceTxt").val(), record_results);
        return false;
    }
});

// $('#add_weight').click(function() {
//     var html = "<div class=\"input-group\">
//                     <span class=\"input-group-addon\" id=\"label-lm\"></span>
//                     <input type="text" class=\"form-control\" value=\"1.0\" size=\"8\" id=\"lm_weight\"
//                            aria-describedby="label-lm" />
//                   </div>";
//     $("#feature_weights").append(html);
// });


// Change the LM weight
$('#lm_weight').keypress(function (e) {
    if (e.which == 13) {
        var message = "@set_weight lm_0 " + $("#lm_weight").val();
        translate(message);
        return false;
    }
});

// Writes the translation results in the output box
function record_results(data, status) {
    result = "<ul class=\"list-group\">";
    $(data.data.translations[0].raw_nbest).each(function(i, item) {
        // result += item.totalScore + " " + item.hyp + "<br/>\n";
        result += "<li class=\"list-group-item\"><span class=\"badge\">" + item.totalScore
            + "</span>" + item.hyp + "</li>";
    });
    result += "</ul>";
    $("#output").html(result);
};

// Displays an error message in the output box
function failure(msg) {
    $("#output").html("<div class='alert alert-danger'>" + msg + "</div>");
};

// Query the Joshua server
function translate(text, success_func) {
    var url = "http://" + $("#server_host").val() + ":" + $("#server_port").val() + "/";
    var request = $.ajax({
        dataType: 'json',
        url: url,
        data: { "q": text },
        success: success_func,
    });

    request.fail(function(jqXHR, textStatus) {
        failure(textStatus);
    });
};
