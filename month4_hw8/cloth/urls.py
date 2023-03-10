from django.urls import path
from . import views


urlpatterns = [
    path("cloth_one_tag/", views.ProductTagFirstView.as_view(), name="first_tag"),
    path("cloth_two_tag/", views.ProductTagSecondView.as_view(), name="second_tag"),
    path("cloth_three_tag/", views.ProductTagThirdView.as_view(), name="third_tag"),
    path("cloth_four_tag/", views.ProductFourthView.as_view(), name="fourth_tag"),
    path("cloth/", views.ProductListView.as_view(), name="product"),
    path("add_order/", views.OrderCreateView.as_view(), name="add"),
]
