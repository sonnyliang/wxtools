# Generated by Django 2.2 on 2020-09-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(blank=True, db_column='\ufeffID', max_length=255, null=True)),
                ('billno', models.CharField(blank=True, db_column='BillNo', max_length=255, null=True)),
                ('billdate1', models.CharField(blank=True, db_column='Billdate1', max_length=255, null=True)),
                ('shopcode', models.CharField(blank=True, db_column='Shopcode', max_length=255, null=True)),
                ('goodscode', models.CharField(blank=True, max_length=255, null=True)),
                ('qty', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.CharField(blank=True, max_length=255, null=True)),
                ('vipcardno', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('holiday', models.CharField(blank=True, max_length=255, null=True)),
                ('orderamount', models.CharField(blank=True, max_length=255, null=True)),
                ('orderqty', models.CharField(blank=True, max_length=255, null=True)),
                ('amounttag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'BusinessOrder',
                'managed': False,
            },
        ),
    ]
