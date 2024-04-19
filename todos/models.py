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
    Date when the task was done.
    
    Attributes:
        null (bool): Whether null values are allowed.
        blank (bool): Whether the field is allowed to be blank.
    """


