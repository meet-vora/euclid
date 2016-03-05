from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *

def index(request):
	question_list = Question.objects.all()
	display = [(q.id, q.level) for q in question_list]
	return render(request, 'euclid/index.html', {'question_list': question_list})

@login_required(login_url='/euclid/login/')
def individual_question(request, question_id):
	if request.POST:
		question = Question.objects.get(pk =question_id)
		problem_statement = question.question_text
		solution =  int(question.answer) == int(request.POST['answer'])
		if solution:
			userprofile
		attempt = True
	else:
		attempt = False
		solution = None
		try:
			question = Question.objects.get(pk = question_id)
		except Question.DoesNotExist:
			raise Http404("Question does not exist")
		problem_statement = question.question_text
	return render(request, 'euclid/post.html', {'problem': problem_statement, 'id': question_id, 'attempt': attempt, 'solution': solution})

def register(request):
	if request.POST:
		user = User()
		user.username = request.POST['username']
		user.email = request.POST['email']
		user.password = request.POST['password']
		user.save()
		userprofile = UserProfile()
		userprofile.user = user
		userprofile.questions_solved = ''
		userprofile.save()
		return HttpResponseRedirect('/euclid/login')
	else:
		return render(request, 'euclid/register.html')

def login_user(request):
	status = True
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		userprofile = authenticate(username=username, password=password)
		if userprofile is not None:
			user = userprofile.user
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, user)
			return HttpResponseRedirect('/euclid/')
		else:
			status = False
	return render(request, 'euclid/login.html', {'status': status})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/euclid/')