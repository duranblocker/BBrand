from django.contrib import admin
from .models import Post
from .models import Svg
from .models import SvgPath

admin.site.register(Post)
admin.site.register(Svg)
# admin.site.register(Projects)
admin.site.register(SvgPath)
