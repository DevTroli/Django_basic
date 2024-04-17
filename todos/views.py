# views.py
from django.views.generic import ListView
from django.shortcuts import redirect
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todo_list"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        if title:  # Verifica se o campo do título não está vazio
            Todo.objects.create(title=title)
        return redirect(
            "todo_list"
        )  # Redireciona de volta para a página de lista de tarefas
