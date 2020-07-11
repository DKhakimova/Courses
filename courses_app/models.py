from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, form_data):
        errors = {}
        if len(form_data['name']) < 5:
            errors['name'] = 'Course name should be at least 5 characters'
        if len(form_data['description']) < 15:
            errors['description'] = 'Description should be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()