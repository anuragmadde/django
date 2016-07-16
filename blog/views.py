from urllib.parse import quote_plus
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect, Http404
from .models import Blog
from comments.models import Comment
from .forms import BlogForm
from comments.forms import CommentForm

# Create your views here.

def blog_home (request):
	querySet_List = Blog.objects.all()#.order_by("-timestamp")
	# instance = Blog.objects.get(id=1)
	# instance = get_object_or_404(Blog,id=1)
	query=request.GET.get('query')
	if query:
		querySet_List = Blog.objects.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) | 
			Q(user__first_name__icontains=query)

			)
	paginator = Paginator(querySet_List, 3) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		querySet = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		querySet = paginator.page(1)
	except EmptyPage:
 		# If page is out of range (e.g. 9999), deliver last page of results.
		querySet = paginator.page(paginator.num_pages)

	context = {
		"query_Set" : querySet,
		"title"	: "My Blog ",
		
	}

	return render(request,"blog.html", context)


def blog_create (request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if not request.user.is_authenticated():
		raise Http404
	form = BlogForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.user=request.user
		instance.save()
		# messages.success(request,"New Post Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Error Creating Post")
	context = {
		"form" : form,
	}
	return render(request,"blog_create.html",context)

def blog_detail (request, slug=None):
	instance = get_object_or_404(Blog,slug=slug )
	# share_string = quote_plus(instance.content)
	# comments=Comment.custom_filter.filter_by_instance(instance)
	initial_data = {
		"content_type" :instance.get_contentType,
		"object_id" : instance.id
	}

	form=CommentForm(request.POST or None,initial=initial_data)
	if form.is_valid():
		contentType=form.cleaned_data.get("content_type")
		c_Type=ContentType.objects.get(model=contentType)
		obj_id=form.cleaned_data.get("object_id")
		contentData=form.cleaned_data.get("comment")
		created=Comment.objects.get_or_create(
				user=request.user,
				content_type=c_Type,
				object_id=obj_id,
				comment = contentData,
			)

		if created:
			print ("Success")


	comments=instance.get_comment
	context = {
		"instance" : instance,
		"title"	: instance.title,
		# "share_string": share_string,
		"comments":comments,
		"my_form":form
	}
	return render(request,"blog_detail.html",context)

def blog_update (request, slug=None):
	instance = get_object_or_404(Blog,slug=slug)
	form = BlogForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance= form.save()
		# messages.success(request,"Post has been Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request,"Cannot be Updated")
	context = {
	"form" : form,
	}
	return render(request,"blog_create.html",context)

def blog_delete (request, slug=None):
	instance = get_object_or_404(Blog,slug=slug)
	instance.delete()
	return redirect("blog:home")