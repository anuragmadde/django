from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
	default_limit=5


	
class CustomPageNumberPagination(PageNumberPagination):
	page_size = 5
		