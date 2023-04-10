setInterval(function() {
    $.ajax({
        url: "/camera",
        success: function(data) {
            var newImageUrl = "{% static 'img/CAMERA/' %}{{ NEW }}";
            var imageElement = document.getElementById("links");
            imageElement.setAttribute("src", newImageUrl);
        }
    });
}, 100);
