from . import comment, subject


class SubjectComment(comment.Comment):

    subject_id = comment.models.ForeignKey(subject.Subject, on_delete=comment.models.CASCADE)
