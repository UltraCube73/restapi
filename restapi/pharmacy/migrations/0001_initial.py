# Generated by Django 3.2.5 on 2021-07-25 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=30)),
                ('m_manufacuter_city', models.CharField(max_length=20)),
                ('m_price', models.IntegerField()),
                ('m_pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_set', to='pharmacy.pharmacy')),
            ],
        ),
    ]
