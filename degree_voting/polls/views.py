from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .polls_models.course import Course
from .polls_models.qualification import Qualification
from .polls_models.assessment import Assessment
from .polls_models.description import HomeDescription
from .polls_models.degree import Degree
from .polls_models.subject import Subject


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


class AssessmentDetailView(DetailView):
    context_object_name = 'subject_with_grade'
    template_name = 'polls/assessment_detail.html'

    def get_queryset(self):
        self.subject = get_object_or_404(Subject, code=self.kwargs['pk'])
        return Assessment.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        context = super(AssessmentDetailView, self).get_context_data(**kwargs)
        context['subject'] = self.subject
        context['title'] = self.subject.code
        return context


class DegreeDetailView(ListView):
    context_object_name = 'subjects_by_course'
    template_name = 'polls/degree_info.html'

    def get_queryset(self):
        self.degree = get_object_or_404(Degree, id=self.kwargs['pk'])
        return Course.objects.filter(degree_id=self.degree)

    def get_context_data(self, **kwargs):
        context = super(DegreeDetailView, self).get_context_data(**kwargs)

        self.assessments, self.qualifications = [], []
        for course in context['subjects_by_course']:
            self.assessments.append(list(Assessment.objects.filter(subject_id=course.subject_id)))
            self.qualifications.append(Qualification.objects.filter(subject_id=course.subject_id))

        context['worst_subjects'], context['best_subjects'] = get_top_for_degrees(3, self.assessments)
        context['worst_teachers'], context['best_teachers'] = get_top_for_degrees(3, self.qualifications)

        context['title'] = self.degree.title
        return context


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
            worst_qualifies = listed.order_by('mark')[:maximum]
            best_qualifies = list(reversed(listed.order_by('mark')))[:maximum]
        else:
            worst_qualifies = listed.order_by('mark')
            best_qualifies = list(reversed(listed.order_by('mark')))

    return worst_qualifies, best_qualifies


def get_top_for_degrees(maximum, listed):
    if len(listed) < maximum:
        return listed, listed
    listed.sort(key=lambda x: x[0].mark)
    return listed[:3], list(reversed(listed[len(listed) - 3:]))
