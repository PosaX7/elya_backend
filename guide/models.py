from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_related_exercises(self):
        return Exercise.objects.filter(course=self)

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    instruction = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exercises')
    solution = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Library(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='libraries/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
