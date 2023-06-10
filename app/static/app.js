$(document).ready(function() {
    // Function to make the API call and update the image and text
    function updateImageAndText() {
        $.get("/get-text-and-image", function(data) {
            var text = data.text;
            var imageBase64 = data.image;
            decodeBase64Image(imageBase64, function(imageUrl) {
                $("#overlay").text(text);
                $("#image").attr("src", imageUrl);
            // Call the function again after a certain delay
            setTimeout(updateImageAndText, 0); // Repeat the API call every 5 seconds
            });
        });
    }

    // Initial API call to start the cycle
    updateImageAndText();
});

function decodeBase64Image(base64, callback) {
    var cleanBase64 = base64.replace(/^data:image\/jpeg;base64,/, '');
    var padding = '='.repeat((4 - cleanBase64.length % 4) % 4);
    var base64Data = cleanBase64 + padding;
    var binaryData = atob(base64Data);
    var byteArray = new Uint8Array(binaryData.length);
    for (var i = 0; i < binaryData.length; i++) {
        byteArray[i] = binaryData.charCodeAt(i);
    }
    var blob = new Blob([byteArray], { type: 'image/jpeg' });
    var imageUrl = URL.createObjectURL(blob);
    callback(imageUrl);
}

