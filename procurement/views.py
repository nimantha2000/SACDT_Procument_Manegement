from django.shortcuts import render, redirect
from .models import Procurement, Step

def admin_dashboard(request):
    procurements = Procurement.objects.all()
    return render(request, 'admin_dashboard.html', {'procurements': procurements})

def create_procurement(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        procurement = Procurement.objects.create(name=name, description=description)
        return redirect('admin_dashboard')
    return render(request, 'create_procurement.html')

def view_procurement(request, id):
    procurement = Procurement.objects.get(id=id)
    steps = Step.objects.filter(procurement=procurement).order_by('step_number')
    return render(request, 'view_procurement.html', {'procurement': procurement, 'steps': steps})

def continue_step(request, id, step):
    procurement = Procurement.objects.get(id=id)
    if request.method == 'POST':
        file = request.FILES['file']
        Step.objects.create(procurement=procurement, step_number=step, file=file)
        procurement.current_step = step
        procurement.save()
        return redirect('admin_dashboard')
    return render(request, 'continue_step.html', {'procurement': procurement, 'step': step})

def user_dashboard(request):
    procurements = Procurement.objects.all()
    return render(request, 'user_dashboard.html', {'procurements': procurements})
