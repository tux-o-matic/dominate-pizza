# Generated by Django 2.0.6 on 2018-06-15 10:48

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
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('currency', models.CharField(max_length=2)),
                ('organic', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('currency', models.CharField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_on', models.DateTimeField(auto_now_add=True)),
                ('shipped_on', models.DateTimeField(auto_now_add=True)),
                ('menus', models.ManyToManyField(to='pizza.Menu')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.Food')),
                ('bacon', models.BooleanField(default=False)),
                ('cheese', models.BooleanField(default=False)),
                ('steaks', models.SmallIntegerField(default=0)),
                ('others', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('pizza.food',),
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.Food')),
                ('size', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('alcohol', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('pizza.food',),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.Food')),
            ],
            options={
                'abstract': False,
            },
            bases=('pizza.food',),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.Food')),
                ('calzone', models.BooleanField()),
                ('diameter', models.SmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('pizza.food',),
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza.Food')),
            ],
            options={
                'abstract': False,
            },
            bases=('pizza.food',),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizza.Topping'),
        ),
        migrations.AddField(
            model_name='order',
            name='burgers',
            field=models.ManyToManyField(to='pizza.Burger'),
        ),
        migrations.AddField(
            model_name='order',
            name='drinks',
            field=models.ManyToManyField(to='pizza.Drink'),
        ),
        migrations.AddField(
            model_name='order',
            name='meals',
            field=models.ManyToManyField(to='pizza.Meal'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(to='pizza.Pizza'),
        ),
        migrations.AddField(
            model_name='menu',
            name='burgers',
            field=models.ManyToManyField(to='pizza.Burger'),
        ),
        migrations.AddField(
            model_name='menu',
            name='drinks',
            field=models.ManyToManyField(to='pizza.Drink'),
        ),
        migrations.AddField(
            model_name='menu',
            name='meals',
            field=models.ManyToManyField(to='pizza.Meal'),
        ),
        migrations.AddField(
            model_name='menu',
            name='pizzas',
            field=models.ManyToManyField(to='pizza.Pizza'),
        ),
    ]