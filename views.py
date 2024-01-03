
# biomedic_app/views.py
from django.shortcuts import render, redirect
from .models import Patient, Topic, Post
from django.http import HttpResponse
def index(request):
    return render(request, 'biomedic_app/index.html')
def registration(request):

    if request.method == 'POST':
        # Retrieve data from the form
        patient_name = request.POST.get('patient_name')
        hiv_status = request.POST.get('hiv_status')
        tb_status = request.POST.get('tb_status')

        # Create a new patient object and save to the database
        new_patient = Patient(patient_name=patient_name, hiv_status=hiv_status, tb_status=tb_status)
        new_patient.save()

        # Redirect to a success page or wherever you want
        return HttpResponse("Patient registered successfully!")
    # Implement patient registration logic
    return render(request, 'biomedic_app/registration.html')

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

def education(request):
    # Implement educational platform logic
    return render(request, 'biomedic_app/education.html')

# Create your views here.
