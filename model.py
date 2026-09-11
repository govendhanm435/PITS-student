from django.db import models


class Subject(models.Model):
    subject_code = models.CharField(
        max_length=20,
        unique=True
    )

    subject_name = models.CharField(
        max_length=150
    )

    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.CASCADE
    )

    semester = models.IntegerField(
        default=1
    )

    credits = models.IntegerField(
        default=3
    )

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"


class Mark(models.Model):
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    semester = models.IntegerField(
        default=1
    )

    internal_mark = models.IntegerField(
        default=0
    )

    external_mark = models.IntegerField(
        default=0
    )

    total_mark = models.IntegerField(
        default=0
    )

    grade = models.CharField (
        max_length=5,
        default=''
    )

    result = models.CharField(
        max_length=10,
        default=''
    )

    def __str__(self):
        return (
            f"{self.student.register_number} - "
            f"{self.subject.subject_code}"
        )
