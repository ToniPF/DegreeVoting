from polls.polls_models.course import Course
from polls.polls_models.degree import Degree
from polls.polls_models.subject import Subject
from polls.polls_models.teacher import Teacher
from polls.polls_models.qualification import Qualification
from polls.polls_models.assessment import Assessment
from polls.polls_models.subject_comment import SubjectComment
from polls.polls_models.teacher_comment import TeacherComment
import os


def make_database():
    # CREC QUE TOT AIXO NO ES NECESARI
    # ********************************
    path = os.getcwd()
    tokens = path.split('/')
    path = tokens[0]
    tokens = tokens[1:]
    for token in tokens:
        path += '/' + token

    add_degrees(path + '/data/degrees.data')


def add_degrees(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_subject(params[0], params[1], params[2], params[3])


def add_degree(title, ects, description, university):
    degree = Degree(title, ects, description, university)
    degree.save()


def add_subject(code, title, ects, description):
    subject = Subject(code, title, ects, description)
    subject.save()


def add_assessment(mark, difficulty, amount, subject):
    assessment = Assessment(mark, difficulty, amount, subject)
    assessment.save()


def add_subject_comment(subject_id, comment):
    subject_comment = SubjectComment(subject_id, comment)
    subject_comment.save()


def add_teacher(name, email):
    teacher = Teacher(name, email)
    teacher.save()


def add_qualification(mark, amount, subject_id, teacher_id):
    qualification = Qualification(mark, amount, subject_id, teacher_id)
    qualification.save()


def add_teacher_qualification(teacher_id, comment):
    teacher_comment = TeacherComment(teacher_id, comment)
    teacher_comment.save()


def add_course(degree_id, subject_id, course):
    degree = Degree.objects.filter(degree_id)
    subject = Subject.objects.filter(subject_id)
    new_course = Course(degree, subject, Course.COURSE_LIST[course-1])
    new_course.save()
