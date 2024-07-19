from django.shortcuts import render
from django.http import JsonResponse
    
from rest_framework import viewsets
from rest_framework.response import Response

from calendar import monthrange
from datetime import datetime

from .models import Plant
from .serializers import PlantSerializer

class PlantViewSet(viewsets.ReadOnlyModelViewSet):
    #A simple ViewSet for listing or retrieving all plants.
    
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()

def get_schedule(request):
    #Return a watering schedule for the current month
    
    #Get current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year
    first_day, num_days = monthrange(current_year, current_month)
    
    schedule = [[] for _ in range(num_days)] #Create an array with length = number of days in the month
    
    #Iterate through every plant of the database:
    plants = Plant.objects.all()
    for plant in plants.values('name', 'species', 'watering_frequency', 'id'):
        #Find all multiples of the watering frequency up to 31
        i = 1;
        freq = plant['watering_frequency']
        while i < num_days:
            #append the plant to the list on the specified day
            schedule[i-1].append({'id': plant['id'], 'name': plant['name'], 'species': plant['species']})
            i += freq
    
    #Respond with the generated watering schedule
    return JsonResponse(data={"month": current_month, "year": current_year, "first_day": first_day, "schedule":schedule})