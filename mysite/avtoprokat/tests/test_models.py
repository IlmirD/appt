from django.test import TestCase
import datetime
from avtoprokat.models import User, Car


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='email@gmail.com',
            username='username',
            language='en',
            date_joined = datetime.datetime.now(),
            last_login = datetime.datetime.now(),
            is_admin = False,
            is_active = True,
            is_staff = False,
            is_superuser = False,
        )


    def test_str(self):
        self.assertEquals(self.user.username, 'username')

    def test_has_perm(self):
        self.assertEquals(self.user.is_admin, False)

    def test_str_(self):
        self.car = Car.objects.create(
            name_en = 'Lada',
            name_ru = 'Лада',
            created = '2020-1-1',
            added = '2020-1-1',
        )
        self.assertEquals(self.car.name_en, 'Lada')
        
    
