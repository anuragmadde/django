from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

	message = "You cannot update others comments"
	def has_object_permission(self,request,view,obj):
		return obj.user == request.user