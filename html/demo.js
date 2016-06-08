// Submit the form when pressing enter in the translation box 
$('#sourceTxt').keypress(function (e) {
    if (e.which == 13 && e.metaKey) {
        translate($("#sourceTxt").val() + "\n", record_results_paragraph);
        return false;
    }
});

/**
 * Adds a rule to the custom grammar housed in the MT system.
 */
$('#add_rule').click(function() {
    var phrasePair = $("#addPhrase").val();
    var tokens = phrasePair.split(" ||| ");
    var sourcePhrase = tokens[0];
    var targetPhrase = tokens[1];
    if (! targetPhrase) {
       alert("phrase pair format must be 'source phrase ||| target phrase'");
       return false;
    } 
    var message = "add_rule " + sourcePhrase + " ,,, " + targetPhrase;
    sendMeta(message);
    sendMeta("list_rules");
    return false;
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
        var message = "| set_weight lm_0 " + $("#lm_weight").val() + " |";
        translate(message);
        return false;
    }
});

// Writes the translation results in the output box
function record_results(data, status) {
    result = "<ul class=\"list-group\">";
    // $(data.data.translations[0].raw_nbest).each(function(i, item) {
    //     // result += item.totalScore + " " + item.hyp + "<br/>\n";
    //     result += "<li class=\"list-group-item\"><span class=\"badge\">" + item.totalScore
    //         + "</span>" + item.hyp + "</li>";
    // });
    $(data.data.translations).each(function(i, item) {
        // result += item.totalScore + " " + item.hyp + "<br/>\n";
        result += "<li class=\"list-group-item\"><span class=\"badge\">" + item.raw_nbest[0].totalScore
            + "</span>" + item.translatedText + "</li>";
    });

    result += "</ul>";
    $("#output").html(result);
};

function record_results_paragraph(data, status) {
    result = "<p>";
    $(data.data.translations).each(function(i, item) {
        // result += item.totalScore + " " + item.hyp + "<br/>\n";
        if (item.translatedText)
            result += item.translatedText + " ";
        else
            result += "</p><p>";
    });

    result += "</p>";
    $("#output").html(result);
};


// Displays an error message in the output box
function failure(msg) {
    $("#output").html("<div class='alert alert-danger'>" + msg + "</div>");
};

/* Query the Joshua server. We create a JSON object with the query string
 */
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

function sendMeta(command) {
  translate("| " + command + " |");
}
