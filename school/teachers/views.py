from django.shortcuts import render,redirect
from .models import Teacher

# Create your views here.

def teachers_list(request):
    teacher = Teacher.objects.all()

    return render(request, "index.html",{ "allTeacher":teacher})

def add_teachers(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get('image')

        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )

        teacher.save()

        return redirect("all-teacher")
    return render(request,'index.html')