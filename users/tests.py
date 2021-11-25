from django.test import TestCase
from users.models import UserModel


class UserTestCase(TestCase):
    def setUp(self):
        UserModel.objects.create(name="Lion", birthday="2021-10-02", sex="Masculino", mail="user@mail.com", password="4213")
        UserModel.objects.create(name="Rute", birthday="2015-12-25", sex="Feminio", mail="user2@mail.com", password="159753")
        UserModel.objects.create(name="Mart", birthday="1995-08-17", sex="Masculino", mail="user3@mail.com", password="951753")

    def test_animals_can_speak(self):
        """Users that are male are correctly identified"""
        men = UserModel.objects.filter(sex="Masculino")
        self.assertEqual(len(men), 2)
