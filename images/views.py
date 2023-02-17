from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger
from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        # formularz jest wyslany
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # dane formularzu są poprawne
            new_item = form.save(commit=False)

            # przypisanie bieżącego użytkownika do elementu
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # przekierowanie do nowo utworzonego widoku szczegółów elementu
            return redirect(new_item.get_absolute_url())
    else:
        # zbuduj formularz z danymi dostarczonymi  poprzez GET
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # Jeśli strona nie jest liczbą całkowitą, podaj pierwszą stronę
        images = paginator.page(1)
    except EmptyPage:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Jeśli żądanie to AJAX, a strona jest poza zakresem
            # zwróć pustą stronę
            return HttpResponse('')
        # Jeśli strona jest poza zakresem, wyślij ostatnią stronę wyników
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request,
                  'images/image/list.html',
                   {'section': 'images', 'images': images})