from rest_framework import routers
from rentall import api_views as rentall_views


router = routers.DefaultRouter()
router.register(r"friends", rentall_views.FriendViewset)
router.register(r"belongings", rentall_views.BelongingViewset)
router.register(r"borrowings", rentall_views.BorrowedViewset)