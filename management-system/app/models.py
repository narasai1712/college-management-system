from django.db import models

class Departments(models.Model):
    Department_id = models.AutoField(primary_key=True)
    Department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Department_name


class Teachers(models.Model):
    Teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Courses(models.Model):
    Course_id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.Course_name


class Students(models.Model):
    Student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Classes(models.Model):
    Class_id = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    room_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Course} - {self.semester} {self.year}"


class Enrollments(models.Model):
    Enrollment_id = models.AutoField(primary_key=True)
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.Student} enrolled in {self.Class} with grade {self.grade}"


class Exams(models.Model):
    Exam_id = models.AutoField(primary_key=True)
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=20)
    exam_date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"Exam for {self.Class} on {self.exam_date}"