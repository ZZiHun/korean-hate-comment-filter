(function () {
    var processedComments = [];
    var badWords = []
    function warnBadComment() {
        var newProcessedComment = [];
        var youtubeCommentBox = document.querySelectorAll("#contenteditable-root");
        console.log(youtubeCommentBox);
        // if 0 (hate speech) replace with redacted
        // if 1 (offensive language) replace offensive word with non offensive word

        [].slice.call(youtubeCommentBox).forEach(function (el) {
            const http = new XMLHttpRequest();
            const url = 'http://localhost:5000/block-hate-speech';

            http.open('POST', url);
            http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            http.responseType = 'json';

            var comment = (el.textContent === undefined) ? el.innerText : el.textContent;
            newProcessedComment.push(comment)

            if (!processedComments.includes(comment)) {
                http.send(JSON.stringify({
                    "comment": comment
                }));
            }

            http.onload = function () {
                var jsonResponse = http.response;
                console.log(jsonResponse);

                if (jsonResponse != null && jsonResponse["classification"] == 0) {
                    var newContent = el.innerHTML.replace(/.*/s, "ANTI-HATE SPEECH PLUGIN: 악플이 감지되었습니다. 입력 전 다시 생각해보자.");
                    if (newContent != el.innerHTML) {
                        el.innerHTML = newContent;
                    }
                } else {
                    tokens = comment.split(" ")
                    for (var i = 0; i < tokens.length; i += 1) {
                        if (badWords.includes(tokens[i])) {
                            var newContent = el.innerHTML.replace(tokens[i], "****");
                            if (newContent != el.innerHTML) {
                                el.innerHTML = newContent;
                            }
                        }
                    }
                }
            };
        });

        processedComments = newProcessedComment;
    }

    // Replace words every 5000 ticks
    function tick() {
        // If it determines hate speech of offensive language (0/1)

        warnBadComment();
        window.setTimeout(tick, 100);
    }

    tick();
})();