from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SnackTests(TestCase):

  def test_list_page_status_code(self):
    url = reverse("snack_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_list_page_template(self):
    url = reverse("snack_list")
    response = self.client.get(url)
    self.assertTemplateUsed(response, "snack_list.html")
    self.assertTemplateUsed(response, "base.html")
    
  #use url name instead of hard coded path
  def test_hard_coded_path(self):
    url = reverse("snack_list")
    self.assertEqual(url, "/snack_list")