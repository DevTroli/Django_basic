from datetime import date
from django.db import models


class Todo(models.Model):
    """
    ORM to represent the data in a SQL table as a Django model
    """

    title = models.CharField(max_length=100, null=False, blank=False)
    """
    Title of the task.
    
    Attributes:
        max_length (int): The maximum length of the title.
        null (bool): Whether null values are allowed.
        blank (bool): Whether the field is allowed to be blank.
    """

    done_date = models.DateField(null=True, blank=False)
    """
    The date when the task was marked as done.

    Attributes:
        null (bool): Whether null values are allowed.
        blank (bool): Whether the field is allowed to be blank.
    """

    def done_task(self):
        """
        Method to mark a task as done, setting the done_date to today's date.
        """
        if not self.done_date:
            self.done_date = date.today()
            self.completed = True
            self.save()

    class Meta:
        """
        Metadata for the Todo model.
        """

        ordering = ["done_date"]
