from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.masterview, name = "masterview"),
    path('detail/<key>', views.detail, name = "detail"),
    path('table', views.table, name = "table"),
	path('duplicate', views.duplicate, name = "duplicate"),
	path('export', views.export, name = "export"),
	path('CreateLesson', views.CreateLesson, name = "CreateLesson"),
	path('modify', views.modify, name = "modify"),
	path('Delete', views.Delete, name = "Delete"),
    path('faq', views.faq, name = "faq"),
    path('support', views.support, name = "support"),
    path('improve', views.improve, name = "improve"),
    path('lessonProfiles', views.lessonProfiles, name = "lessonProfiles"),
    path('reports', views.reports, name = "reports"),
    path('duplicationLogs', views.duplicationLogs, name = "duplicationLogs"),
    path('visualize', views.Visualize, name = "visualize"),
    path('logout_view', views.logout, name = "logout")
]
