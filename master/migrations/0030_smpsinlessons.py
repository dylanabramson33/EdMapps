# Generated by Django 2.0.6 on 2019-06-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0029_auto_20190628_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMPsInLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField()),
                ('SMP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SMPsInLessons', to='master.SMPText')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SMPsInLessons', to='master.Master')),
                ('unionkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SMPsInLessons', to='master.Lesson')),
            ],
        ),
    ]
