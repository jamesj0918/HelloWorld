from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

# Create your models here

class AccountManager(BaseUserManager): #장고 기본제공 로그인 사용하기 (장고 공식문서 참조코드)
    def create_user(self,username,password=None):
	    user=self.model(
		    username=username,
	    )
	    user.set_password(password)
	    user.save(using=self._db)
	    return user

    def create_superuser(self, username, password=None): #슈퍼유저 생성 (장고 공식문서 참조코드)
	    user=self.create_user(
		    username=username,
		    password=password,
	    )

	    user.is_admin=True
	    user.is_superuser=True
	    user.is_active=True
	    user.save(using=self._db)
	    return user

class TimeStampedModel(models.Model):#아이디 생성시간, 최근 접속시간 (장고 공식문서 참조코드)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
	    abstract=True

class Member(AbstractBaseUser, TimeStampedModel): # 멤버 모델 정의
    username = models.CharField(max_length=100, unique=True) #사용자 이름
    profile_img = models.CharField(max_length = 200) #프로필 이미지의 이름
    line_intro = models.CharField(max_length = 30, default = '표시할 내용이 없습니다.')# 한줄 소개
    self_intro = models.TextField(max_length = 800, default = '표시할 내용이 없습니다.' )# 프로필 자기소개
    gender = models.CharField(max_length = 100, default = '설정 안함')# 성별
    blood_type = models.CharField(max_length = 100, default = '설정 안함')# 혈액형
    age = models.CharField(max_length = 100, default = '설정 안함')# 나이
    bday = models.CharField(max_length = 100, default = '설정 안함')# 생일
    weight = models.CharField(max_length = 100, default = '설정 안함')# 몸무게
    height = models.CharField(max_length = 100, default = '설정 안함')# 키
    phone_num = models.CharField(max_length = 100, default = '설정 안함')# 전화번호

    #10문10답에서 사용자가 저장한 답변
    A1 = models.CharField(max_length=200)
    A2 = models.CharField(max_length=200)
    A3 = models.CharField(max_length=200)
    A4 = models.CharField(max_length=200)
    A5 = models.CharField(max_length=200)
    A6 = models.CharField(max_length=200)
    A7 = models.CharField(max_length=200)
    A8 = models.CharField(max_length=200)
    A9 = models.CharField(max_length=200)
    A10 = models.CharField(max_length=200)

    # 장고 기본제공 로그인 사용(공식문서 참조 코드)
    is_admin = models.BooleanField(default=False)# 어드민 유저권한
    is_superuser=models.BooleanField(default=False)# 슈퍼유저 권한

    objects=AccountManager()

    USERNAME_FIELD='username'

    def __str__(self):
	    return "username: "+self.username
    @property
    def is_staff(self):
	    return self.is_admin
    def has_module_perms(self, app_label):
	    if self.is_active and self.is_superuser:
		    return True
	    return self.is_admin

    def has_perm(self, perm, obj=None):
	    if self.is_active and self.is_superuser:
		    return True
	    return self.is_admin

class Home_guest(models.Model): # 홈화면 일촌평 모델 정의
    home_book = models.CharField(max_length = 100, default = '표시할 컨텐츠가 없습니다.')# 일촌평 본문
    src_user = models.CharField(max_length = 100, default = '없음')# 작성한 사람
    dest_user = models.CharField(max_length = 100, default =  '없음')# 작성한 홈페이지의 주인

class Guest_book(models.Model):# 방명록 모델 정의
    guest_book_text = models.CharField(max_length = 200)# 방명록 본문
    reg_time = models.DateTimeField(auto_now_add = True)# 작성시간 -> 자동으로 현재시간 저장
    src_user = models.CharField(max_length = 200)# 작성한 사람
    dest_user = models.CharField(max_length = 200)#작성한 홈페이지의 주인
    src_user_profile_img = models.CharField(max_length = 200)# 작성한 사람의 프로필 이미지 사진

class Album(models.Model):# 앨범 모델 정의
    album_text = models.CharField(max_length = 200)# 앨범 게시물 본문
    album_title = models.CharField(max_length = 200)#앨범 게시문 제목
    reg_time = models.DateTimeField(auto_now_add = True)# 작성시간 -> 자동으로 현재시간 저장
    src_user = models.CharField(max_length = 200)# 작성한 사람
    img_name = models.CharField(max_length = 200)# 업로드한 이미지의 이름 저장

class Comment(models.Model):#댓글 모델 정의
    guest_book_comment = models.CharField(max_length = 200, null = False)# 댓글 본문
    reg_time = models.DateTimeField(auto_now_add = True)#작성 시간
    src_user = models.CharField(max_length = 200)#작성한 사람
    dest_user = models.CharField(max_length = 200)#작성한 홈페이지의 주인
    guest_text = models.CharField(max_length = 200)# 댓글달 방명록의 본문

class Photo_comment(models.Model):#앨범의 댓글 모델 정의
    album_comment = models.CharField(max_length = 200, null = False)#댓글 본문
    reg_time = models.DateTimeField(auto_now_add = True)# 작성시간 -> 자동으로 현재시간 저장
    src_user = models.CharField(max_length = 200)#작성한 사람
    dest_user = models.CharField(max_length = 200)#작성한 홈페이지의 주인
    img_name = models.CharField(max_length = 200)# 댓글달 게시물의 이미지 이름

class Friend(models.Model):#친구요청 모델 정의
    friend_req = models.CharField(max_length = 200)#요청을 보낸 친구
    friend_rcv = models.CharField(max_length = 200)#요청을 받은 친구

class Friend_list(models.Model):#친구관계 모델 정의 (한 모델안에 있는 username 두명은 친구관계임)
    f1 = models.CharField(max_length = 200)#친구 1
    f2 = models.CharField(max_length = 200)#친구 2

class Keyword(models.Model):#키워드 모델 정의
    src_user = models.CharField(max_length = 200)# 작성한 사람
    key = models.CharField(max_length = 200)#키워드 본문
    stat = models.CharField(max_length = 200)#키워드 단계

class Music(models.Model):#음악 모델 정의 (반드시 어드민계정으로 처음에 필드 한개 생성 필수)
    music_name = models.CharField(max_length = 200, default = '아이유-잠 못 드는 밤 비는 내리고')#현재 플레이할 음악의 이름
