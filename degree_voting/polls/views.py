from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
    }
    return render(request, 'polls/home.html', context)


def degrees(request):
    context = {
        'title': 'Degrees',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
    }
    return render(request, 'polls/degrees.html', context)


def teachers_ranking(request):
    context = {
        'title': 'Teachers Ranking',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
    }
    return render(request, 'polls/ranking.html', context)


def subjects_ranking(request):
    context = {
        'title': 'Subject Ranking',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
    }
    return render(request, 'polls/ranking.html', context)
