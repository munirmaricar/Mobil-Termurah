function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function submitRating() {
    let data = $(submitRatingForm).serializeArray().reduce(function (object, item) {
        object[item.name] = item.value;
        return object
    }, {});
    var newRating = document.getElementById('ratings').value;
    var articleTitle = document.getElementById('articleTitle').textContent;
    document.getElementById('articleRating').innerHTML = "";
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", data.csrfmiddlewaretoken);
            }
        },
        data: {
            articleTitle: articleTitle,
            newRating: newRating,
            csrfmiddlewaretoken: data.csrfmiddlewaretoken,
        },
        url: "/chooseArticleSubmitRating/",
        success: function (data) {
            $.ajax({
                url: "/articlesjson/",
                datatype: JSON,
                success: function (data) {
                    for (var i = 0; i < data.articles.length; i++) {
                        if (data.articles[i].articleTitle === articleTitle) {
                            document.getElementById('articleRating').innerHTML += "<h2 style='color: #518384; font-weight: bold;'><i class='fas fa-star' style='color: #518384;'></i> " +
                                data.articles[i].articleRating + "</h2>";
                        }
                    }
                },
                type: 'GET'
            });
        },
        type: 'POST'
    })
}