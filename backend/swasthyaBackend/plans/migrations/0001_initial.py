# Generated by Django 4.1.10 on 2023-08-31 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255)),
                ('goal', models.CharField(choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('cardio_fitness', 'Cardio Fitness')], max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255)),
                ('goal', models.CharField(choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('balanced_diet', 'Balanced Diet')], max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('guidelines', models.TextField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainerprofile')),
            ],
        ),
    ]