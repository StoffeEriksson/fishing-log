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
            return redirect('log_list')
    else:
        form = FishLogForm()
    return render(request, 'logs/log_form.html', {'form': form})

@login_required
def log_list(request):
    logs = FishLog.objects.filter(user=request.user)
    total = sum(log.fish_count for log in logs)
    return render(request, 'logs/log_list.html', {'logs': logs, 'total': total})