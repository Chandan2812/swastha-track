# Generated by Django 4.1.10 on 2023-08-31 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorkoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exercises', models.TextField()),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.workoutplan')),
            ],
        ),
        migrations.CreateModel(
            name='UserNutritionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meals', models.TextField()),
                ('caloric_intake', models.PositiveIntegerField(help_text='Calories consumed')),
                ('nutrition_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.nutritionplan')),
            ],
        ),
    ]