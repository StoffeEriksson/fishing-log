from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FishLog
from .forms import FishLogForm

# Log a fish session
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
    return render(request, 'logs/log_forms.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    logs = FishLog.objects.filter(user=request.user).order_by('-date')
    total = sum(log.fish_count for log in logs)
    last_session = logs.first()  # Assuming most recent
    return render(request, 'logs/dashboard.html', {
        'logs': logs,
        'total': total,
        'last_session': last_session
    })

# Home page
def home(request):
    return render(request, 'logs/home.html')

# Session list
@login_required
def session_list(request):
    sessions = FishLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'logs/session_list.html', {'sessions': sessions})

# Session stats
@login_required
def session_stats(request):
    last_session = FishLog.objects.filter(user=request.user).order_by('-date').first()
    return render(request, 'logs/session_stats.html', {'last_session': last_session})