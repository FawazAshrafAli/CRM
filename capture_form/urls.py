from django.urls import path
from .views import FormView, CreateLeadView, GetProgramView, GetCourseView

app_name = 'capture_form'

urlpatterns = [
    path('', FormView.as_view(), name="form"),
    path('create_lead/', CreateLeadView.as_view(), name="create_lead"),
    path('get_programs/', GetProgramView.as_view(), name="get_programs"),
    path('get_course/', GetCourseView.as_view(), name="get_course"),
]
