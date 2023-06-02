from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse


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
        "students": [
            {"name": "Jane", "id": 1, "age": 23, "active": True},
            {"name": "Harry", "id": 2, "age": 21, "active": False},
            {"name": "Jon", "id": 3, "age": 20, "active": True}
        ],
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
