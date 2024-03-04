from django.contrib import admin

from website_admin.models import Service, About_executive_team, About_functional_team, About_technical_team, About_technical2_team, About_executive2_team, News, User, Message

# Register your models here.
admin.site.register(Service)
admin.site.register(About_executive_team)
admin.site.register(About_functional_team)
admin.site.register(About_technical_team)
admin.site.register(About_technical2_team)
admin.site.register(About_executive2_team)
admin.site.register(News)
admin.site.register(User)
admin.site.register(Message)