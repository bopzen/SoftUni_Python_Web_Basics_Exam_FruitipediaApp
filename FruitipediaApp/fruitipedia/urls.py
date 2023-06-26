from django.urls import path, include

from FruitipediaApp.fruitipedia.views import index, dashboard, create_profile, profile_details, edit_profile, \
    delete_profile, create_fruit, fruit_details, edit_fruit, delete_fruit

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete_profile')
    ])),
    path('create/', create_fruit, name='create-fruit'),
    path('<int:pk>/', include([
        path('details/', fruit_details, name='fruit-details'),
        path('edit/', edit_fruit, name='edit-fruit'),
        path('delete/', delete_fruit, name='delete-fruit')
    ]))
]