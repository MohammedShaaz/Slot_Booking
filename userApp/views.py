from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from userApp.models import User_registraton
from userApp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class UserReg(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



# class VeiwAll(APIView):
#     def get(self,request):
#         users = User_registraton.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

class Avalability(APIView):

    def find_slots(self,user):
        time_from = user.FromTime
        time_to = user.ToTime
        time_list = []
        y = time_from
        for x in range(time_to - time_from):
            set_time = [y,y+1]

            time_list.append(set_time)

            y += 1
        return time_list

    def available(self,ilist,clist):
        available_list = [x for x in ilist if x in clist]
        # print(available_list)
        return (available_list)


    def get(self,request):
        interviewer_id = request.GET["interviewer"]
        candidate_id = request.GET["candidate"]

        interviewer = User_registraton.objects.get(id = interviewer_id)
        # print(interviewer)
        candidate = User_registraton.objects.get(id = candidate_id)
        # print(candidate)

        interviewer_slots = self.find_slots(interviewer)
        # print(interviewer_slots)
        candidate_slots = self.find_slots(candidate)
        # print(candidate_slots)

        available_slots = self.available(interviewer_slots,candidate_slots)

        # print(available_slots)
        return Response(available_slots)

