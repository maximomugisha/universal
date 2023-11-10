from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from phone_field import PhoneField


# Create your models here.
class Profile(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    nationality = CountryField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='userprofile')
    gender = models.CharField(
        max_length=255, choices=GENDER, default=GENDER[0][0]
    )
    date_of_birth = models.DateField(null=False)
    address_of_origin = models.CharField(max_length=255, null=True, blank=True)
    address_of_residence = models.CharField(max_length=255, null=True, blank=True)
    address_of_work = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        fullname = (self.user.first_name + " " + self.user.last_name)
        if len(fullname) !=0:
            return fullname
        else:
            return str('User has no First or Last Name')

    class Meta:
        ordering = ['user_id']


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')
    whatsapp_number = PhoneField(blank=True, help_text='Contact phone number')
    mobile_number = PhoneField(blank=True, help_text='Contact phone number')
    home_number = PhoneField(blank=True, help_text='Contact phone number')
    primary_email = models.EmailField(max_length=70, blank=True, unique=True)
    secondary_email = models.EmailField(max_length=70, blank=True, unique=True)
    work_email = models.EmailField(max_length=70, blank=True, unique=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return str(self.mobile_number)

    class Meta:
        ordering = ['id']


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work')
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    position_held = models.CharField(max_length=255, null=True, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    image_1 = models.ImageField(upload_to='work_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='work_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='work_images/', null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ['id']


class Biography(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bio')
    heading = models.CharField(max_length=255, null=True, blank=True)
    paragraph_1 = models.TextField(max_length=255, null=True, blank=True)
    paragraph_2 = models.TextField(max_length=255, null=True, blank=True)
    paragraph_3 = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Biography"
        verbose_name_plural = "Biographies"
        ordering = ['id']


class HobbyCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "HobbyCategory"
        verbose_name_plural = "HobbyCategories"
        ordering = ['id']


class SkillCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SkillCategory"
        verbose_name_plural = "SkillCategories"
        ordering = ['id']


class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hobby')
    category = models.ForeignKey(HobbyCategory, on_delete=models.CASCADE, related_name='hobby_category')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"
        ordering = ['id']


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill')
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skill_category')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

