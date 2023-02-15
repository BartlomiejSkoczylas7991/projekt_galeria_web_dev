from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

#logowanie
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

#wyswietlenie danych o koncie
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

#rejestracja
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Stwórz nowego użytkownika, ale unika zapisania go jeszcze
            new_user = user_form.save(commit=False)
            # Ustaw wybrane hasło
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Zapisz obiekt User
            new_user.save()
            # Stwórz profil użytkownika
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
#@login_required
#def add_post(request):
#    if request.method == "POST":
#        title = request.POST['title']
#        content = request.POST['content']
#        author = request.user
#        post = Post.objects.create(title=title, content=content, author=author)
#        return redirect('account:index')
#    return render(request, 'account/add_post.html')
#
#@login_required
#def add_comment(request, post_id):
#    if request.method == "POST":
#        content = request.POST['content']
#        author = request.user
#        post = Post.objects.get(id=post_id)
#        Comment.objects.create(content=content, author=author, post=post)
#        return redirect('account:index')
#    return redirect('account:index')
#
#def register(request):
#    if request.method == "POST":
#        username = request.POST['username']
#        email = request.POST['email']
#        password = request.POST['password']
#        user = User.objects.create_user(username=username, email=email, password=password)
#        user.save()
#        return redirect('index')
#    return render(request, 'galeria_app/register.html')
#
#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'galeria_app/post_detail.html', {'post': post})

#
#
#
#
#def post_new(request):
#    if request.method == "POST":
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#    return render(request, 'galeria_app/post_edit.html', {'form': form})
#
#
#
#
#
#def post_edit(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = PostForm(request.POST, request.FILES, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm(instance=post)
#    return render(request, 'galeria_app/post_edit.html', {'form': form})
#
#
#
#
#
#
#def post_delete(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    post.delete()
#    return redirect('index')
#
#def add_comment_to_post(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.post = post
#            comment.author = request.user
#            comment.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = CommentForm()
#    return render(request, 'galeria_app/add_comment_to_post.html', {'form': form})
#
#def comment_approve(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    comment.approve()
#    return redirect('post_detail', pk=comment.post.pk)
#
#def comment_remove(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    comment.delete()
#    return redirect('post_detail', pk=comment.post.pk)