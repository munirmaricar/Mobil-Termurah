function submitRating() {
    var newRating = document.getElementById('ratings').value;
    $.ajax({
        url: "http://127.0.0.1:8000/articlesjson/",
        dataType: "json",
        success: function (data) {
            console.log('YOOOO');
            var json = JSON.parse(data.article);
            for (var i = 0; i < json.length; i++) {
                if (json[i].fields.articleTitle === $("#articleTitle").text) {
                    var articleRating = json[i].fields.articleRating;
                    console.log(json[i].fields.articleRating);
                    var totalRatings = json[i].fields.totalRatings;
                    articleRating = ((articleRating * totalRatings) + newRating) / (
                        totalRatings + 1);
                    totalRatings = totalRatings + 1;
                }
            }
        },
        type: 'GET'
    })
}