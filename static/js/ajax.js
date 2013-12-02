$(function() {       /*only runs when document is loaded*/
   $('#search').keyup(function() {     //event handler on keyup on <input id="search">
       
       $.ajax({
            type: "POST",
            url: "/articles/search/",
            data: {
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,    
            dataType: 'html'    //expect html to come back from AJAX call
       });
    
   });
});

//3 params defined by jquery's ajax handler
function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data)
}
