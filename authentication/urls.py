from django.urls import path
from .views import (LoginView, LogoutView, RegisterUserView, 
                    CrmUserDetailView, Error404, Error500, 
                    MyProfileView, CrmUserFamilyUpdationView, 
                    CrmUserEducationUpdationView, CrmUserExperienceUpdationView,
                    CrmUserUpdateView, CrmUserPersonalInfoUpdateView, 
                    CrmUserEmergencyContactUpdateView, CrmUserBankInfoUpdateView, 
                    FamilyMemberDetailView, FamilyMemberUpdateView, 
                    FamilyMemberDeleteView, EducationDetailView, 
                    EducationUpdateView, EducationDeleteView, 
                    ExperienceDetailView, ExperienceUpdateView, 
                    ExperienceDeleteView)

app_name = "authentication"

urlpatterns = [
    path('', LoginView.as_view(), name='login'),  # home page view    
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('detail/<pk>', CrmUserDetailView.as_view(), name="detail"),

    path('update_user/', CrmUserUpdateView.as_view(), name="update_user"),
    path('update_personal_info/', CrmUserPersonalInfoUpdateView.as_view(), name="update_personal_info"),
    path('update_emergency_contacts/', CrmUserEmergencyContactUpdateView.as_view(), name="update_emergency_contacts"),
    path('update_bank_info/', CrmUserBankInfoUpdateView.as_view(), name="update_bank_info"),
    path('update_family_info/', CrmUserFamilyUpdationView.as_view(), name="update_family_info"),
    path('update_education/', CrmUserEducationUpdationView.as_view(), name="update_education"),
    path('update_experience/', CrmUserExperienceUpdationView.as_view(), name="update_experience"),

    path('family_member/<pk>', FamilyMemberDetailView.as_view(), name="family_member"),
    path('edit_family_member/<pk>', FamilyMemberUpdateView.as_view(), name="edit_family_member"),
    path('delete_family_member/<pk>', FamilyMemberDeleteView.as_view(), name="delete_family_member"),

    path('education/<pk>', EducationDetailView.as_view(), name="education"),
    path('edit_education/<pk>', EducationUpdateView.as_view(), name="edit_education"),
    path('delete_education/<pk>', EducationDeleteView.as_view(), name="delete_education"),

    path('experience/<pk>', ExperienceDetailView.as_view(), name="experience"),
    path('edit_experience/<pk>', ExperienceUpdateView.as_view(), name="edit_experience"),
    path('delete_experience/<pk>', ExperienceDeleteView.as_view(), name="delete_experience"),

    path('my_profile/', MyProfileView.as_view(), name="my_profile"),

    path('error404', Error404.as_view(), name="error404"),
    path('error500', Error500.as_view(), name="error500"),
]
