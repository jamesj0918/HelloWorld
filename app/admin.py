from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Guest_book)
admin.site.register(Comment)
admin.site.register(Member)
admin.site.register(Album)
admin.site.register(Friend)
admin.site.register(Friend_list)
admin.site.register(Photo_comment)
admin.site.register(Keyword)
admin.site.register(Music)
admin.site.register(Home_guest)

#Admin site에 DB에 있는 데이터를 확인,수정이 가능하도록 모델을 등록한다.
