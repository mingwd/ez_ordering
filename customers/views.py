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
    # else
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
from collections import defaultdict

@login_required
def customer_profile_edit_view(request):
    if request.method == 'POST':

        try:
            profile = CustomerProfile.objects.get(user=request.user)
        except CustomerProfile.DoesNotExist:
            profile = None

        profile_form = CustomerProfileForm(request.POST, instance=profile)
        tag_form = CustomerTagForm(request.POST)

        if profile_form.is_valid() and tag_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

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

        all_tags = Tag.objects.all().order_by('category')
        grouped_tags = defaultdict(list)

        for tag in all_tags:
            grouped_tags[tag.category].append(tag)

        grouped_tags = grouped_tags.items()

        return render(request, 'customer/profile-edit.html', {
            'profile_form': profile_form,
            'tag_form': tag_form,
            'highlighted_tags': [tag.id for tag in existing_tags],
            'grouped_tags': grouped_tags,
        })


@login_required
def customer_dashboard_view(request):
    profile = CustomerProfile.objects.get(user=request.user)
    tags = Tag.objects.filter(customers__user=request.user)

    categorized_tags = {}
    for tag in tags:
        pretty_name = tag.category.replace('_', ' ').title()
        if pretty_name not in categorized_tags:
            categorized_tags[pretty_name] = []
        categorized_tags[pretty_name].append(tag.name)

    return render(request, 'customer/dashboard.html', {
        'profile': profile,
        'categorized_tags': categorized_tags,
    })


def customer_login_error_view(request):
    return render(request, 'customer/login_error.html')

def homepage_view(request):
    return render(request, 'home.html')

""" views that works with frontend """
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def frontend_login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('User logged in successfully:', user.username)
            return JsonResponse({'success': True})
        else:
            print('Wrong credential!')
            return JsonResponse({'success': False, 'error': 'Username or Password Error!'})