from django.contrib import admin
from .models import Submissions, User, Subject, Task

# Register your models here.
admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(Subject)
admin.site.register(Submissions)