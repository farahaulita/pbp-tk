from django.contrib import admin
<<<<<<< HEAD
from .models import Submissions, User, Subject, Task

# Register your models here.
admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(Subject)
admin.site.register(Submissions)
=======
from .models import User,Submissions, Task, Subject

# Register your models here.
admin.site.register(User)
admin.site.register(Submissions)
admin.site.register(Task)
admin.site.register(Subject)

# admin.site.register(Student)
# admin.site.register(Teacher)
>>>>>>> 895d920d906c78739bbed892074bd829788cf032
