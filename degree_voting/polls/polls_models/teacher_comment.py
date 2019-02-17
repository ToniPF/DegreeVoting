from . import comment, teacher


class TeacherComment(comment.Comment):

    teacher_id = comment.models.ForeignKey(teacher.Teacher, on_delete=comment.models.CASCADE)
