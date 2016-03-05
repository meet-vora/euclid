from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *

def index(request):
	question_list = Question.objects.all()
	userprofile_list = UserProfile.objects.all()
	userprofile_list_solved_str = [userprofile.questions_solved.split(';')[:-1] for userprofile in userprofile_list]
	question_solve_count = [0]*len(question_list)
	for up_list_solved_str in userprofile_list_solved_str:
		userprofile_list_solved = [int(s) for s in up_list_solved_str]
		if userprofile_list_solved is not None:
			for entry in userprofile_list_solved:
				question_solve_count[entry-1] += 1
	print question_solve_count
	solved_by_user = []
	display =[]
	if request.user.is_authenticated():
		userprofile = UserProfile.objects.get(user = request.user)
		if userprofile.questions_solved.split(';') != ['']:
			solved_by_user = [int(s) for s in userprofile.questions_solved.split(';')[:-1]]
	for i, q in enumerate(question_list):
		solved_by_count = 0
		solved = False
		if int(q.id) in solved_by_user:
			solved = True
		display.append((q.id, q.level, solved, question_solve_count[i]))
	return render(request, 'euclid/index.html', {'question_list': display})

@login_required(login_url='/euclid/login/')
def individual_question(request, question_id):
	userprofile = UserProfile.objects.get(user = request.user) 
	solved = False
	if request.POST:
		question = Question.objects.get(pk =question_id)
		problem_statement = question.question_text
		solution =  int(question.answer) == int(request.POST['answer'])
		if solution:
			userprofile.questions_solved += str(question_id) + ';'
			userprofile.save()
		attempt = True
	else:
		attempt = False
		solution = None
		if userprofile.questions_solved.split(';') != ['']:
			solved_by_user = [int(s) for s in userprofile.questions_solved.split(';')[:-1]] 
			if int(question_id) in solved_by_user:
				solved = True
				attempt = True
		try:
			question = Question.objects.get(pk = question_id)
		except Question.DoesNotExist:
			raise Http404("Question does not exist")
		problem_statement = question.question_text
	return render(request, 'euclid/post.html', {'problem': problem_statement, 'id': question_id, 'attempt': attempt, 'solution': solution, 'solved': solved})

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