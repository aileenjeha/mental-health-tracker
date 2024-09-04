from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165761',
        'name': 'Aileen Josephine Halim',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)