# Generated by Django 4.1.2 on 2023-02-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blogs_tex2_alter_blogs_text3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='blog_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.blogcategory'),
        ),
    ]
