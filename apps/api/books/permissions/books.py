  #djangoRF
from rest_framework.permissions import BasePermission

class IsManager(BasePermission):

	def has_object_permission(self , request , view , obj):
		print(request.user.is_manager)
		return request.user.is_manager