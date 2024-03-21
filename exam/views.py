from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import CandidateForm
from django.contrib.auth.models import User
from .models import Exam


@login_required
def home(request):
    user = request.user
    if user.is_superuser:
         return redirect ('admin:index')
    return render(request, 'exam/home.html', {'user': user})

@login_required
def question (request, m_id, q_id=1):
    exam = request.user.exam

    if request.method == 'POST':
        answer = request.POST['answer']
        questions = exam.breakdown_set.filter(question__module_id=m_id)
        question= questions[q_id -1]
        questions.answer=answer
        question.save()
        return redirect('exam:question', m_id, q_id +1 )
    try :

        questions = exam.breakdown_set.filter(qustion__module_id=m_id)
        question=questions[q_id-1].questio
        answer = questions[q_id -1].answer
        return render(request, 'exam/question.html',{
            'question' : question,
            'correct' : answer,
            'm_id' : m_id,
            'q_id':q_id})
    except IndexError:
            return redirect('exam:home')

# def question (request, m_id, q_id=1):
#     user = request.user
#     question = user.exam.questions.filter(module_id=m_id)
#     question=question[q_id-1]
#     return render(request, 'exam/question.html',{'question' : question})

# Create your views here.

@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            #recibir datos
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            career = form.cleaned_data['career']
            stage = form.cleaned_data['stage']

            #crear usuario
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            #crear examen
            exam = Exam.objects.create(
                user=user,
                career=career,
                stage=stage
            )

    form = CandidateForm()
    return render(request,
                  'exam/add_candidate.html',
                  {'form': form}
                )