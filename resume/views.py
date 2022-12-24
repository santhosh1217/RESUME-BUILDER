from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from resume.models import Collection


def form(request):
    return render(request, 'form1.html')


def home(request):
    return render(request, 'home.html')


def resume(request):
    use = request.POST.get('user1', '')
    hmail = request.POST.get('gmail', '')
    domain = request.POST.get('domain1', '')
    mobile = request.POST.get('mobile1', '')
    image = request.FILES.get('image1', 'images/.mp3.jpg')
    skill = request.POST.get('skill1', 'fresher')
    about = request.POST.get('about1', '')
    hobby = request.POST.get('hobby1', '')
    address = request.POST.get('address1', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    lang = request.POST.get('language', '')
    summary = request.POST.get('summary', '')
    project_name = request.POST.get('project', '')
    decs = request.POST.get('project_desc', '')
    clg = request.POST.get('college', '')
    cgp = request.POST.get('cgpa', '')
    pout = request.POST.get('passout','')

    obj = Collection()
    obj.name = use
    obj.mail = hmail
    obj.domain = domain
    obj.mobile = mobile
    obj.image = image
    obj.skill = skill
    obj.about = about
    obj.hobby = hobby
    obj.address = address
    obj.password = password1
    obj.project_name = project_name
    obj.project_description = decs
    obj.language = lang
    obj.summary = summary
    obj.college = clg
    obj.cgpa = cgp
    obj.passout = pout

    if password1 == password2:
        if Collection.objects.filter(name=use).exists():
            messages.info(request,"Try different username")
            return render(request, 'form1.html')
        else:
            obj.save()
            User.objects.create_user(username=use, password=password1)
            b = Collection.objects.get(name=use)
            l = convert(b.skill)
            la = convert(b.language)
            d = {'name': b.name, 'mail': b.mail, 'domain': b.domain, 'mobile': b.mobile, 'image': b.image,
                 'skill': l,
                 'about': b.about, 'hobby': b.hobby, 'address': b.address,
                 'project': b.project_name, 'project_decs': b.project_description
                , 'language': la, 'summary': b.summary, 'college': b.college, 'year': b.passout, 'cgpa': b.cgpa}
            return render(request, 'resume.html', d)            

    else:
        messages.info(request, "password not matching")
        return render(request, 'form1.html')


def valid(request):
    name = request.POST['user']
    password = request.POST['password']
    if Collection.objects.filter(name=name).exists():
        b = Collection.objects.get(name=name)
        print(b.mail)
        if b.password == password:
            l = convert(b.skill)
            la = convert(b.language)
            print(l)
            print(b.image)
            d = {'name': b.name, 'mail': b.mail, 'domain': b.domain, 'mobile': b.mobile, 'image': b.image,
                 'skill': l,
                 'about': b.about, 'hobby': b.hobby, 'address': b.address,
                 'project': b.project_name, 'project_decs': b.project_description
                , 'language': la, 'summary': b.summary, 'college': b.college, 'year': b.passout, 'cgpa': b.cgpa}
            return render(request, 'resume.html', d)
        else:

            messages.info(request, "wrong password")
            return render(request, 'home.html')

    else:
        messages.info(request, "user not found")
        return render(request, 'home.html')


def convert(string):
    li = list(string.split(" "))
    return li
