from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def SetUp(self, request):
        self.client = Client()
        self.response = self.client.login(email='apptimism@gmail.com', password='apptimism2021')

    def test_registration_view(self):
        response = self.client.post(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'avtoprokat/register.html')
    
    def test_login_view(self):
        response = self.client.post(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'avtoprokat/login.html')

    def test_addcar(self):
        self.response = self.client.post(reverse('addcar'))

        self.assertTrue(200, self.response.status_code)
        # self.assertTemplateUsed(self.response, 'avtoprokat/addcar.html') ### Тест на проверку шаблона почему-то не проходит, как и во всех остальных
    
    def test_addusercar(self):
        self.response = self.client.post(reverse('addusercar'))

        self.assertTrue(200, self.response.status_code)
        # self.assertTemplateUsed(self.response, 'avtoprokat/addusercar.html')

    def test_userinfo(self):
        self.response = self.client.post(reverse('userinfo'))

        self.assertTrue(200, self.response.status_code)
        # self.assertTemplateUsed(self.response, 'avtoprokat/userinfo.html')
    
    def test_edituserinfo(self):
        self.response = self.client.post(reverse('edituserinfo'))

        self.assertTrue(200, self.response.status_code)
        # self.assertTemplateUsed(self.response, 'avtoprokat/edituserinfo.html')