import random
import string

from django.http import HttpResponse
from django.shortcuts import render, redirect
from geopy.geocoders import Nominatim

from .forms import RegistrationForm
from .models import Topic, Post, Patient, DosageHistory


def index(request):
    return render(request, 'biomedic_app/index.html')


def generate_unique_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def find_nearest_hospital(patient_location, hiv_status, tb_status, hepatitis_status):
    # Replace with the actual healthcare API endpoint
    api_url = ('https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJrTLr-GyuEmsRBfy61i59si0&fields'
               '=address_components&key=YOUR_API_KEY')

    # Prepare request parameters
    params = {
        'latitude': patient_location.latitude,
        'longitude': patient_location.longitude,
        'hiv_status': hiv_status,
        'tb_status': tb_status,
        'hepatitis_status': hepatitis_status,
    }

    # Make a request to the healthcare API

    from requests import get
    response = get(api_url, params=params)

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
                    patient.hepatitis_status
                )

                if nearest_hospital:
                    patient.nearest_hospital = nearest_hospital

            patient.save()
            return render(request, 'biomedic_app/registration.html', {'patient': patient})
    else:
        form = RegistrationForm()

    return render(request, 'biomedic_app/registration.html', {'form': form})


def login_view(request):
    # Your login view logic here
    return render(request, 'biomedic_app/login.html')

def medication(request):
    if request.method == 'POST':
            # Get patient information based on the logged-in user
            patient = Patient.objects.get(user=request.user)

            # Get dosage history for the patient
            dosage_history = DosageHistory.objects.filter(patient=patient)

            # Get a list of medications based on dosage history
            medications = [dh.medication for dh in dosage_history]

            # Render the order medication form with patient information, dosage history, and medication details
            return render(request, 'order_medication.html',
                          {'patient': patient, 'dosage_history': dosage_history, 'medications': medications})
    else:

    # Implement medication ordering logic
    return render(request, 'biomedic_app/medication.html')


def counseling(request):
    # Implement counseling access logic
    return render(request, 'biomedic_app/counseling.html')


def forum(request):
    Topic.objects.all()
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
