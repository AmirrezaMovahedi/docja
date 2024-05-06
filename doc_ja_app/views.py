from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.decorators.http import require_POST

from .models import *

from .forms import *


def index_view(request):
    return redirect('doc_ja_app:doctor_list')


def about_us_view(request):
    return render(request, 'docja/about_us.html')


def doctor_list_view(request, expert=None):
    # if expert is not None:
    #     doctors = Doctor.objects.filter(user__is_active=True, expert=expert)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        expert = request.GET.get('expert')
        doctors = Doctor.objects.filter(user__is_active=True, expert=expert)
        if expert == 'all':
            doctors = Doctor.objects.filter(user__is_active=True)
        return render(request, 'docja/ajaxlist.html', {'doctors': doctors})

    else:
        doctors = Doctor.objects.filter(user__is_active=True)

    return render(request, 'docja/doctor_list.html', context={'doctors': doctors})


@login_required()
def doctor_detail_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    comments = doctor.doctor_comments.filter(active=True)
    # doctor.days.get(day='').hours.get(form='', to='').is_full()
    # doctor.reservations.filter(day='یکشنبه', From='10', to='11', web_user='').exists()
    return render(request, 'docja/doctor_detail.html', context={'doctor': doctor, 'comments': comments})


def doctor_register_view(request):
    if request.method == 'POST':
        user_form = UserRegister(request.POST, request.FILES)
        doctor_form = DoctorRegister(request.POST, request.FILES)

        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.expert = doctor_form.cleaned_data['expert']
            doctor.user = user
            doctor.save()
            return redirect('doc_ja_app:doctor_list')

    else:
        user_form = UserRegister()
        doctor_form = DoctorRegister()

    return render(request, 'registration/doctor_register.html',
                  context={'user_form': user_form, 'doctor_form': doctor_form})


def web_user_register_view(request):
    if request.method == 'POST':
        user_form = UserRegister(request.POST, request.FILES)
        web_user_form = Web_userRegister(request.POST, request.FILES)
        if user_form.is_valid() and web_user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            web_user = web_user_form.save(commit=False)
            web_user.user = user
            web_user.save()
            return redirect('doc_ja_app:doctor_list')
    else:
        user_form = UserRegister()
        web_user_form = Web_userRegister()

    return render(request, 'registration/web_user_register.html',
                  context={'user_form': user_form, 'web_user_form': web_user_form})


@login_required()
def profile_view(request):
    user = request.user
    if Web_user.objects.filter(user=user.id).exists():
        user = Web_user.objects.get(user=user)
        doctor = False
    elif Doctor.objects.filter(user=user.id).exists():
        user = Doctor.objects.get(user=user)
        doctor = True
    else:
        raise Http404('پروفایلی برای کاربر وجود ندارد')
    if doctor:
        return render(request, 'docja/doctor_profile.html', context={'own_user': user})
    else:
        return render(request, 'docja/web_user_profile.html', context={'own_user': user})


@login_required()
def doctor_account_edit_view(request):
    user = request.user
    if Doctor.objects.filter(user=user.id).exists():
        if request.method == 'POST':
            user_form = UserEdit(request.POST, instance=request.user)
            doctor_form = DoctorEdit(request.POST, request.FILES, instance=request.user.doctor)

            if doctor_form.is_valid and user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                print(request.POST)
                doctor_form.save()

                return redirect('doc_ja_app:profile')

        else:
            doctor_form = DoctorEdit(instance=request.user.doctor)
            user_form = UserEdit(instance=request.user)
        return render(request, 'registration/doctor_edit.html',
                      context={'doctor_form': doctor_form, 'user_form': user_form})
    else:
        raise Http404('این صفحه برای شما وجود ندارد(عدم دسترسی)')


@login_required()
def web_user_account_edit_view(request):
    user = request.user
    if Web_user.objects.filter(user=user.id).exists():
        if request.method == 'POST':
            user_form = UserEdit(request.POST, instance=request.user)
            web_user_form = Web_userRegister(request.POST, request.FILES, instance=request.user.web_user)

            if web_user_form.is_valid and user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                web_user_form.save()

                return redirect('doc_ja_app:profile')

        else:
            web_user_form = Web_userRegister(instance=request.user.web_user)
            user_form = UserEdit(instance=request.user)
        return render(request, 'registration/web_user_edit.html',
                      context={'web_user_form': web_user_form, 'user_form': user_form})
    else:
        raise Http404('این صفحه برای شما وجود ندارد(عدم دسترسی)')


@login_required()
@require_POST
def doctor_like(request):
    doctor_id = request.POST.get('doctor_id')
    if doctor_id is not None:
        doctor = get_object_or_404(Doctor, id=doctor_id)
        user = request.user
        if user in doctor.likes.all():
            doctor.likes.remove(user)
            liked = False
        else:
            doctor.likes.add(user)
            liked = True

        like_count = doctor.likes.count()
        response_data = {
            "like_count": like_count,
            "liked": liked,
        }
    else:
        response_data = {"error": "invalid doctor_id"}

    return JsonResponse(response_data)


def search_view(request):
    query = None
    result = []
    if "query" in request.GET and request.GET.get('query') != '':

        form = SearchFrom(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result1 = Doctor.objects.filter(description__icontains=query)
            result2 = Doctor.objects.filter(user__first_name__icontains=query)
            result = result1 | result2
    else:
        return redirect('doc_ja_app:doctor_list')

    return render(request, 'forms/search.html', {'query': query, 'result': result})


@require_POST
@login_required()
def doctor_comment_view(request, pk):
    form = CommentForm(request.POST)
    doctor = get_object_or_404(Doctor, id=pk)

    if form.is_valid():
        doctor_c = form.save(commit=False)
        doctor_c.user = request.user.web_user
        doctor_c.doctor = doctor
        doctor_c.save()

        return redirect('doc_ja_app:doctor_detail', doctor.id)


@login_required()
@require_POST
def reservation_view(request):
    doctor_id = request.POST.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    day = request.POST.get('day')
    hour = request.POST.get('hour')
    web_user = request.user.web_user

    if Reservation.objects.filter(doctor=doctor, day=day, hour=hour, web_user=web_user).exists():
        response_data = {'status': False}
        return JsonResponse(response_data)

    else:
        Reservation.objects.create(doctor=doctor, day=day, hour=hour, web_user=web_user)
        response_data = {'status': True}
        return JsonResponse(response_data)
