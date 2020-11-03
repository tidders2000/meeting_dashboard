
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
# from .models import Meeting, Visitors, Guests, Apologies
# from .forms import meeting_model_form, status_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .utils import render_to_pdf
from .models import Hr, Action, Finance, Issue, Rag
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime


def finance(request):
    data = Finance.objects.all()
    actions = Action.objects.filter(area='Finance', closed=False)
    issues = Issue.objects.filter(area='Finance', closed=False)
    rags = Rag.objects.all()
    risks = Risk.objects.filter(area='Finance')
    object = {
        'data': data,
        'actions': actions,
        'issues': issues,
        'rags': rags,
        'risks': risks


    }
    return render(request, 'finance.html', object)


def hr(request):
    data = Hr.objects.all()
    actions = Action.objects.filter(area='HR', closed=False)
    issues = Issue.objects.filter(area='HR', closed=False)
    rags = Rag.objects.all()
    risks = Risk.objects.filter(area='HR')
    object = {
        'data': data,
        'actions': actions,
        'issues': issues,
        'rags': rags,
        'risks': risks


    }
    return render(request, 'hr.html', object)


def clinical(request):

    actions = Action.objects.filter(area='Clinical', closed=False)
    issues = Issue.objects.filter(area='Clinical', closed=False)
    rags = Rag.objects.all()
    risks = Risk.objects.filter(area='Clinical')
    object = {

        'actions': actions,
        'issues': issues,
        'rags': rags,
        'risks': risks


    }
    return render(request, 'clinical.html', object)


def buildings(request):

    actions = Action.objects.filter(area='Buildinga', closed=False)
    issues = Issue.objects.filter(area='Buildings', closed=False)
    rags = Rag.objects.all()
    risks = Risk.objects.filter(area='Buildings')
    object = {

        'actions': actions,
        'issues': issues,
        'rags': rags,
        'risks': risks


    }
    return render(request, 'building.html', object)


def actions_ud(request, pk):
    act = get_object_or_404(Action, pk=pk)

    act.closed = True
    act.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def issues_ud(request, pk):
    iss = get_object_or_404(Issue, pk=pk)

    iss.closed = True
    iss.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def issues(request):
    if request.method == "POST":
        form = add_issues(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.error(request, "Issue Added")
    else:
        form = add_issues()
    return render(request, 'issues.html', {'form': form})


def actions(request):
    if request.method == "POST":
        form = add_actions(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.error(request, "Action Added")
    else:
        form = add_actions()
    return render(request, 'actions.html', {'form': form})


def risklog(request):
    if request.method == "POST":
        form = add_risk(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.error(request, "Risk Added")
    else:
        form = add_risk()
    return render(request, 'risklog.html', {'form': form})


def rag(request):

    if request.method == "POST":
        pk = request.POST.get('pk')
        status = request.POST.get('tl')
        rag = get_object_or_404(Rag, pk=pk)
        rag.rag = status
        rag.save()
        messages.error(request, "Rag Updated")
    rag = Rag.objects.all()
    return render(request, 'rag.html', {'rag': rag})


def charts(request):
    hr_form = add_hr()
    fin_form = add_finance()
    object = {
        'hr_form': hr_form,
        'fin_form': fin_form
    }
    return render(request, 'charts.html', object)


def minutes(request):
    return render(request, 'minutes.html')


def pdf(request):

    meeting = 'Practice Ops Meeting'
    attendees = User.objects.all()
    meet_date = datetime.now()
    issues = Issue.objects.filter(date=meet_date, closed=True)
    attendees = User.objects.all()
    risks = Risk.objects.all()
    actions = Action.objects.filter(closed=False)
    data = {'meeting': meeting, 'attendees': attendees,
            'meet_date': meet_date, 'issues': issues, 'actions': actions, 'risks': risks, }

    pdf = render_to_pdf('pdf/agenda.html', data)

    return HttpResponse(pdf, content_type='application/pdf')
