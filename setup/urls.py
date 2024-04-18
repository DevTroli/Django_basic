from django.urls import path

from todos.views import TodoListView, RemoveTodoView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("remove/<int:todo_id>/", RemoveTodoView.as_view(), name="remove_todo"),
]
