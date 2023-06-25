from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Student


# request is the object of HttpRequest class
# views must return HttpResponse object
def home(request):
    # response = HttpResponse()
    # response.content = "Hello from Django"
    # return response
    html_content = """
    <html>
    <head>
        <title>test project</title>
    </head>
    <body>
    <h1> Hello Django </h1>
    </body>
    </html>
    """
    return HttpResponse(html_content)


def template_test(request):
    context = {
        "students": Student.objects.all(),
        "title": "Students"
    }
    return render(request, "myapp/index.html", context=context)

# In DTL (Django Templating Language) we have, variables, tags and filters


def name_message(request, name):
    print(request.method)   # GET , POST
    # request.method
    # request.user
    # request.GET
    # request.POST
    # request.FILES
    last_name = request.GET.get("last_name")
    names = {
        "ram": "Ram Bahadur ",
        "hari": "Hari Prasad ",
        "shyam": "Shyam Krishna "
    }
    try:
        full_name = names[name.lower()]
        if last_name:
            full_name += last_name.title()
    except KeyError:
        return HttpResponseNotFound("Name not found")
    return HttpResponse(f"Hello I'm {full_name}")


def json_view(request):
    response = {
        "name": "Harry",
        "age": 23,
        "id": 2
    }
    return JsonResponse(response)


def inheritance_page1(request):
    return render(request, "myapp/home.html")


def inheritance_page2(request):
    return render(request, "myapp/page2.html")


def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")


def db_data(request):
    context = {
        "students": Student.objects.all()  # ORM
    }
    return render(request, template_name="myapp/db_data.html", context=context)


def students(request):
    context = {
        "students": Student.objects.all(),
        "title": "Students"
    }
    return render(request, "students.html", context=context)

# ORMs (Object Relational Mapping)
# Using ORM we don't need to apply raw sql queries to CRUD in a db table. We
# get queries in python language to CRUD in the table.

# Read
    # Student.objects.all()
    # Student.objects.get(id=1)
    # Student.objects.filter(id=2)

# Create
    # Student.objects.create(name="Kane", age=21, department="CS")

# Update
    # Student.objects.filter(id=1).update(age=25)

# Delete
    # Student.objects.filter(id=1).delete()
