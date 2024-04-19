from datetime import date
from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect, get_object_or_404


from .models import Todo


class TodoListView(ListView):
    """
    This view renders the list of todos.

    Attributes:
        model (Model): The Todo model.
        template_name (str): The template to render the todo list.
        context_object_name (str): The name of the context variable containing the todo list.
    """

    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todo_list"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create new todos.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponseRedirect: Redirects to the todo list page after creating a new todo.
        """
        title = request.POST.get("title")
        if title:  # Check if the title field is not empty
            Todo.objects.create(title=title)
        return redirect("todo_list")


class RemoveTodoView(View):
    """
    This view handles the removal of a todo.
    """

    def post(self, request, todo_id):
        """
        Handle POST requests to delete a todo.

        Args:
            request (HttpRequest): The HTTP request object.
            todo_id (int): The ID of the todo to be deleted.

        Returns:
            HttpResponseRedirect: Redirects to the todo list page after deleting the todo.
        """
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return redirect("todo_list")


class CompleteTaskView(View):
    """
    This view handles completing a todo task.
    """

    def post(self, request, todo_id):
        """
        Handle POST requests to mark a todo as complete.

        Args:
            request (HttpRequest): The HTTP request object.
            todo_id (int): The ID of the todo to be marked as complete.

        Returns:
            HttpResponseRedirect: Redirects back to the todo list page after marking the todo as complete.
        """
        todo = get_object_or_404(Todo, id=todo_id)
        todo.done_task()
        return redirect("todo_list")
