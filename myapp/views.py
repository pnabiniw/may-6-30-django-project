from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


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
    return render(request, "myapp/index.html")


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
