from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404,  redirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models import Avg
import json
from . import models



def temples(request):
    all_temples = models.Temple.objects.all()
    return render(request, "BackpackMate/temples.html", {
        "all_temples" : all_temples
    })


def temple_view(request, id):
    if request.method == "GET":
        temple = get_object_or_404(models.Temple, pk=id)
        content_type = ContentType.objects.get_for_model(temple)
        comments = models.Comment.objects.filter(content_type=content_type, object_id=temple.id).order_by('-timestamp')
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']
        no_of_comments =0
        sum_of_comments = 0
        for comment in comments:
            no_of_comments+=1
            sum_of_comments+=comment.rating
            comment.time_ago = time_ago(comment.timestamp)
        return render(request, "BackpackMate/temple_view.html", {
            "temple": temple,
            "comments": comments,
            "content_type": content_type,
            "avg_rating" : avg_rating if avg_rating else 0,
            "no_of_comments" : no_of_comments,
            "sum_of_comments" : sum_of_comments
        })
    elif request.method == "POST":
            data = json.loads(request.body)
            body = data.get("body")
            content_type_id = data.get("content_type_id")
            object_id = data.get("object_id")
            rating = data.get("rating") if data.get("rating") else 5

            content_type = ContentType.objects.get_for_id(content_type_id)
            temple = get_object_or_404(content_type.model_class(), pk=object_id)

            comment = models.Comment.objects.create(
                user=request.user,
                body=body,
                content_type=content_type,
                object_id=temple.id,
                rating=rating,
                timestamp=now(),  # Add timestamp
            )

            return JsonResponse({
                "success": True,
                "comment": {
                    "body": comment.body,
                    "user": comment.user.username,
                    "rating": comment.rating,
                    "time_ago": time_ago(comment.timestamp),
                }
            })


def heritage(request):
    centers = models.Heritage_centers.objects.all()
    return render(request, "BackpackMate/heritage.html", {
        "centers" : centers
    })

def heritage_view(request, id):
    if request.method == "GET":
        center = get_object_or_404(models.Heritage_centers, pk=id)
        content_type = ContentType.objects.get_for_model(center)
        comments = models.Comment.objects.filter(content_type=content_type, object_id=center.id).order_by('-timestamp')
        no_of_comments =0
        sum_of_comments = 0
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']
        for comment in comments:
            no_of_comments+=1
            sum_of_comments+=comment.rating
            comment.time_ago = time_ago(comment.timestamp)
        return render(request, "BackpackMate/heritage_view.html", {
            "center": center,
            "comments": comments,
            "content_type": content_type,
            "avg_rating" : avg_rating if avg_rating else 0,
            "no_of_comments" : no_of_comments,
            "sum_of_comments" : sum_of_comments
        })
    elif request.method == "POST":
        data = json.loads(request.body)
        body = data.get("body")
        content_type_id = data.get("content_type_id")
        object_id = data.get("object_id")
        rating = data.get("rating") if data.get("rating") else 5

        content_type = ContentType.objects.get_for_id(content_type_id)
        temple = get_object_or_404(content_type.model_class(), pk=object_id)

        comment = models.Comment.objects.create(
            user=request.user,
            body=body,
            content_type=content_type,
            object_id=temple.id,
            rating=rating,
            timestamp=now(),  # Add timestamp
        )

        return JsonResponse({
            "success": True,
            "comment": {
                "body": comment.body,
                "user": comment.user.username,
                "rating": comment.rating,
                "time_ago": time_ago(comment.timestamp),
            }
        })



def tourism_spots(request):
    spots = models.Tourism_place.objects.all()
    return render(request, "BackpackMate/t_spots.html", {
        "spots":spots,
    })



def tourism_view(request,id):
    if request.method == "GET":
        place = get_object_or_404(models.Tourism_place, pk=id)
        content_type = ContentType.objects.get_for_model(place)
        comments = models.Comment.objects.filter(content_type=content_type, object_id=place.id).order_by('-timestamp')
        spots = models.Tourist_spots.objects.filter(place=place)
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']
        no_of_comments =0
        sum_of_comments = 0
        for comment in comments:
            no_of_comments+=1
            sum_of_comments+=comment.rating
            comment.time_ago = time_ago(comment.timestamp)
        return render(request, "BackpackMate/tourism_view.html", {
            "center": place,
            "spots" : spots,
            "comments": comments,
            "content_type": content_type,
            "avg_rating" : avg_rating if avg_rating else 0,
            "no_of_comments" : no_of_comments,
            "sum_of_comments" : sum_of_comments,
        })
    elif request.method == "POST":
        data = json.loads(request.body)
        body = data.get("body")
        content_type_id = data.get("content_type_id")
        object_id = data.get("object_id")
        rating = data.get("rating") if data.get("rating") else 5

        content_type = ContentType.objects.get_for_id(content_type_id)
        temple = get_object_or_404(content_type.model_class(), pk=object_id)

        comment = models.Comment.objects.create(
            user=request.user,
            body=body,
            content_type=content_type,
            object_id=temple.id,
            rating=rating,
            timestamp=now(),  # Add timestamp
        )

        return JsonResponse({
            "success": True,
            "comment": {
                "body": comment.body,
                "user": comment.user.username,
                "rating": comment.rating,
                "time_ago": time_ago(comment.timestamp),
            }
        })



def spots_view(request,id):
    spot = models.Tourist_spots.objects.get(pk=id)
    return render(request, "BackpackMate/spot_view.html", {
        "spot":spot,
    })


def beach(request):
    beaches = models.Beach.objects.all()
    return render(request, "BackpackMate/beaches.html", {
        "beaches" : beaches
    })


def beach_view(request,id):
    if request.method == "GET":
        center = get_object_or_404(models.Beach, id=id)
        content_type = ContentType.objects.get_for_model(center)
        comments = models.Comment.objects.filter(content_type=content_type, object_id=center.id).order_by('-timestamp')
        no_of_comments =0
        sum_of_comments = 0
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']
        for comment in comments:
            no_of_comments+=1
            sum_of_comments+=comment.rating
            comment.time_ago = time_ago(comment.timestamp)
        return render(request, "BackpackMate/heritage_view.html", {
            "center": center,
            "comments": comments,
            "content_type": content_type,
            "avg_rating" : avg_rating if avg_rating else 0,
            "no_of_comments" : no_of_comments,
            "sum_of_comments" : sum_of_comments
        })
    elif request.method == "POST":
        data = json.loads(request.body)
        body = data.get("body")
        content_type_id = data.get("content_type_id")
        object_id = data.get("object_id")
        rating = data.get("rating") if data.get("rating") else 5

        content_type = ContentType.objects.get_for_id(content_type_id)
        temple = get_object_or_404(content_type.model_class(), pk=object_id)

        comment = models.Comment.objects.create(
            user=request.user,
            body=body,
            content_type=content_type,
            object_id=temple.id,
            rating=rating,
            timestamp=now(),  # Add timestamp
        )

        return JsonResponse({
            "success": True,
            "comment": {
                "body": comment.body,
                "user": comment.user.username,
                "rating": comment.rating,
                "time_ago": time_ago(comment.timestamp),
            }
        })



def contribute(request):
    if request.method == "GET":
        return render(request, 'BackpackMate/contribute.html')


def addnew_beach(request):
    if request.method=="GET":
        places = models.District.objects.all()
        return render(request,"BackpackMate/new_beach.html", {
            "places" : places
        })
    else:
        name = request.POST['name']
        description = request.POST['description']
        mapUrl = request.POST['mapUrl']
        try:
            image = request.FILES.get('image')
        except ObjectDoesNotExist:
            return HttpResponse("No image uploaded. Please go back and upload an image.")
        place_name = request.POST['place']
        place = models.District.objects.get(name=place_name)

        new_beach = models.Beach(
            name = name,
            description = description,
            venue_img = image,
            district = place,
            mapUrl = mapUrl
        )
        new_beach.save()
        return render(request,"BackpackMate/thank.html")


def addnew_heritage(request):
    if request.method=="GET":
        places = models.District.objects.all()
        return render(request,"BackpackMate/new_heritage.html", {
            "places" : places
        })
    else:
        name = request.POST['name']
        description = request.POST['description']
        mapUrl = request.POST['mapUrl']
        try:
            image = request.FILES.get('image')
        except ObjectDoesNotExist:
            return HttpResponse("No image uploaded. Please go back and upload an image.")
        place_name = request.POST['place']
        place = models.District.objects.get(name=place_name)

        new_heritage = models.Heritage_centers(
            name = name,
            description = description,
            venue_img = image,
            district = place,
            mapUrl = mapUrl
        )
        new_heritage.save()
        return render(request,"BackpackMate/thank.html")


def addnew_t_spots(request):
    if request.method=="GET":
        places = models.Tourism_place.objects.values_list('name', flat=True)
        return render(request,"BackpackMate/new_t_spots.html", {
            "places" : places
        })
    else:
        name = request.POST['name']
        description = request.POST['description']
        mapUrl = request.POST['mapUrl']
        try:
            image = request.FILES.get('image')
        except ObjectDoesNotExist:
            return HttpResponse("No image uploaded. Please go back and upload an image.")
        place_name = request.POST['place']
        place = models.Tourism_place.objects.get(name=place_name)

        new_t_spots = models.Tourist_spots(
            name = name,
            description = description,
            venue_img = image,
            place = place,
            mapUrl = mapUrl
        )
        new_t_spots.save()
        return render(request,"BackpackMate/thank.html")


def addnew_temple(request):
    if request.method=="GET":
        places = models.District.objects.all()
        return render(request,"BackpackMate/new_temple.html", {
            "places" : places
        })
    else:
        name = request.POST['name']
        description = request.POST['description']
        architecture = request.POST['architecture']
        major_high = request.POST['major_high']
        zipcode = request.POST['zipcode']
        mapUrl = request.POST['mapUrl']
        try:
            image = request.FILES.get('image')
        except ObjectDoesNotExist:
            return HttpResponse("No image uploaded. Please go back and upload an image.")
        place_name = request.POST['place']
        place = models.District.objects.get(name=place_name)

        new_temple = models.Temple(
            name = name,
            description = description,
            venue_img = image,
            district = place,
            architecture = architecture,
            major_high = major_high,
            zipcode = zipcode,
            mapUrl = mapUrl
        )
        new_temple.save()
        return render(request,"BackpackMate/thank.html")


def time_ago(timestamp):
    delta = now() - timestamp
    if delta.days < 1:  # Less than 1 day
        hours = delta.seconds // 3600
        if hours == 0:
            minutes = delta.seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif delta.days < 7:  # Less than 1 week
        return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"
    elif 7 <= delta.days < 30:  # 1 week or more, less than 1 month
        weeks = delta.days // 7
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
    elif 30 <= delta.days < 365:  # 1 month or more, less than 1 year
        months = delta.days // 30
        return f"{months} month{'s' if months != 1 else ''} ago"
    else:  # 1 year or more
        years = delta.days // 365
        return f"{years} year{'s' if years != 1 else ''} ago"




def index(request):
    return render(request, 'BackpackMate/index.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "BackpackMate/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "BackpackMate/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "BackpackMate/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = models.User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "BackpackMate/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "BackpackMate/register.html")
