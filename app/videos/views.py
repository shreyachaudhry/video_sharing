from django.shortcuts import render, redirect  
from videos.forms import VideoForm  
from videos.models import Video

# Create your views here.
def vid(request):  
    if request.method == "POST":  
        form = VideoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = VideoForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    videos = Video.objects.all()  
    return render(request,"show.html",{'employees':videos})  
def destroy(request, id):  
    video = Video.objects.get(id=id)  
    video.delete()  
    return redirect("/show")  