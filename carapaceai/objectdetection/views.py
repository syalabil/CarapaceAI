from django.views import View
from django.shortcuts import render
from .models import *

# Create your views here.
class HomePageView(View):
    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,'objectdetection/home.html') 


class LiveCameraView(View):
    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,'objectdetection/livefeed.html') 

def upload_video_file(request):
    file = request.FILES.get("fileName")
    print(file.name + "reached file name")
    video = Video(video=file)
    video.save()
    return file

    # fss = FileSystemStorage()
    # filename = fss.save(file.name, file)
    # url = fss.url(filename)
    # img = StaffImage(image=file)
    # img.save()
    # print(img.image.url)
    # count = StaffImage.objects.all().count()
    # print(str(count))
    # os.chdir("D:\Desktop\ppecomputervisiongithub\ppecomputervision\PPE Model\PPE Model\yolov5-master")
    # os.system("python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source D:/Desktop/ppecomputervisiongithub/ppecomputervision/ppecomputervision" + str(img.image.url) + " --save-txt --save-conf")