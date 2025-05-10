from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("temples", views.temples, name="temples"),
    path("temple_item/<int:id>", views.temple_view, name="temple_item"),
    path("heritage_centers", views.heritage, name="heritage_centers"),
    path("heritage_centers/<int:id>", views.heritage_view, name="heritage_view"),
    path("tourism_spots", views.tourism_spots, name="tourism_spots"),
    path("tourism_spots/<int:id>", views.tourism_view, name="tourism_view"),
    path("spots_view/<int:id>", views.spots_view, name="spots_view"),
    path("beach", views.beach, name="beach"),
    path("beach/<int:id>", views.beach_view, name="beach_view"),
    path("contribute", views.contribute, name="contribute"),
    path("addnew/temple", views.addnew_temple, name='addnew_temple'),
    path("addnew/beach", views.addnew_beach, name='addnew_beach'),
    path("addnew/heritage", views.addnew_heritage, name='addnew_heritage'),
    path("addnew/t_spots", views.addnew_t_spots, name='addnew_t_spots'),
    path("places", views.place_list, name="place_list"),
    path("district-autocomplete/", views.district_autocomplete, name="district_autocomplete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)