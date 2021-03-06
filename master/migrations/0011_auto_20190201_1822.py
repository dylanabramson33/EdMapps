# Generated by Django 2.0.6 on 2019-02-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_auto_20181219_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardCodesAndVerbiage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=255)),
                ('standardWording', models.CharField(blank=True, max_length=255)),
                ('majorSuportingOrAdditional', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StandardsInLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField()),
                ('standardCode', models.CharField(blank=True, max_length=255)),
                ('focusDevelopingOrApplied', models.CharField(blank=True, max_length=255)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StandardsInLessons', to='master.Master')),
                ('unionkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StandardsInLessons', to='master.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='standardcodesandverbiage',
            name='standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StandardCodesAndVerbiage', to='master.StandardsInLessons'),
        ),
    ]
