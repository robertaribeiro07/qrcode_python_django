from django.shortcuts import render
from qrcode import *
import time


ts = time.time()
result=str(ts)

data=None
def home(request):
    filename= "qrcode_generator/static/image/" + result + ".png"
    global data
    
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.box_size=10
        img.save(filename)
        
    return render(request,"home.html",{'data':data,'filename':filename }) 

  