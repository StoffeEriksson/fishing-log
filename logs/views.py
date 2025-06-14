from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, DateField
from django.db.models.functions import TruncMonth
from django.utils.safestring import mark_safe
from django.contrib import messages
from .models import FishingSession, Catch
from .forms import FishingSessionForm, CatchFormSet
import json
import calendar

# Home page
def home(request):
    return render(request, 'logs/home.html')

# Dashboard – visar senaste pass och total fångst
@login_required
def dashboard(request):
    sessions = FishingSession.objects.filter(user=request.user).order_by('-date')
    total_fish = sum(
        catch.count for session in sessions for catch in session.catches.all()
    )
    last_session = sessions.first()

    return render(request, 'logs/dashboard.html', {
        'sessions': sessions,
        'total': total_fish,
        'last_session': last_session
    })

# Logga nytt fiskepass
@login_required
def log_fish_session(request):
    if request.method == 'POST':
        session_form = FishingSessionForm(request.POST)
        formset = CatchFormSet(request.POST)

        if session_form.is_valid() and formset.is_valid():
            session = session_form.save(commit=False)
            session.user = request.user
            session.save()

            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    catch = form.save(commit=False)
                    catch.session = session
                    catch.save()

            messages.success(request, "Fishing session has been logged successfully!")  # 👈 Lägg till detta
            return redirect('session_stats')
    else:
        session_form = FishingSessionForm()
        formset = CatchFormSet(queryset=Catch.objects.none())

    return render(request, 'logs/log_fishing_session.html', {
        'session_form': session_form,
        'formset': formset,
    })

# Visa alla sessioner och grafer
@login_required
def session_list(request):
    sessions = FishingSession.objects.filter(user=request.user).order_by('-date')

    # Fångst per art
    species_data = (
        Catch.objects
        .filter(session__user=request.user)
        .values('species')
        .annotate(total=Sum('count'))
        .order_by('species')
    )
    species_labels = [entry['species'].title() for entry in species_data]
    species_counts = [entry['total'] for entry in species_data]

    # Fångst per månad (fixat!)
    monthly_data = (
        Catch.objects
        .filter(session__user=request.user)
        .annotate(month=TruncMonth('session__date', output_field=DateField()))
        .values('month')
        .annotate(total=Sum('count'))
        .order_by('month')
    )
    month_labels = [calendar.month_name[entry['month'].month] for entry in monthly_data]
    month_counts = [entry['total'] for entry in monthly_data]

    return render(request, 'logs/session_list.html', {
        'sessions': sessions,
        'species_labels': mark_safe(json.dumps(species_labels)),
        'species_counts': mark_safe(json.dumps(species_counts)),
        'month_labels': mark_safe(json.dumps(month_labels)),
        'month_counts': mark_safe(json.dumps(month_counts)),
    })

# Statistik för senaste passet
@login_required
def session_stats(request):
    last_session = FishingSession.objects.filter(user=request.user).order_by('-id').first()
    catches = last_session.catches.all() if last_session else []
    total = sum(c.count for c in catches) if last_session else 0

    return render(request, 'logs/session_stats.html', {
        'last_session': last_session,
        'catches': catches,
        'total': total
    })

# Nollställ statistik
@login_required
def reset_stats(request):
    FishingSession.objects.filter(user=request.user).delete()
    return redirect('dashboard')