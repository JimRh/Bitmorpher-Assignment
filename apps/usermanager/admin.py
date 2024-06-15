from django.contrib import admin
from .models import User,APILog
# Register your models here.
admin.site.register(User)
admin.site.register(APILog)