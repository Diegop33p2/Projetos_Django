# Generated by Django 5.0 on 2024-03-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treino_academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pernas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_treino', models.DateField()),
                ('agachamneto', models.TextField()),
                ('leg_press', models.TextField()),
                ('extensora', models.TextField()),
                ('rack', models.TextField()),
                ('bulgaro', models.TextField()),
                ('stiff', models.TextField()),
                ('cadeira_flexora', models.TextField()),
                ('mesa_flexora', models.TextField()),
                ('ele_pelvica', models.TextField()),
                ('aga_sumo', models.TextField()),
                ('abdutora', models.TextField()),
                ('adutora', models.TextField()),
                ('panturilha', models.TextField()),
            ],
        ),
    ]