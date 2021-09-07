from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="User")
    SUBJECT_CHOICES = [
        # Full Year
        ('COMP2019', 'Software Engineering Group Project'),
        ('COMP2038', 'Algorithms Correctness and Efficiency'),
        ('COMP3043', 'Development Experience'),
        ('COMP3044', 'Industrial Experience'),
        ('COMP3047', 'Schools Experience'),
        ('COMP3025', 'Individual Dissertation'),

        # Autumn
        ('COMP1027', 'Computer Fundamentals'),
        ('COMP1017', 'Mathematics for Computer Scientists'),
        ('COMP1028', 'Programming and Algorithms'),
        ('COMP1030', 'Systems and Architecture'),
        ('COMP2042', 'Developing Maintainable Software'),
        ('COMP2035', 'Operating Systems and Concurrency'),
        ('COMP3041', 'Professional Ethics in Computing'),
        ('COMP3033', 'Software Quality Assurance'),
        ('COMP3032', 'Compilers'),
        ('COMP3038', 'Machine Learning'),
        ('COMP3040', 'Mobile Device Programming'),
        ('COMP4082', 'Autonomous Robotic Systems'),

        # Spring
        ('COMP1029', 'Programming Paradigms'),
        ('COMP1031', 'Databases and Interfaces'),
        ('COMP1023', 'Software Engineering'),
        ('COMP1032', 'Fundamentals of Artificial Intelligence'),
        ('COMP1045', 'Mathematics for Computer Scientists 2'),
        ('COMP2024', 'Artificial Intelligence Methods (20cr)'),
        ('COMP2039', 'Artificial Intelligence Methods (10cr)'),
        ('COMP2040', 'Languages and Computation'),
        ('COMP2034', 'C++ Programming'),
        ('COMP2025', 'Introduction to Human Computer Interaction'),
        ('COMP2032', 'Introduction to Image Processing'),
        ('COMP2041', 'Software Specification'),
        ('COMP3028', 'Computer Security'),
        ('COMP3029', 'Computer Vision'),
        ('COMP3046', 'Parallel Computing'),
        ('COMP3042', 'Fundamentals of Information Visualisation'),
        ('COMP3045', 'Information Visualisation Project')
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default="Subject")
    enquiry = models.CharField(max_length=50)
    details = models.TextField(max_length=200, null=True, blank=True)
    # documents = models.FileField(default=False)
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['time']

# class Subjects(models.Model):
#     enquiry = models.ForeignKey(Enquiry, null=True, on_delete=models.SET_NULL)
