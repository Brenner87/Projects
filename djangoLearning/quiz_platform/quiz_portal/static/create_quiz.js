function createQuiz(quizContainer, appendButton, submitButton){
    var questionNumber=1
    function addQuestion(quizContainer){
        if (questionNumber>20){
        alert('Максимальна кількість питаннь досягнена')
        return
        }
        var question='<div class="form">\n'+
            '<form class=question>\n'+
            '<div>'+questionNumber+
            'Питання:</div>\n'+
            '<div class="question"><input type="text" name="question"></div>\n'+
            '<div><p>Варіанти відповіді:</p></div>\n'+
            '<div class="choice">1: <input type="text" name="choice1"></div>\n'+
            '<div class="choice">2: <input type="text" name="choice2"></div>\n'+
            '<div class="choice">3: <input type="text" name="choice3"></div>\n'+
            '<div class="choice">4: <input type="text" name="choice4"></div>\n'+
            '<div class="choice">5: <input type="text" name="choice5"></div>\n'+
            '<div class="choice">6: <input type="text" name="choice6"></div>\n'+
            '<div>Правильні варіанти(через кому): <input type="text" name="correctAnswers"></div>\n'+
            '</form></div>'

        var target=document.createElement("div")
        target.innerHTML=question
        quizContainer.appendChild(target)
        questionNumber++

    }

    function createJson(quizContainer){
        var quiz={}
        quiz.question=[]
        quiz.name=document.querySelector('input[name=title]').value
        if(!(quiz.name)){
            alert("Будь-ласка, введіть назву тесту")
            return
        }
        var questions=quizContainer.querySelectorAll('form')
        for (var i=0; i<questions.length; i++){
            question=[]
            items=questions[i].querySelectorAll('input')
            console.log(items)
            var answers=items[items.length-1].value
            console.log(answers)

            if (!(answers)){
                alert('Вкажіть правильні варианти відповіді')
                return
            }
            for (var j=0; j<items.length; j++){
                if (items[j].name=="correctAnswers"){
                    continue
                }
                if (items[j].value){
                    question.push(items[j].value)
                }
            }
            question.push(answers.split(','))
            quiz.question.push(question)
        }
        console.log(quiz)

    }
    appendButton.onclick=function(){addQuestion(quizContainer)}
    submitButton.onclick=function(){createJson(quizContainer)}
}