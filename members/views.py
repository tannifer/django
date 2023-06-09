from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import Member
from .forms import MemberForm


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))



def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def json(request):
    mymembers = Member.objects.all().values()
    return JsonResponse({"data" : list(mymembers)})

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context,request))

def home_view(request):
    context = {}

    form = MemberForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,"all_members.html", context)

