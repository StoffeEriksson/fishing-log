from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FishLog
from .forms import FishLogForm

# Create your views here.
@login_required
def log_fish_session(request):
    if request.method == 'POST':
        form = FishLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('dashboard')
    else:
        form = FishLogForm()
    return render(request, 'logs/log_form.html', {'form': form})

@login_required
def dashboard(request):
    logs = FishLog.objects.filter(user=request.user)
    total = sum(log.fish_count for log in logs)
    return render(request, 'logs/dashboard.html', {'logs': logs, 'total': total})


def home_or_dashboard(request):
    if request.user.is_authenticated:
        return dashboard(request)  # visar dashboard.html
    return render(request, 'logs/home.html')  # visar home.html
