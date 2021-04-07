from django.test import SimpleTestCase
from django.urls import reverse, resolve
from avtoprokat.views import (
    registration_view,
    login_view,
    logout_view,
    addcar,
    addusercar,
    userinfo,
    edituserinfo
)

class TestUrls(SimpleTestCase):

    def test_accounts_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registration_view)
    
    def test_accounts_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)
    
    def test_accounts_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_addcar(self):
        url = reverse('addcar')
        self.assertEquals(resolve(url).func, addcar)
    
    def test_userinfo(self):
        url = reverse('userinfo')
        self.assertEquals(resolve(url).func, userinfo)

    def test_edituserinfo(self):
        url = reverse('edituserinfo')
        self.assertEquals(resolve(url).func, edituserinfo)
    