var questionQueue = [];

function askUserInput(string, callback) {
    if (questionQueue.length == 0) {
        rl.question(string, function(answer) {
            fs.exists(answer, function(exists) {
                if (exists === false) {
                    echo('File ' + answer + ' not found!');
                    askUserInput(string, callback);
                } else {
                    callback(answer);

                    if (questionQueue.length > 0) {
                        var question = questionQueue.shift();
                        askUserInput(question.string, question.callback);
                    }
                }
            });
        });
    } else {
        questionQueue.push({ string: string, callback: callback });
    }
}