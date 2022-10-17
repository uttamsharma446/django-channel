from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
import json
import time
from .thread import CreateStudentThread
# Create your views here.
async def home(request):
     
    return render(request,'home.html')


def generate_student_data(request):
  total=request.GET.get('total',0)

  CreateStudentThread(int(total)).start()
  return JsonResponse({"status":200})

  