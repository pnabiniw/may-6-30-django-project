from django.shortcuts import render, redirect
from myapp.models import Student, ClassRoom


def template_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        department = request.POST.get("department")
        class_name = request.POST.get("classroom")  # class_name = "One" which is a str
        try:
            classroom_obj = ClassRoom.objects.get(name=class_name)
        except:
            classroom_obj = None
        Student.objects.create(name=name, age=age, department=department, classroom=classroom_obj)
        return redirect("students")
    context = {
        "title": "Add Student",
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "form/template_form.html", context=context)
