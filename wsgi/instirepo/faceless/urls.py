from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup_request/', views.signup_request, name='signup_request'),
    url(r'^check_team_exist/', views.check_team_exist, name='check_team_exist'),
    url(r'^login_request/', views.login_request, name='login_request'),
    url(r'^add_user_to_team', views.add_user_to_team, name='add_user_to_team'),
    url(r'^add_gcm_token', views.add_gcm_token, name='add_gcm_token'),
    url(r'^make_channel', views.make_channel, name='make_channel'),
    url(r'^all_channels', views.all_channels, name='all_channels'),
    url(r'^get_chats_for_channel', views.get_chats_for_channel, name='get_chats_for_channel'),
    url(r'^add_chat_message', views.add_chat_message, name='add_chat_message'),
    url(r'^get_feeds', views.get_feeds, name='get_feeds'),
    # url(r'^add_to_favourite', views.add_to_favourite, name='add_to_favourite'),
    # url(r'^view_wishlist_request', views.view_wishlist_request, name='view_wishlist_request'),
    # url(r'^autocomplete_search', views.autocomplete_search, name='autocomplete_search'),
    # url(r'^logout_view', views.logout_view, name='logout_view'),
    # url(r'^add_to_cart', views.add_to_cart, name='add_to_cart'),
    # url(r'^remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    # url(r'^view_cart_request', views.view_cart_request, name='view_cart_request'),
    # url(r'^add_or_edit_address', views.add_or_edit_address, name='add_or_edit_address'),
    # url(r'^add_review', views.add_review, name='add_review'),
    # url(r'^view_reviews', views.view_reviews, name='view_reviews'),
    # url(r'^view_addresses', views.view_addresses, name='view_addresses'),
]
