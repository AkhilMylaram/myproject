from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import SampleForm

@csrf_exempt
def form_view(request):
    if request.method=='POST':
        data=SampleForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            email=data.cleaned_data['email']
            return render(request,'form_app/form.html',{
                'name':name,
                'email':email
            })

    form = SampleForm()
    return render(request, 'form_app/form.html', {'form': form})

