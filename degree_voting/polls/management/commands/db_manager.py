import os
from django.core.management.base import BaseCommand
from polls.polls_models.course import Course
from polls.polls_models.degree import Degree
from polls.polls_models.subject import Subject
from polls.polls_models.teacher import Teacher
from polls.polls_models.qualification import Qualification
from polls.polls_models.assessment import Assessment
from polls.polls_models.subject_comment import SubjectComment
from polls.polls_models.teacher_comment import TeacherComment


class Command(BaseCommand):
    def handle(self, *args, **options):
        make_database()


def make_database():
    path = os.getcwd()
    add_degrees(path + '/data/degrees.data')
    add_subjects(path + '/data/subjects.data')
    add_courses(path + '/data/courses.data')
    add_teachers(path + '/data/teachers.data')
    add_qualifications(path + '/data/qualifications.data')
    add_assessments(path + '/data/assessments.data')


def add_degrees(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_degree(i, params[0], params[1], params[2], params[3])


def add_subjects(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_subject(params[0], params[1], params[2], params[3])


def add_courses(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_course(params[0], params[1], params[2])


def add_teachers(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            params = line.split('|')
            add_teacher(i, params[0], params[1])


def add_qualifications(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_qualification(params[0], params[1], params[2], params[3])


def add_assessments(filename):
    _add_with_four_params(add_assessment, filename)


def _add_with_four_params(func, filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            func(params[0], params[1], params[2], params[3])


def add_degree(index, title, ects, description, university):
    degree = Degree(title=title, ects=ects, description=description, university=university)
    degree.id = index
    degree.save()


def add_subject(code, title, ects, description):
    subject = Subject(code=code, title=title, ects=ects, description=description)
    subject.save()


def add_assessment(mark, difficulty, amount, subject_id):
    subject = Subject.objects.get(code=subject_id)
    assessment = Assessment(mark=mark, difficulty=difficulty, amount=amount, subject=subject)
    assessment.save()


def add_subject_comment(subject_id, comment):
    subject_comment = SubjectComment(subject_id=subject_id, comment=comment)
    subject_comment.save()


def add_teacher(index, name, email):
    teacher = Teacher(name=name, email=email)
    teacher.id = index
    teacher.save()


def add_qualification(mark, amount, teacher_id, subject_id):
    subject = Subject.objects.get(code=subject_id)
    teacher = Teacher.objects.get(id=teacher_id)
    qualification = Qualification(mark=mark, amount=amount, subject_id=subject, teacher_id=teacher)
    qualification.save()


def add_teacher_comment(teacher_id, comment):
    teacher_comment = TeacherComment(teacher_id=teacher_id, comment=comment)
    teacher_comment.save()


def add_course(degree_id, subject_id, course):
    degree = Degree.objects.get(id=degree_id)
    subject = Subject.objects.get(code=subject_id)
    new_course = Course(degree_id=degree, subject_id=subject, course=course)
    new_course.save()
