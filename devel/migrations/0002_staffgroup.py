# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('devel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('sort_order', models.PositiveIntegerField()),
                ('member_title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'ordering': ('sort_order',),
            },
            bases=(models.Model,),
        ),
    ]
