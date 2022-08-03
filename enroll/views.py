from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def update(request, id):
    if request.method == 'POST':
        pk = User.objects.get(pk=id)
        sf = StudentRegistration(request.POST, instance=pk)
        if sf.is_valid:
            sf.save()
    else:
        pa = User.objects.get(pk=id)
        sf = StudentRegistration(instance=pa)
    return render(request, 'update.html', {'form':sf})

#get all data and submit data
def show_all(request):
    if request.method == 'POST':
        sf = StudentRegistration(request.POST)
        if sf.is_valid:
            # na = sf.changed_data['name']
            # ema = sf.changed_data['email']
            # pas = sf.changed_data['password']
            # print(pas)
            # user = User(name=na, email=ema, password=pas)
            # user.save()
            sf.save()
            sf = StudentRegistration()
    else :
        sf = StudentRegistration()
    std = User.objects.all()
    return render(request, 'addshow.html', {'forms':sf, 'std':std} )

def delete(request, id):
    if request.method == "POST":
        pa = User.objects.get(pk=id)
        pa.delete()
        return redirect('/')