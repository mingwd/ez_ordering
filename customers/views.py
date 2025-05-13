from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def customer_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            return redirect('login_error')

    form = UserRegisterForm
    return render(request, 'customer/login.html', {'form': form})


from .forms import UserRegisterForm, CustomerProfileForm, CustomerTagForm
from .models import CustomerPreference

def customer_signup_view(request):

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user) 
            return redirect('customer_profile_edit')
    else:
        user_form = UserRegisterForm()
        return render(request, 'customer/signup.html', {
            'user_form': user_form,
        })

from django.contrib.auth.decorators import login_required
from .models import CustomerProfile
from .models import Tag

@login_required
def customer_profile_edit_view(request):
    if request.method == 'POST':
        profile_form = CustomerProfileForm(request.POST)
        tag_form = CustomerTagForm(request.POST)

        if profile_form.is_valid() and tag_form.is_valid():
            profile, _ = CustomerProfile.objects.get_or_create(user=request.user)
            profile_form = CustomerProfileForm(request.POST, instance=profile)
            profile_form.save()

            # existing user tag (sys generated or added before)
            existing_prefs = CustomerPreference.objects.filter(user=request.user)
            existing_tag_to_pref = {pref.tag: pref for pref in existing_prefs}
            existing_tags = set(existing_tag_to_pref.keys())

            final_selected_tags = set(tag_form.cleaned_data['preference_tags'])

            # user deleted tags
            tags_to_remove = existing_tags - final_selected_tags
            CustomerPreference.objects.filter(user=request.user, tag__in=tags_to_remove).delete()

            # user added tags
            tags_to_add = final_selected_tags - existing_tags
            for tag in tags_to_add:
                CustomerPreference.objects.create(user=request.user, tag=tag, count=5)

            return redirect('customer_dashboard')

    else:
        try:
            profile = CustomerProfile.objects.get(user=request.user)
            profile_form = CustomerProfileForm(instance=profile)
        except CustomerProfile.DoesNotExist:
            profile_form = CustomerProfileForm()

        # currect existing tag
        existing_tags = Tag.objects.filter(customers__user=request.user)
        tag_form = CustomerTagForm(initial={
            'preference_tags': existing_tags,
        })

    return render(request, 'customer/profile-edit.html', {
        'profile_form': profile_form,
        'tag_form': tag_form,
        'highlighted_tags': [tag.id for tag in existing_tags], 
    })


@login_required
def customer_dashboard_view(request):
    profile = CustomerProfileForm.objects.get(user=request.user)
    return render(request, 'customer/dashboard.html', {
        'profile': profile,
    })


def customer_login_error_view(request):
    return render(request, 'customer/login_error.html')