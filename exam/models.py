from django.db import models
from career.models import Career
from django.contrib.auth.models import User
from library.models import Module, Question

# Create your models here.
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name =  "Etapa",
        max_length=2
        )
    application_date = models.DateField(
        verbose_name = "Fecha de aplicacion"
    )
    
    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio' , 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

        return months[self.application_date.month - 1]
    
    def _str_(self):
        return f"{ self.stage } - {self.month } - { self.year }"
    
    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

class Exam(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuarios')
    stage = models.ForeignKey(Stage, on_delete = models.CASCADE, verbose_name = 'Etapa')
    career = models.ForeignKey(Career, on_delete = models.CASCADE, verbose_name = 'Carrera')
    modules = models.ManyToManyField(Module, through='ExamModule', verbose_name = 'Modulos')
    questions = models.ManyToManyField('Question', through='Breakdown', verbose_name = 'Preguntas')
    score = models.FloatField(verbose_name = 'Calificacion', default = 0.0)
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Creado')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Actualizado')

    def set_modules (self):
        for module in Module.objects.all():
            self.modules.add(module)

    def set_questions (self):
        for module in self.modules.all():
            for question in Question.objects.filter(module=module):
                Breakdown.objects.crate(examen = self,question = question, correct = question.correct)

    def __str__(self):
        return f"{self.user} - {self.career} -: {self.score}"
    class Meta: 
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"
    
    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"
    
class ExamModule(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE, verbose_name = 'Examen')
    module = models.ForeignKey(Module, on_delete = models.CASCADE, verbose_name = 'Modulo')
    active = models.BooleanField(verbose_name = 'Activo', default = True)
    score = models.FloatField(verbose_name = 'Calificacion', default = 0.0)

    def __str__(self):
        return f"{self.module} - {self.score}"


class Breakdown(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE, verbose_name = 'Examen')
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = 'Pregunta')
    answer = models.CharField(verbose_name = 'Respuesta', max_lenght = 5, default = '-')
    correct = models.CharField(verbose_name = 'Respuesta correcta', max_lenght = 5, default = '-')

    def __str__(self):
        return f"{self.question} - {self.answer} - {self.correct}"