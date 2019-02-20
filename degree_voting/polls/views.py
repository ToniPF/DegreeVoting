from django.shortcuts import render
from .polls_models.qualification import Qualification
from .polls_models.assessment import Assessment



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

    teachers = Qualification.objects.all()

    worst_qualifies, best_qualifies = get_top_qualifying(5, teachers)

    context = {
        'title': 'Teachers Ranking',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
        'worst_qualifies': worst_qualifies,
        'best_qualifies': best_qualifies,
    }
    return render(request, 'polls/teachers_ranking.html', context)


def subjects_ranking(request):

    subjects = Assessment.objects.all()

    worst_qualifies, best_qualifies = get_top_qualifying(5, subjects)

    context = {
        'title': 'Subject Ranking',
        'header': 'polls/header.html',
        'footer': 'polls/footer.html',
        'worst_qualifies': worst_qualifies,
        'best_qualifies': best_qualifies,
    }

    return render(request, 'polls/subjects_ranking.html', context)


def get_top_qualifying(maximum, listed):

    worst_qualifies, best_qualifies = [], []

    # Check for maximum qualified items
    if listed:
        length = len(listed)
        if length >= maximum:
            worst_qualifies = (reversed(listed.order_by('mark')[-maximum:]))
            best_qualifies = listed.order_by('mark')[:maximum]
        else:
            worst_qualifies = (reversed(listed.order_by('mark')))
            best_qualifies = (listed.order_by('mark'))

    return worst_qualifies, best_qualifies
