from django.shortcuts import get_object_or_404
from .models import UserProfile
def user_profile_context_processor(request):
    context = {}
    # Fetch the user's profile
    user_profile = UserProfile.objects.first()

    if user_profile:
        context['user_profile'] = user_profile
        context['user_email'] = user_profile.email if hasattr(user_profile, 'email') else None
        context['user_description'] = user_profile.description if hasattr(user_profile, 'description') else None
        context['linkedin_url'] = user_profile.linkedin_url if hasattr(user_profile, 'linkedin_url') else None
    else:
        # If there is no user profile, you can include any default data or None
        context['user_profile'] = None
        context['user_email'] = None
        context['user_description'] = None
        context['linkedin_url'] = None

    return context