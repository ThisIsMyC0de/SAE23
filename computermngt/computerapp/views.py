from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def machine_list_view(request):
    from computerapp.models import Machine
    machines = Machine.objects.all()
    context={
        'machines' : machines,
    }
    return render(request, 'computerapp/machine_list.html', context)
