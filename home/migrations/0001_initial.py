# Generated by Django 4.1.5 on 2023-01-25 10:38

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(max_length=1000)),
                ('image', models.ImageField(upload_to='blog')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
