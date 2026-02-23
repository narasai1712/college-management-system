from django.contrib import admin
from .models import Departments, Teachers, Courses, Students, Classes, Enrollments, Exams


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('Department_id', 'Department_name')


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('Teacher_id', 'first_name', 'last_name', 'phone', 'Department')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('Course_id', 'Course_name', 'credits', 'Department')


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('Student_id', 'first_name', 'last_name', 'email', 'phone', 'Department')


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('Class_id', 'Course', 'teacher', 'semester', 'year', 'room_number')


@admin.register(Enrollments)
class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('Enrollment_id', 'Student', 'Class', 'enrollment_date', 'grade')


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
    list_display = ('Exam_id', 'Class', 'exam_type', 'exam_date', 'total_marks')