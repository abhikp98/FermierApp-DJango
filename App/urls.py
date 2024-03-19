"""FermierApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from App import views

urlpatterns = [
    path('', views.login),
    path('login_post', views.login_post),
    path('logout', views.logout),

    path('admin_home', views.admin_home),
    path('admin_add_officer', views.admin_add_officer),
    path('admin_add_officer_post', views.admin_add_officer_post),
    path('admin_view_officer', views.admin_view_officer),
    path('admin_edit_officer/<officerid>', views.admin_edit_officer),
    path('admin_edit_officer_post/<officerid>', views.admin_edit_officer_post),
    path('adin_delete_officer/<officerid>', views.adin_delete_officer),
    path('admin_add_notification', views.admin_add_notification),
    path('admin_add_notification_post', views.admin_add_notification_post),
    path('admin_view_notification', views.admin_view_notification),
    path('admin_delete_notification/<notificationid>', views.admin_delete_notification),
    path('admin_view_feedback', views.admin_view_feedback),
    path('admin_add_crop_fert_perc', views.admin_add_crop_fert_perc),
    path('admin_add_crop_fert_perc_post', views.admin_add_crop_fert_perc_post),
    path('admin_view_crop_fert_perc', views.admin_view_crop_fert_perc),
    path('admin_edit_crop_fert_perc/<cfpid>', views.admin_edit_crop_fert_perc),
    path('admin_edit_crop_fert_perc_post/<cfpid>', views.admin_edit_crop_fert_perc_post),
    path('admin_delete_crop_fert_perc/<cfpid>', views.admin_delete_crop_fert_perc),
    path('list_table_list/<qry>', views.list_table_list),
    path('admin_view_complaints', views.admin_view_complaints),
    path('admin_send_reply/<id>', views.admin_send_reply),
    path('admin_send_reply_post/<id>', views.admin_send_reply_post),

    path('officer_home', views.officer_home),
    path('officer_view_profile', views.officer_view_profile),
    path('officer_view_cfp', views.officer_view_cfp),
    path('officer_list_table_list/<qry>', views.officer_list_table_list),
    path('officer_update_stock/<cfpid>', views.officer_update_stock),
    path('officer_update_stock_post/<cfpid>', views.officer_update_stock_post),
    path('officer_view_request', views.officer_view_request),
    path('officer_view_items', views.officer_view_items),
    path('officer_accept_request/<reqid>', views.officer_accept_request),
    path('officer_reject_request/<reqid>', views.officer_reject_request),
    path('officer_view_notifications', views.officer_view_notifications),
    path('officer_chat_page', views.officer_chat_page),
    path('chatt/<u>', views.chatt),
    path('chatrply', views.chatrply),
    path('chatsnd/<u>', views.chatsnd),
    path('officer_change_password', views.officer_change_password),
    path('officer_change_password_post', views.officer_change_password_post),


    path('loginAndroid', views.loginAndroid),
    path('register', views.register),
    path('viewcfp', views.viewcfp),
    path('view_agroff', views.view_agroff),
    path('view_stock', views.view_stock),
    path('add_cart', views.add_cart),
    path('view_cart', views.view_cart),
    path('delete_cart', views.delete_cart),
    path('send_request', views.send_request),
    path('view_request_status', views.view_request_status),
    path('view_items', views.view_items),
    path('view_notification', views.view_notification),

    path('view_chat', views.view_chat),
    path('add_chat', views.add_chat),
    path('view_updates', views.view_updates),
    path('and_send_feedback', views.and_send_feedback),
    path('and_send_complaint', views.and_send_complaint),
    path('and_view_complaints', views.and_view_complaints),
    path('view_own_updates', views.view_own_updates),
    path('send_update', views.send_update),
    path('delete_story', views.delete_story),


]
