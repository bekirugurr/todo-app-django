from django.db import models

class Todo(models.Model):
    PRIORITY = (
        ("High Priority", "😱 High Priority"), 
        ("Middle Priority", "😨 Middle Priority"), 
        ("Low Priority", "😧 Low Priority"), 
    )
    title = models.CharField(max_length=25)
    content = models.TextField(max_length=120)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    tag = models.CharField(max_length=20, blank=True, null=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


