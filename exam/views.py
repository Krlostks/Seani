from django.shortcuts import render
from django.http import HttpResponse

from .forms import CandidateForm
from django.contrib.auth.models import User
from .models import Exam

# Create your views here.

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