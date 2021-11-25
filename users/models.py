from django.db import models
from django.contrib.auth.hashers import make_password
from djchoices import ChoiceItem, DjangoChoices


class UserModel(models.Model):
    class Sex(DjangoChoices):
        male = ChoiceItem("Masculino")
        female = ChoiceItem("Feminino")

    name = models.CharField(max_length=50, )
    birthday = models.DateField()
    sex = models.CharField(max_length=10, choices=Sex.choices)
    email = models.EmailField()
    password = models.CharField(max_length=19, )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.password = make_password(password=self.password, salt=None, hasher='pbkdf2_sha256')
        super().save()
