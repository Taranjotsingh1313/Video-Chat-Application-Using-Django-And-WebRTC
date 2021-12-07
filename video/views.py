from django.shortcuts import redirect, render
from .models import Chat
# Create your views here.
def index(request):
    if request.method == 'POST':
        room = request.POST['room']
        get_room = Chat.objects.filter(room_name=room)
        if get_room:
            c = get_room[0]
            number = c.allowed_users
            if int(number) < 2:
                number = 2
                return redirect(f'/video/{room}/join/')
        else:
            create = Chat.objects.create(room_name=room,allowed_users=1)
            if create:
                return redirect(f'/video/{room}/created/')
    return render(request,'index.html')

def video(request,room,created):
    return render(request,'video.html',{'room':room,'created':created})