from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from myapp.models import Student, ClassRoom, StudentProfile
from django.db import transaction
from django.views.generic import CreateView, TemplateView, ListView

from .forms import StudentForm, StudentModelForm


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


def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            age = form.cleaned_data.get("age")
            dept = form.cleaned_data.get("department")
            Student.objects.create(name=name, age=age, department=dept)
            Student.objects.create(**form.cleaned_data)
            # Student.objects.create(**form.cleaned_data)
            return redirect("students")
    context = {
        "title": "Add Student",
        "form": StudentForm()
    }
    return render(request, "form/student_form.html", context=context)


def student_model_form(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("students")
    context = {
        "title": "Add Student",
        "form": StudentModelForm()
    }
    return render(request, "form/student_form.html", context=context)


class PortfolioView(TemplateView):
    template_name = "myapp/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Portfolio"
        return context

    # def get(self, request, *args, **kwargs):
    #     # Write sth extra logic
    #     count = StudentTotalCount.objects.all().count()
    #     count += 1
    #     mail()
    #     return super().get(request, *args, **kwargs)


class StudentListView(ListView):
    model = Student
    template_name = "students.html"
    context_object_name = "students"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Student List"
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = "form/student_form.html"
    success_url = reverse_lazy("students")