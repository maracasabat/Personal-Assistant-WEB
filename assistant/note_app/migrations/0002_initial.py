# Generated by Django 4.2 on 2023-04-13 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notetotag',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note_app.note'),
        ),
        migrations.AddField(
            model_name='notetotag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note_app.tag'),
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(through='note_app.NoteToTag', to='note_app.tag'),
        ),
    ]