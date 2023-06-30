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


def student_update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        department = request.POST.get("department")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        pp = request.FILES.get("pp")
        class_name = request.POST.get("classroom")
        try:
            classroom_obj = ClassRoom.objects.get(name=class_name)
        except:
            classroom_obj = None
        Student.objects.filter(id=id).update(name=name, age=age, department=department, classroom=classroom_obj)
        try:
            sp = StudentProfile.objects.get(student_id=id)
        except:
            pass
        else:
            sp.address = address
            sp.email = email
            sp.phone = phone
            if pp:
                sp.profile_picture = pp
            sp.save()
        return redirect("student_update", id=id)
    context = {
        "student": Student.objects.get(id=id),
        "title": "Student Update",
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "form/student_update.html", context=context)
