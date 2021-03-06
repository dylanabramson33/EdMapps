# Generated by Django 2.0.6 on 2019-06-28 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0025_auto_20190618_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicVocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField()),
                ('word', models.CharField(blank=True, max_length=255)),
                ('definition', models.CharField(blank=True, max_length=255)),
                ('defIfFoundInGradeLevel', models.CharField(blank=True, max_length=255)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AcademicVocabulary', to='master.Master')),
                ('unionkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AcademicVocabulary', to='master.Lesson')),
            ],
        ),
    ]
