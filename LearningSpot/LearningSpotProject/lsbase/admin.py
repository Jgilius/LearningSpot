from django.contrib import admin
from .models import *


# admin.site.register(learning_material_student)
# admin.site.register(zoom_student)
# admin.site.register(whiteboard_student)
admin.site.register(Learning_Intention)
admin.site.register(Happy_Select)
admin.site.register(Unsure_Select)
admin.site.register(Sad_Select)
admin.site.register(Learning_Task)
admin.site.register(LTComplete)
admin.site.register(LTInProgress)
admin.site.register(LTNeedHelp)
admin.site.register(LTNotStarted)