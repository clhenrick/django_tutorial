from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
#from django.template import RequestContext, loader

from .models import Choice, Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]  
  context = {'latest_question_list' : latest_question_list} # shortcut
  return render(request, 'polls/index.html', context)
  
# def index(request):
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]  
  # template = loader.get_template('polls/index.html')
  # context = RequestContext(request, {
  #     'latest_question_list' : latest_question_list,
  #   })
  # return HttpResponse(template.render(context))

# def index(request):
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]    
  # output = ', '.join([p.question_text for p in latest_question_list])
  # return HttpResponse(output)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
  #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  #### left off here!!! ####
  # response = "You're looking at the results of question %s."
  # return HttpResponse(response % question_id)



def vote(request, question_id):
  p = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExists):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
        'question' : p,
        'error_message' : "You didn't select a choice.",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Return an HttpResponse after successfully dealing with POST data.
    # prevents data from being posted twice if user hits back button
    return HttpResponseRedirect(reverse('polls:results', args=(p.id, )))
  # return HttpResponse("You're voting on question %s." % question_id)







