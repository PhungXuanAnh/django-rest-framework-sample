from django.urls import include, path, re_path
from rest_framework import routers

from music import model_viewsets as music_model_viewsets
from music import generic_views as music_generic_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musican-viewset', music_model_viewsets.MusicianModelViewSet)


urlpatterns = [
    # path(r'prohibited-items', ProhibitedItemListView.as_view(), name='get_list_prohibited_items'),
    # re_path(r'^delivery-order/(?P<code>{})/change-status$'.format(ORDER_CODE_REGEX_BASE),
    #         DeliveryUpdateShipmentOrderStatus.as_view(), name='update_status_from_deleviry'),
    re_path(r'^', include(router.urls))
]
