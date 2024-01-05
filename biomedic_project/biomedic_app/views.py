
# biomedic_app/views.py
import requests
from django.shortcuts import render, redirect
from .models import Patient, Topic, Post
from django.http import HttpResponse
from .forms import  RegistrationForm
from geopy.geocoders import Nominatim
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
import random
import string


def index(request):
    return render(request, 'biomedic_app/index.html')


def generate_unique_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def find_nearest_hospital(patient_location, hiv_status, tb_status, hypertension_status):
    # Replace with the actual healthcare API endpoint
    api_url = 'https://example.com/api/find_nearest_hospital'

    # Prepare request parameters
    params = {
        'latitude': patient_location.latitude,
        'longitude': patient_location.longitude,
        'hiv_status': hiv_status,
        'tb_status': tb_status,
        'hypertension_status': hypertension_status,
    }

    # Make a request to the healthcare API
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        nearest_hospital = response.json().get('nearest_hospital')
        return nearest_hospital

    return None
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.unique_number = generate_unique_number()

            # Geocode the provided location
            geolocator = Nominatim(user_agent="your_app_name")
            patient_location = geolocator.geocode(patient.location)

            if patient_location:
                # Call the healthcare API to find the nearest hospital
                nearest_hospital = find_nearest_hospital(
                    patient_location,
                    patient.hiv_status,
                    patient.tb_status,
                    patient.hypertension_status
                )

                if nearest_hospital:
                    patient.nearest_hospital = nearest_hospital

            patient.save()
            return render(request, 'biomedic_app/registration_success.html', {'patient': patient})
    else:
        form = RegistrationForm()

    return render(request, 'biomedic_app/registration.html', {'form': form})


def login_view(request):
    # Your login view logic here
    return render(request, 'biomedic_app/login.html')

def medication(request):
    # Implement medication ordering logic
    return render(request, 'biomedic_app/medication.html')

def counseling(request):
    # Implement counseling access logic
    return render(request, 'biomedic_app/counseling.html')

def forum(request):
    topics = Topic.objects.all()
    # Implement forums logic
    return render(request, 'biomedic_app/forum.html')
def create_topic(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_topic = Topic(title=title, description=description)
        new_topic.save()
        return redirect('forum')  # Redirect back to the forum page

    return HttpResponse("Invalid request method")
def view_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    posts = Post.objects.filter(topic=topic)
    return render(request, 'view_topic.html', {'topic': topic, 'posts': posts})

def elearning(request):
    # Implement educational platform logic
    return render(request, 'biomedic_app/E-learning.html')

# Create your views here.
