# Generated by Django 3.2.23 on 2024-02-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroff',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agroff',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agroff',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agroff',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agroff',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfp',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfp',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfp',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfpcart',
            name='count',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfpreqmain',
            name='date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cfpreqmain',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfpreqmain',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfpreqsub',
            name='count',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cfpreqsub',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='mdate',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='chat',
            name='mtime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='rdate',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='rtime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='usertype',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='marketprice',
            name='item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='marketprice',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policy',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policy',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policy',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='count',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productreqmain',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productreqmain',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productreqmain',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productreqsub',
            name='count',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productreqsub',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='count',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='techwing',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='techwing',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='techwing',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trendnewstech',
            name='date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trendnewstech',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trendnewstech',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]