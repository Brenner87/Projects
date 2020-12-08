from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from BookLearning.models import Book, Publisher
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import ListView

import datetime



def current_date(request):
    cur_date=datetime.datetime.now()
    t=Template("""<html><head><title>Date</title></head><body><p>Current date is {{ cur_date }}</p></body></html>""")
    c=Context({'cur_date' : cur_date})
    return HttpResponse(t.render(c))

def newer_current_date(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date' : now})
    return HttpResponse(html)

def best_current_date(request):
    now=datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def time_offset(request,offset):
    cur_date=datetime.datetime.now()
    try:
        delta=datetime.timedelta(hours=int(offset))
    except Exception:
        return Http404('invalid offset')
    result=cur_date+delta

    t = Template("""<html><head><title>Date</title></head><body><p>Current date is {{ result }}</p></body></html>""")
    c = Context({'result': result})

    #return HttpResponse(str(cur_date+delta))
    return HttpResponse(t.render(c))


def best_time_offset(request, offset):
    cur_date=datetime.datetime.now()
    try:
        delta=datetime.timedelta(hours=int(offset))
    except Exception:
        return Http404('invalid offset')
    result=cur_date+delta
    return render(request, 'hours_ahead.html', {'next_time':result, 'hour_offset':offset})


def get_service_info(request):
    result='<html><head></head><body>'
    for i in request.META:
        result+='<div>'+str(i)+' : '+str(request.META[i])+'</div>'
    result+='</body></html>'
    return HttpResponse(result)

def get_post(request):
    result = '<html><head></head><body>'
    for i in request.GET:
        result += '<div>' + str(i) + ' : ' + str(request.META[i]) + '</div>'
    result += '</body></html>'
    return HttpResponse(result)


def test_search_form(request):
    return render(request, 'test_search_form.html')


def test_search(request):
    if 'q' in request.GET and request.GET['q']!='':
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def query_params(request):
    return HttpResponse(str(request.GET['hours']))


#def search_form(request):
#    return render(request, 'search_form.html')

def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books=Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books':books, 'query': q})

    return render(request, 'search_form.html', {'errors': errors})

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),['siteowner@example.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})

class PublisherList(ListView):
    model=Publisher
    template_name='publisher_list.html'
