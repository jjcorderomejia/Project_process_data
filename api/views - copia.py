from urllib.request import Request
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import trips
import json
import csv
import MySQLdb
import requests
# Create your views here.

class TripView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        trip=list(trips.objects.values())
        if len(trip) > 0:
            data={'message':"Successo", 'trip':trip}
        else:
            data={'message':"Trips not found ..."}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        trips.objects.create(region=jd['region'], origin_coord=jd['origin_coord'], destination_coord=jd['destination_coord'], datetime=jd['datetime'], datasource=jd['datasource'])
        data={'message':"Success"}
        return JsonResponse(data)

    def put(self, request):
        pass

    def delete(self, request):
        pass



class load_trips_class(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        mydb = MySQLdb.connect(host="127.0.0.1", user="root", password='', database='jobsity')

        with open("C:/trips.csv") as csv_file:
            csvfile = csv.reader(csv_file, delimiter=',')
            all_value = []
            query = "insert into `api_trips`(`region`, `origin_coord`, `destination_coord`, `datetime`, `datasource`) values (%s, %s, %s, %s, %s) "
            mycursor = mydb.cursor()
            for row in csvfile:
                value = (row[0], row[1], row[2], row[3], row[4])
                all_value.append(value)

                if csvfile.line_num % 10000 == 0:
                    #query = "insert into `api_trips`(`region`, `origin_coord`, `destination_coord`, `datetime`, `datasource`) values (%s, %s, %s, %s, %s) "

                    #mycursor = mydb.cursor()
                    mycursor.executemany(query, all_value)
                    mydb.commit()            
                    all_value.clear()
                    print(len(all_value))                       

        
        #mycursor = mydb.cursor()
        mycursor.executemany(query, all_value)
        mydb.commit() 
        mycursor.close()
        mydb.close()       
        data={'message':"Successful"}  
        return JsonResponse(data)

