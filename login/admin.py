from django.contrib import admin
from .models import User,Submissions, Task, Subject

# Register your models here.
admin.site.register(User)
admin.site.register(Submissions)
admin.site.register(Task)
admin.site.register(Subject)

# admin.site.register(Student)
# admin.site.register(Teacher)
