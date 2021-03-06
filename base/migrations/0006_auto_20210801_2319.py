# Generated by Django 3.2.5 on 2021-08-01 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_auto_20210720_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='subject',
            field=models.CharField(choices=[('COMP2019', 'Software Engineering Group Project'), ('COMP2038', 'Algorithms Correctness and Efficiency'), ('COMP3043', 'Development Experience'), ('COMP3044', 'Industrial Experience'), ('COMP3047', 'Schools Experience'), ('COMP3025', 'Individual Dissertation'), ('COMP1027', 'Computer Fundamentals'), ('COMP1017', 'Mathematics for Computer Scientists'), ('COMP1028', 'Programming and Algorithms'), ('COMP1030', 'Systems and Architecture'), ('COMP2042', 'Developing Maintainable Software'), ('COMP2035', 'Operating Systems and Concurrency'), ('COMP3041', 'Professional Ethics in Computing'), ('COMP3033', 'Software Quality Assurance'), ('COMP3032', 'Compilers'), ('COMP3038', 'Machine Learning'), ('COMP3040', 'Mobile Device Programming'), ('COMP4082', 'Autonomous Robotic Systems'), ('COMP1029', 'Programming Paradigms'), ('COMP1031', 'Databases and Interfaces'), ('COMP1023', 'Software Engineering'), ('COMP1032', 'Fundamentals of Artificial Intelligence'), ('COMP1045', 'Mathematics for Computer Scientists 2'), ('COMP2024', 'Artificial Intelligence Methods (20cr)'), ('COMP2039', 'Artificial Intelligence Methods (10cr)'), ('COMP2040', 'Languages and Computation'), ('COMP2034', 'C++ Programming'), ('COMP2025', 'Introduction to Human Computer Interaction'), ('COMP2032', 'Introduction to Image Processing'), ('COMP2041', 'Software Specification'), ('COMP3028', 'Computer Security'), ('COMP3029', 'Computer Vision'), ('COMP3046', 'Parallel Computing'), ('COMP3042', 'Fundamentals of Information Visualisation'), ('COMP3045', 'Information Visualisation Project')], default='Subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
