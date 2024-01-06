from django.db import models
import json

class Service(models.Model):
    name = models.CharField(max_length=50,
                            help_text="The name of the Service.")
    description = models.TextField(max_length=50, help_text="The Service's description.")
    price = models.IntegerField(help_text="The Service's price.")
    image_url = models.URLField(help_text="URL of the Service's image",default='default-image.jpg')


    def __str__(self):
        return self.name
    
    def get_description_list(self):
        try:
            return json.loads(self.description)
        except json.JSONDecodeError:
            return []

    def description_as_list(self):
        return self.get_description_list()
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Contact")
    phone_numbers = models.JSONField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    working_hours = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class ContactType(models.Model):
    class ContactChoice(models.TextChoices):
        PHONE = "PHONE", "Phone"
        EMAIL = "EMAIL", "Email"
        ADDRESS = "ADDRESS", "Address"
        WORKING_HOURS = "WORKING_HOURS", "Working Hours"

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    choice = models.CharField(
        verbose_name="The choice of the service",
        choices=ContactChoice.choices,
        max_length=20,
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    working_hours = models.JSONField(null=True, blank=True)
