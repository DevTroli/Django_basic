from django.urls import path

from todos.views import TodoListView, RemoveTodoView, CompleteTaskView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("remove/<int:todo_id>/", RemoveTodoView.as_view(), name="remove_todo"),
    path(
        "complete/<int:todo_id>/", CompleteTaskView.as_view(), name="complete_task"
    ),  # Nova rota para completar uma tarefa
]
