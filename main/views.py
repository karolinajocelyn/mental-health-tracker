from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306221762',
        'name': 'Karolina Jocelyn',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)