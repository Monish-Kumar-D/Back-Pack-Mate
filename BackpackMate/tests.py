from django.test import TestCase, Client
from django.urls import reverse
from .models import User, District, Temple, Heritage_centers, Tourism_place, Tourist_spots, Beach, Comment

class ViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")

        # Create a district
        self.district = District.objects.create(name="Chennai")

        # Create a temple
        self.temple = Temple.objects.create(
            name="Kapaleeswarar Temple",
            description="A historic temple",
            architecture="Dravidian",
            major_high="Famous for its sculptures",
            venue_img="images/temple.jpg",
            zip_code="600004",
            district=self.district
        )

        # Create a heritage center
        self.heritage_center = Heritage_centers.objects.create(
            name="Fort St. George",
            description="A historical fort",
            venue_img="images/fort.jpg",
            district=self.district
        )

        # Create a tourism place
        self.tourism_place = Tourism_place.objects.create(
            name="Marina Beach",
            description="A famous beach",
            venue_img="images/marina.jpg",
            district=self.district
        )

        # Create a tourist spot
        self.tourist_spot = Tourist_spots.objects.create(
            name="Light House",
            description="A scenic lighthouse",
            venue_img="images/lighthouse.jpg",
            place=self.tourism_place
        )

        # Create a beach
        self.beach = Beach.objects.create(
            name="Elliot's Beach",
            description="A tranquil beach",
            venue_img="images/elliots.jpg",
            district=self.district
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/index.html")

    def test_login_view(self):
        # Test GET request
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/login.html")

        # Test POST request with valid credentials
        response = self.client.post(reverse("login"), {
            "username": "testuser",
            "password": "password"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

        # Test POST request with invalid credentials
        response = self.client.post(reverse("login"), {
            "username": "wronguser",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username and/or password.")

    def test_logout_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_register_view(self):
        # Test GET request
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/register.html")

        # Test POST request with valid data
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
            "confirmation": "newpassword"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

        # Test POST request with mismatched passwords
        response = self.client.post(reverse("register"), {
            "username": "newuser2",
            "email": "newuser2@example.com",
            "password": "password1",
            "confirmation": "password2"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords must match.")

    def test_temples_view(self):
        response = self.client.get(reverse("temples"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/temples.html")
        self.assertContains(response, "Kapaleeswarar Temple")

    def test_heritage_view(self):
        response = self.client.get(reverse("heritage_view", args=[self.heritage_center.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/heritage_view.html")
        self.assertContains(response, "Fort St. George")

    def test_tourism_spots_view(self):
        response = self.client.get(reverse("tourism_spots"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/t_spots.html")
        self.assertContains(response, "Marina Beach")

    def test_tourism_view(self):
        response = self.client.get(reverse("tourism_view", args=[self.tourism_place.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BackpackMate/tourism_view.html")
        self.assertContains(response, "Marina Beach")
        self.assertContains(response, "Light House")


