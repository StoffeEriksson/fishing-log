from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, DateField
from django.db.models.functions import TruncMonth
from django.utils.safestring import mark_safe
from django.contrib import messages
from .models import FishingSession, Catch
from .forms import FishingSessionForm, CatchFormSet
import json
import calendar


# Home page (public)
def home(request):
    """Render the public home page."""
    return render(request, 'logs/home.html')


# Dashboard for logged-in users
def dashboard(request):
    """Display user's dashboard with recent sessions and total fish count."""
    sessions = FishingSession.objects.filter(user=request.user).order_by(
        '-date'
    )
    total_fish = sum(
        catch.count for session in sessions for catch in session.catches.all()
    )
    last_session = sessions.first()

    return render(
        request,
        'logs/dashboard.html',
        {
            'sessions': sessions,
            'total': total_fish,
            'last_session': last_session,
        },
    )


# Log a new fishing session
def log_fish_session(request):
    """Allow user to log a new fishing session and related catches."""
    if request.method == 'POST':
        session_form = FishingSessionForm(request.POST)
        formset = CatchFormSet(request.POST)

        if session_form.is_valid() and formset.is_valid():
            session = session_form.save(commit=False)
            session.user = request.user
            session.save()

            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get(
                    'DELETE', False
                ):
                    catch = form.save(commit=False)
                    catch.session = session
                    catch.save()
            messages.success(
                request, "Fishing session has been logged successfully!"
            )
            return redirect('session_stats')
    else:
        session_form = FishingSessionForm()
        formset = CatchFormSet(queryset=Catch.objects.none())

    return render(
        request,
        'logs/log_fishing_session.html',
        {
            'session_form': session_form,
            'formset': formset,
        },
    )


# List all fishing sessions and display stats
def session_list(request):
    """Show all user's sessions along with species and monthly statistics."""
    sessions = FishingSession.objects.filter(user=request.user).order_by(
        '-date'
    )

    species_data = (
        Catch.objects.filter(session__user=request.user)
        .values('species')
        .annotate(total=Sum('count'))
        .order_by('species')
    )
    species_labels = [entry['species'].title() for entry in species_data]
    species_counts = [entry['total'] for entry in species_data]

    monthly_data = (
        Catch.objects.filter(session__user=request.user)
        .annotate(month=TruncMonth('session__date', output_field=DateField()))
        .values('month')
        .annotate(total=Sum('count'))
        .order_by('month')
    )
    month_labels = [
        calendar.month_name[entry['month'].month] for entry in monthly_data
    ]
    month_counts = [entry['total'] for entry in monthly_data]

    return render(
        request,
        'logs/session_list.html',
        {
            'sessions': sessions,
            'species_labels': mark_safe(json.dumps(species_labels)),
            'species_counts': mark_safe(json.dumps(species_counts)),
            'month_labels': mark_safe(json.dumps(month_labels)),
            'month_counts': mark_safe(json.dumps(month_counts)),
        },
    )


# Show stats for the most recent session
def session_stats(request):
    """Display detailed stats for the user's latest session."""
    last_session = FishingSession.objects.filter(user=request.user).order_by(
        '-id'
    ).first()
    catches = last_session.catches.all() if last_session else []
    total = sum(c.count for c in catches) if last_session else 0

    return render(
        request,
        'logs/session_stats.html',
        {
            'last_session': last_session,
            'catches': catches,
            'total': total,
        },
    )


# Delete all user's fishing sessions
def reset_stats(request):
    """Remove all fishing sessions for the current user."""
    FishingSession.objects.filter(user=request.user).delete()
    return redirect('dashboard')


# Delete user account
def delete_account(request):
    """Delete the current user account permanently."""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'logs/delete_account.html')


# Edit an existing fishing session
def edit_fishing_session(request, session_id):
    """Edit a specific fishing session and its catches."""
    session = get_object_or_404(FishingSession, id=session_id, user=request.user)

    if request.method == 'POST':
        print("Form submitted")
        session_form = FishingSessionForm(request.POST, instance=session)
        formset = CatchFormSet(request.POST, queryset=session.catches.all())

        if session_form.is_valid() and formset.is_valid():
            print("Form valid")
            session_form.save()
            for form in formset:
                if form.cleaned_data:
                    catch = form.save(commit=False)
                    catch.session = session
                    if form.cleaned_data.get('DELETE'):
                        if catch.pk:
                            catch.delete()
                    else:
                        catch.save()
            messages.success(request, "Fishing session updated successfully!")
            return redirect('session_list')
        else:
            print("FORMULAR ERROR:")
            print(session_form.errors)
            print(formset.errors)
    else:
        session_form = FishingSessionForm(instance=session)
        formset = CatchFormSet(queryset=session.catches.all())

    return render(
        request,
        'logs/edit_fishing_session.html',
        {
            'session_form': session_form,
            'formset': formset,
        },
    )
