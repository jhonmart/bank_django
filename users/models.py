from django.db import models
from djchoices import ChoiceItem, DjangoChoices

class UserModel(models.Model):
    class Sex(DjangoChoices):
        male = ChoiceItem("Masculino")
        female = ChoiceItem("Feminino")

    name = models.CharField(max_length=50, )
    birthday = models.DateField()
    sex = models.CharField(max_length=10, choices=Sex.choices)
    mail = models.EmailField()
    password = models.CharField(max_length=19, )
