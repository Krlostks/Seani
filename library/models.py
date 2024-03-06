from django.db import models
from cloudinary.models import CloudinaryField


class Module(models.Model):
    name =models.CharField(
        verbose_name= 'Nombre',
        max_length=100)
    description = models.TextField(
        verbose_name='Descripcion',
        max_length= 200)
    
    @property
    def num_questions(self):
        return self.question_set.count()
    

    def str(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'


class Question(models.Model):
    module=models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name = 'Modulo')
    question_text = models.CharField(
        verbose_name="Texto de la pregunta",
        max_length=200,blank=True,
        null = True)

    question_image= CloudinaryField(
        verbose_name="Imagen de la pregunta",
        folder = 'questions', 
        resource_type ='image', 
        null = True, blank = True
    )
    #    verbose_name="Imagen de la pregunta",
     #   
      #  upload_to='Question',blank=True,
        #null=True)
    answer1= models.CharField(max_length=200, verbose_name="Respuesta A")
    answer2= models.CharField(max_length=200, verbose_name="Respuesta B")
    answer3= models.CharField(max_length=200, verbose_name="Respuesta C", null = True, blank = True)
    answer4= models.CharField(max_length=200, verbose_name="Respuesta D", null = True, blank = True)
    correct= models.CharField(max_length=5, verbose_name="Respuesta Correcta")

    
    def str(self):
        return f"{self.module} - {self.id}"
    class Meta: 
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'