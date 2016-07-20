from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,Http404,HttpResponse
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.

def comment_delete(request, id):
	instance=get_object_or_404(Comment,id=id)

	if  instance.user != request.user:
		reponse=HttpResponse("You dont have Permissions to delete others comments")
		reponse.status_code = 403
		return reponse

	if request.method== "POST":
		parent_page=instance.content_object.get_absolute_url()
		instance.delete()
		return HttpResponseRedirect(parent_page)

	content={
	"object" : instance,
	}
	return render(request,"comment_delete.html",content)


def comment_detail (request, id):
	instance = get_object_or_404(Comment,id=id )
	
	if not instance.is_parent:
		instance=instance.parent
	
	initial_data={
		"object_id" : instance.object_id,
		"content_type" : instance.content_type
	}


	form = CommentForm(request.POST or None,initial=initial_data)
	
	if form.is_valid():
		contentType=form.cleaned_data.get("content_type")
		c_Type=ContentType.objects.get(model=contentType)
		obj_id=form.cleaned_data.get("object_id")
		contentData=form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id=request.POST.get("parent_id")
		except:
			parent_id=None
		
		if parent_id:
			parent_qs=Comment.objects.filter(id=parent_id)
			if parent_qs.exists():
				parent_obj=parent_qs.first()

		# if not request.user.is_authenticated():
		# 	raise Http404
		new_comment,created=Comment.objects.get_or_create(
				user=request.user,
				content_type=c_Type,
				object_id=obj_id,
				content = contentData,
				parent=parent_obj
			)
		
		return HttpResponseRedirect(instance.get_comments_absolute_url())



	context = {
		"my_form":form,
		"loop" : instance
	}
	return render(request,"comment_detail.html",context)
