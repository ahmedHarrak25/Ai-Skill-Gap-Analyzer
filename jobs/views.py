# jobs/views.py
from django.shortcuts import render 
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# NEW VIEW FOR THE DASHBOARD PAGE
def job_dashboard_view(request):
    return render(request, 'jobs/job_dashboard.html')