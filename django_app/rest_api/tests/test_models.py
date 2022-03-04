from django.test import TestCase

from rest_api.models import AssociatedUser
from rest_api.models import DependentUser
from rest_api.models import Document
from rest_api.models import BaseUser

import datetime


class AssociatedUserTest(TestCase):
    def test_create(self):
        date = datetime.datetime(1994, 7, 7)
        u = AssociatedUser(
            first_name='Mathias',
            last_name='Scroccaro Costa',
            birth=date,
            patient=True
        )
        u.save()
        self.assertEqual(AssociatedUser.objects.count(), 1)

        users = AssociatedUser.objects.all()
        user = users[0]
        self.assertEqual(user.first_name, 'Mathias')
        self.assertEqual(user.last_name, 'Scroccaro Costa')
        self.assertEqual(user.birth, date.date())

    def test_modify(self):

        pass

    def test_create_and_delete(self):
        pass


class DependentUserTest(TestCase):
    def test_create(self):
        pass

    def test_modify(self):
        pass

    def test_create_and_delete(self):
        pass


class DocumentTest(TestCase):
    def test_create(self):
        pass

    def test_modify(self):
        pass

    def test_create_and_delete(self):
        pass

