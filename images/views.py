from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCreateForm, EmailForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from common.decorators import ajax_required
from actions.utils import create_action
from django.core.mail import send_mail
from django.utils.text import slugify
from django.contrib import messages
from .models import Image

@login_required
def image_create(request):
    if request.method =='POST':
        #form is Sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            new_item = form.save(commit = False)
            #assign current user to new_item
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'bookmarked image', new_item)
            messages.success(request,'Image added successfully')
            #redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section':'images',
    'form':form})

@login_required
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        slug = slugify(myfile.name)
        filename = fs.save(slug, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('http://localhost:8000/images/create/?url=http://localhost:8000'+uploaded_file_url+'&title='+myfile.name)
    return render(request, 'images/image/upload.html')

@login_required
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    comments = image.comments.filter(active=True)
    likes = image.users_like.all()
    no_of_likes = likes.count()
    if request.method == 'POST':
        #comment posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #Creates a comment object but doesn't save it to the Database
            new_comment = comment_form.save(commit=False)
            #assigns current post to the comment
            new_comment.image = image
            #save the comment to database
            new_comment.save()
    else:
        # if request method is get then empty form is created.
        comment_form = CommentForm()
    return render(request, 'images/image/detail.html', {'section':'images',
    'image':image,
    'comments':comments,
    'comment_form':comment_form,
    'limit':no_of_likes-5,
    })

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
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
                create_action(request.user, 'unliked', image)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,5)
    imagecount= images.count()
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'images/image/list.html', {'section': 'images','images':images,'page':page})

@login_required
def image_share(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    sent =False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            image_url = request.build_absolute_uri(image.get_absolute_url())
            subject ='{} ({}) wants you to have a look at this image.'.format(request.user.get_full_name(), request.user.email)
            message = 'View "{}" at {}\n\n{}\'s comments: {}'.format(image.title, image_url, request.user.get_full_name(), cd['comments'])
            send_mail(subject, message, 'admin@mysite.com', [cd['to']])
            sent = True
    else:
        form = EmailForm()
    return render(request, 'images/image/share.html', {'image':image,
    'form':form,
    'sent':sent})
