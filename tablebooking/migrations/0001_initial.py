# Generated by Django 3.0.7 on 2020-08-25 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('rmn', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('rmn', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderby', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Order Confirmed', 'Order Confirmed'), ('Order Pending', 'Order Pending'), ('Order Cancelled', 'Order Cancelled')], max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Customer')),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Dishes')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dishes',
            name='rname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Restaurant'),
        ),
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Customer')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tablebooking.Restaurant')),
            ],
        ),
    ]
