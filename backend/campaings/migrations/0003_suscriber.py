# Generated by Django 4.0.5 on 2022-06-06 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaings', '0002_alter_campaing_options_campaing_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campaing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaings.campaing')),
            ],
            options={
                'verbose_name': 'Suscriber',
                'verbose_name_plural': 'Suscribers',
                'ordering': ('-subscribed_at',),
            },
        ),
    ]