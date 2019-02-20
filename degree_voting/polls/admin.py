from django.contrib import admin

from .polls_models.degree import Degree
from.polls_models.course import Course
from .polls_models.subject import Subject
from .polls_models.assessment import Assessment

from .polls_models.teacher import Teacher
from .polls_models.qualification import Qualification

from .polls_models.subject_comment import SubjectComment
from .polls_models.teacher_comment import TeacherComment

from .polls_models.description import HomeDescription


# Register your polls_models here.

# Registers related with University structure
admin.site.register(Degree)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Assessment)

# Registers related with University Teachers
admin.site.register(Teacher)
admin.site.register(Qualification)

# Registers related with Comments
admin.site.register(SubjectComment)
admin.site.register(TeacherComment)

admin.site.register(HomeDescription)

