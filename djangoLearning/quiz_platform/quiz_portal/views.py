
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from quiz_portal.models import quiz
from quiz_portal.createQuiz import Constructor
import io, json

def index(request):
    list=quiz.objects.filter(status='published')
    #[print(i.title) for i in list]
    return render(request, 'items/index.html', {
        'list': list,
    })


def viewSelectedQuiz(request, id):
    toDisplay=get_object_or_404(quiz,id=id)
    xmlQuiz=Constructor(io.StringIO(toDisplay.quizXml))
    #print (xmlQuiz.quiz)
    return render(request, 'items/quiz.html', {'obj':xmlQuiz.quiz,})


def createOwnQuiz(request):
    return render(request, 'items/item_create.html')






