from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
    }
    return render(request, 'polls/home.html', context)
