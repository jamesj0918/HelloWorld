from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from django.core.files.storage import FileSystemStorage
from datetime import datetime
# Create your views hereself


def home(request): #홈화면
    if request.GET.get('user_name'):#GET Data가 존재해야 홈화면 진입 가능
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        guestbook_data = Guest_book.objects.filter(dest_user = request.GET.get('user_name')).first()
        album_data = Album.objects.filter(src_user = request.GET.get('user_name')).first()
        music_data = Music.objects.first()
        home_data = Home_guest.objects.filter(dest_user = request.GET.get('user_name'))
        return render(request, 'home.html', {'home_data':home_data, 'music_data':music_data, 'member_data' : member_data, 'guestbook_data': guestbook_data, 'album_data': album_data })
        #render 할 html파일, 넘겨줄 데이터
    elif request.user.username:#세션이 있다면 GET data에 세션정보를 넘겨주고 Redirect
        return HttpResponseRedirect('/home/?user_name=' + request.user.username)
    else:#세션이 없다면 로그인화면으로 Redirect
        return HttpResponseRedirect('/login/')

def add_profile_img(request):#프로필 이미지 추가
    if request.method == 'POST':#POST 데이터 받아올때
        img = request.FILES['profile_img']
        fs = FileSystemStorage()
        img_name = str(datetime.now()).replace(" ","").replace(":","").replace(".","") + '.jpg'#이미지이름에 공백, :, . 제거해서 저장
        filename = fs.save(img_name , img)
        uploaded_file_url = fs.url(filename)
        Member.objects.filter(username = request.user.username).update(profile_img = img_name)#현재 로그인된 유저 Member 모델에서 찾아서 프로필이미지의 이미지이름 바꿔줌
    return HttpResponseRedirect('/setting/?user_name='+request.user.username)#Redirect

def select_music(request):#음악 선택
    if request.method == 'POST':#POST 데이터 받아올때
        Music.objects.update(music_name = request.POST.get('music_select'))#플레이할 음악 이름 바꿈
    return HttpResponseRedirect('/home/?user_name=' + request.GET.get('user_name'))#Redirect

def add_line_intro(request):#한줄소개
    if request.method == 'POST':#POST 데이터 받아올떄
        Member.objects.filter(username = request.user.username).update(line_intro = request.POST.get('line_intro'))#현재 로그인된 유저 Member 모델에서 찾아서 한줄소개 바꿈
    return HttpResponseRedirect('/setting/?user_name='+request.user.username)#Redirect

def add_self_intro(request):#프로필 소개
    if request.method == 'POST':#POST 데이터 받아올때
        Member.objects.filter(username = request.user.username).update(self_intro = request.POST.get('self_intro'))#현재 로그인된 유저 Member 모델에서 찾아서 프로필소개 바꿈
    return HttpResponseRedirect('/setting/?user_name='+request.user.username)#Redirect

def add_gender(request):#성별추가
    #@@@@@이하 비슷한 과정은 생략@@@@@
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(gender = request.POST.get('gender'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_bloodtype(request):#혈액형 추가
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(blood_type = request.POST.get('blood_type'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_age(request):# 나이추가
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(age = request.POST.get('age'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_bday(request):# 생일 추가
    if request.method == 'POST':
        if request.POST.get('bday_year') == '알려고 하지 마세요!':
            Member.objects.filter(username = request.user.username).update(bday = request.POST.get('bday_year'))
        else:
            Member.objects.filter(username = request.user.username).update(bday = request.POST.get('bday_year') + ' 년 ' + request.POST.get('bday_month') + ' 월 ' + request.POST.get('bday_date') + ' 일')
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_weight(request):# 몸무게 추가
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(weight = request.POST.get('weight'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_height(request):# 키 추가
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(height = request.POST.get('height'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)

def add_phone_num(request):# 전화번호 추가
    if request.method == 'POST':
        Member.objects.filter(username = request.user.username).update(phone_num = request.POST.get('phone_num'))
    return HttpResponseRedirect('/basic_info/?user_name='+request.user.username)


def album(request):#앨범
    if request.user.username:
        album_data = Album.objects.all()
        comment_data = Photo_comment.objects.all()
        music_data = Music.objects.first()
        member_data = Member.objects.filter(username = request.user.username).first()
        return render(request, 'album.html', {'member_data':member_data, 'music_data':music_data, 'album_data' : album_data, 'comment_data' : comment_data})
    else:
        return HttpResponseRedirect('/login/')

def setting(request):#설정
    if request.user.username:
        if request.GET.get('user_name') != request.user.username:#현재 로그인한 사람의 홈페이지가 아니면 관리창을 들어갈 수 없음
            return HttpResponseRedirect('/home/?user_name='+str(request.GET.get('user_name')))
        member_data = Member.objects.filter(username = request.user.username).first()
        music_data = Music.objects.first()
        return render(request, 'setting.html',{'music_data':music_data, 'member_data': member_data})
    else:
        return HttpResponseRedirect('/login/')

def album_comment(request):#앨범 댓글 달기
    if request.method == 'POST':
        Photo_comment.objects.create(album_comment = request.POST.get('photo-comment-value'), src_user = request.user.username, dest_user = request.GET.get('user_name'), img_name = request.POST.get('img_name'))# 앨범 댓글 모델 생성
    return HttpResponseRedirect('/album/?user_name=' + str(request.GET.get('user_name')))

def basic_info(request):#기본정보 설정
    if request.user.username:
        music_data = Music.objects.first()
        return render(request, 'basic_information.html', {'music_data':music_data})
    else:
        return HttpResponseRedirect('/login/')

def guestbook(request):#방명록
    if request.user.username:
        if request.method == 'POST':
            Guest_book.objects.create(guest_book_text = request.POST.get('guest_book_text'), src_user = request.user.username, dest_user = request.GET.get('user_name'), src_user_profile_img = request.POST.get('writer_profile_img'))
        guest_article = Guest_book.objects.filter(dest_user = request.GET.get('user_name'))
        guest_comment = Comment.objects.all()
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        music_data = Music.objects.first()
        writer_data = Member.objects.filter(username = request.user.username).first()
        return render(request, 'guestbook.html', {'writer_data':writer_data, 'music_data':music_data, 'member_data' : member_data, 'guest_comment' :guest_comment, 'guest_article' :guest_article})
    else:
        return HttpResponseRedirect('/login/')

def guestcomment(request):#방명록 댓글 쓰기
    if request.method == 'POST':
        Comment.objects.create(guest_book_comment = request.POST.get("guest_book_comment"), src_user = request.user.username, guest_text = request.POST.get("guest_book_text"), dest_user = request.GET.get('user_name'))
    return HttpResponseRedirect('/guestbook/?user_name=' + str(request.GET.get('user_name')))

def album_delete(request):#앨범 삭제
    if request.GET.get('user_name') != request.user.username:#앨범 홈페이지 주인이 아니면 Redirect
        return HttpResponseRedirect('/album/?user_name='+str(request.GET.get('user_name')))
    if request.method == 'POST':
        Album.objects.filter(img_name = request.POST.get('img_name')).first().delete()#삭제
    return HttpResponseRedirect('/album/?user_name=' + str(request.GET.get('user_name')))

def guestbook_delete(request):#방명록 삭제
    if request.GET.get('user_name') != request.user.username:
        return HttpResponseRedirect('/guestbook/?user_name='+str(request.GET.get('user_name')))
    if request.method == 'POST':
        Guest_book.objects.filter(guest_book_text = request.POST.get('guest_book_text')).first().delete()
    return HttpResponseRedirect('/guestbook/?user_name=' +str(request.GET.get('user_name')))

def comment_delete(request):#방명록 댓글 삭제
    if request.method == 'POST':
        Comment.objects.filter(guest_book_comment = request.POST.get('guest_book_comment')).first().delete()
    return HttpResponseRedirect('/guestbook/?user_name=' + str(request.GET.get('user_name')))

def photo_comment_delete(request):#앨범 댓글 삭제
    if request.method == 'POST':
        Photo_comment.objects.filter(img_name = request.POST.get('img_name')).first().delete()
    return HttpResponseRedirect('/album/?user_name=' + str(request.GET.get('user_name')))


def join(request):# 회원 가입
    if request.method == 'POST':
        if Member.objects.filter(username = request.POST.get('user_id')).count() == 1:#아이디 중복 체크
            return HttpResponseRedirect('/join')
        else:
            member = Member.objects.create(username = request.POST.get('user_id'))
            member.set_password(request.POST.get('user_pw'))
            member.save()

            return HttpResponseRedirect('/login')
    return render(request, 'join.html')

def friend(request):#친구추가창
    if request.user.username:
        if request.GET.get('user_name') != request.user.username:#홈페이지 주인이 아니면 redirect
            return HttpResponseRedirect('/home/?user_name='+str(request.GET.get('user_name')))
        friend_request = Friend.objects.filter(friend_rcv = request.user.username)
        friend_data = None
        friend_list1 = Friend_list.objects.filter(f1 = request.user.username)
        friend_list2 = Friend_list.objects.filter(f2 = request.user.username)
        if request.method == 'POST':
            data = Member.objects.filter(username = request.POST.get("search_user"))
            if data.count() == 1:
                friend_data = data.first()
        music_data = Music.objects.first()
        return render(request, 'friend.html', {'music_data':music_data, 'friend_data' : friend_data, 'friend_request' : friend_request, 'friend_list1' : friend_list1, 'friend_list2' : friend_list2})
    else:
        return HttpResponseRedirect('/login/')

def friend_add(request):#친구요청
    data = request.POST.get("reqID")
    if request.method =='POST':
        Friend.objects.create(friend_req = request.user.username, friend_rcv = data)
    return HttpResponseRedirect('/friend/?user_name='+str(request.GET.get('user_name')))

def recieve_friend(request):#친구요청 수락
    if request.method == 'POST':
        Friend_list.objects.create(f1 = request.POST.get("req_answer"), f2= request.user.username)
        Friend.objects.filter(friend_rcv = request.user.username, friend_req = request.POST.get("req_answer")).delete()
    return HttpResponseRedirect('/friend/?user_name='+str(request.GET.get('user_name')))

def add_picture(request):#앨범 사진쓰기
    if request.user.username:
        if request.GET.get('user_name') != request.user.username:
            return HttpResponseRedirect('/album/?user_name='+request.GET.get('user_name'))

        if request.method == 'POST':
            img = request.FILES['album_imgs']
            fs = FileSystemStorage()
            img_name = str(datetime.now()).replace(" ","").replace(":","").replace(".","") + '.jpg'
            filename = fs.save(img_name , img)
            uploaded_file_url = fs.url(filename)
            Album.objects.create(src_user = request.user.username , album_text = request.POST.get('album_text'), album_title = request.POST.get('album_title'), img_name = img_name)
            return HttpResponseRedirect('/album/?user_name='+request.GET.get('user_name'))
        music_data = Music.objects.first()
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        return render(request, 'add_picture.html', {'member_data':member_data, 'music_data':music_data})
    else:
        return HttpResponseRedirect('/login/')

def profile_info(request):#프로필 기본정보
    if request.user.username:
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        music_data = Music.objects.first()
        return render(request, 'profile_info.html', {'music_data':music_data, 'member_data':member_data})
    else:
        return HttpResponseRedirect('/login/')

def profile_intro(request):#프로필 소개
    if request.user.username:
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        music_data = Music.objects.first()
        return render(request, 'profile_intro.html', {'music_data':music_data, 'member_data': member_data})
    else:
        return HttpResponseRedirect('/login/')

def profile_key(request):#프로필 키워드
    if request.user.username:
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        key_data = Keyword.objects.filter(src_user = request.GET.get('user_name')).all()
        music_data = Music.objects.first()
        return render(request, 'profile_key.html', {'music_data':music_data, 'member_data': member_data, 'key_data':key_data})
    else:
        return HttpResponseRedirect('/login/')

def profile_QnA(request):#프로필 10문 10답
    if request.user.username:
        music_data = Music.objects.first()
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        return render(request, 'profile_QnA.html', {'music_data':music_data, 'member_data':member_data})
    else:
        return HttpResponseRedirect('/login/')

def keyword(request):#키워드 추가화면
    if request.user.username:
        music_data = Music.objects.first()
        if request.GET.get('user_name') != request.user.username:
            return HttpResponseRedirect('/profile_key/?user_name='+str(request.GET.get('user_name')))
        return render(request, 'add_keyword.html', {'music_data':music_data})
    else:
        return HttpResponseRedirect('/login/')

def add_keyword(request):#키워드 추가하기
    if request.method == 'POST':
        Keyword.objects.create(src_user = request.user.username, key = request.POST.get('key'), stat = request.POST.get('stat'))
    return HttpResponseRedirect('/profile_key/?user_name='+str(request.GET.get('user_name')))

def delete_keyword(request):#키워드 전체 삭제
    if request.method == 'POST':
        Keyword.objects.filter(src_user = request.user.username).delete()
    return HttpResponseRedirect('/profile_key/?user_name='+str(request.GET.get('user_name')))

def add_QnA(request):#10문10답 수정화면
    if request.user.username:
        if request.GET.get('user_name') != request.user.username:
            return HttpResponseRedirect('/profile_QnA/?user_name='+request.GET.get('user_name'))
        member_data = Member.objects.filter(username = request.GET.get('user_name')).first()
        music_data = Music.objects.first()
        return render(request, 'add_QnA.html', {'music_data':music_data, 'member_data':member_data})
    else:
        return HttpResponseRedirect('/login/')

def submit_QnA(request):#10답 submit
    if request.method == 'POST':
        Member.objects.filter(username=request.user.username).update(A1 = request.POST.get('a1'),A2 = request.POST.get('a2'),A3 = request.POST.get('a3'),A4 = request.POST.get('a4'),A10 = request.POST.get('a10'))
        Member.objects.filter(username=request.user.username).update(A5 = request.POST.get('a5'),A6 = request.POST.get('a6'),A7 = request.POST.get('a7'),A8 = request.POST.get('a8'),A9 = request.POST.get('a9'))
    return HttpResponseRedirect('/profile_QnA/?user_name='+request.user.username)

def add_home_guest(request):#일촌평 추가
    if request.method == 'POST':
        Home_guest.objects.create(home_book = request.POST.get('home_book'), src_user = request.user.username, dest_user = request.GET.get('user_name'))
    return HttpResponseRedirect('/home/?user_name='+str(request.GET.get('user_name')))
