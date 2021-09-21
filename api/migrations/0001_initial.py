# Generated by Django 3.2.7 on 2021-09-20 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_tag', models.CharField(max_length=10)),
                ('category_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=30)),
                ('subcategory_details', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Leve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=30)),
                ('score_type', models.CharField(max_length=30)),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='function_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.function'),
        ),
    ]
