from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .polls_models.course import Course
from .polls_models.qualification import Qualification
from .polls_models.assessment import Assessment
from .polls_models.description import HomeDescription
from .polls_models.degree import Degree


def home(request):
    context = {
        'title': 'Home',
        'description': HomeDescription.objects.filter(display=True).first(),
    }
    return render(request, 'polls/home.html', context)


def degrees(request):
    context = {
        'title': 'Degrees',
        'degrees': Degree.objects.all(),
    }
    return render(request, 'polls/degrees.html', context)


class DegreeDetailView(DetailView):
    context_object_name = 'degree'
    template_name = 'polls/degree_info.html'

    def get_queryset(self):
        self.degree = get_object_or_404(Degree, id=self.kwargs['pk'])
        return Course.objects.filter(degree_id=self.degree)


def teachers_ranking(request):

    teachers = Qualification.objects.all()

    worst_qualifies, best_qualifies = get_top_qualifying(5, teachers)

    context = {
        'title': 'Teachers Ranking',
        'worst_qualifies': worst_qualifies,
        'best_qualifies': best_qualifies,
    }
    return render(request, 'polls/teachers_ranking.html', context)


def subjects_ranking(request):

    subjects = Assessment.objects.all()

    worst_qualifies, best_qualifies = get_top_qualifying(5, subjects)

    context = {
        'title': 'Subject Ranking',
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
