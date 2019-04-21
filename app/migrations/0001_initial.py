# Generated by Django 2.0.6 on 2018-06-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('profile_img', models.CharField(max_length=200)),
                ('line_intro', models.CharField(default='표시할 내용이 없습니다.', max_length=30)),
                ('self_intro', models.TextField(default='표시할 내용이 없습니다.', max_length=800)),
                ('gender', models.CharField(default='설정 안함', max_length=100)),
                ('blood_type', models.CharField(default='설정 안함', max_length=100)),
                ('age', models.CharField(default='설정 안함', max_length=100)),
                ('bday', models.CharField(default='설정 안함', max_length=100)),
                ('weight', models.CharField(default='설정 안함', max_length=100)),
                ('height', models.CharField(default='설정 안함', max_length=100)),
                ('phone_num', models.CharField(default='설정 안함', max_length=100)),
                ('A1', models.CharField(max_length=200)),
                ('A2', models.CharField(max_length=200)),
                ('A3', models.CharField(max_length=200)),
                ('A4', models.CharField(max_length=200)),
                ('A5', models.CharField(max_length=200)),
                ('A6', models.CharField(max_length=200)),
                ('A7', models.CharField(max_length=200)),
                ('A8', models.CharField(max_length=200)),
                ('A9', models.CharField(max_length=200)),
                ('A10', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_text', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=200)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('src_user', models.CharField(max_length=200)),
                ('img_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_book_comment', models.CharField(max_length=200)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('src_user', models.CharField(max_length=200)),
                ('dest_user', models.CharField(max_length=200)),
                ('guest_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_req', models.CharField(max_length=200)),
                ('friend_rcv', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Friend_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Guest_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_book_text', models.CharField(max_length=200)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('src_user', models.CharField(max_length=200)),
                ('dest_user', models.CharField(max_length=200)),
                ('src_user_profile_img', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Home_guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_book', models.CharField(default='표시할 컨텐츠가 없습니다.', max_length=100)),
                ('src_user', models.CharField(default='없음', max_length=100)),
                ('dest_user', models.CharField(default='없음', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_user', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('stat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(default='아이유-잠 못 드는 밤 비는 내리고', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_comment', models.CharField(max_length=200)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('src_user', models.CharField(max_length=200)),
                ('dest_user', models.CharField(max_length=200)),
                ('img_name', models.CharField(max_length=200)),
            ],
        ),
    ]
