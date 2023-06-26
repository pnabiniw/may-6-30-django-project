from django.shortcuts import render, redirect
from myapp.models import Student, ClassRoom, StudentProfile
from django.db import transaction


@transaction.atomic
def template_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        department = request.POST.get("department")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        pp = request.FILES.get("pp")
        class_name = request.POST.get("classroom")  # class_name = "One" which is a str
        try:
            classroom_obj = ClassRoom.objects.get(name=class_name)
        except:
            classroom_obj = None
        s = Student.objects.create(name=name, age=age, department=department, classroom=classroom_obj)
        StudentProfile.objects.create(phone=phone, email=email, address=address,
                                      profile_picture=pp, student=s)
        return redirect("students")
    context = {
        "title": "Add Student",
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "form/template_form.html", context=context)


def student_detail(request, id):
    context = {
        "student": Student.objects.get(id=id),
        "title": "Student Detail"
    }
    return render(request, "form/student_detail.html", context=context)
