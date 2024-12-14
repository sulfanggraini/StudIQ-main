from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, blank=True, null=True)

    #add any additional atributes you want
    portofolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank= True)

    #create__str__method to overide the default one
    def __str__(self):
        return self.user.username



# GABUNGAN DARI WARDAH & RANGGA
# Models untuk Video Kelas 4 Bahasa inggris
class Videoing(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

# Models untuk Video Kelas 5 Bahasa inggris
class Videoing2(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Videoing2'  # Nama tabel di database
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

# Models untuk Materi Mapel IPA Kelas 4
class Materiipa4(models.Model):
    title = models.CharField(max_length=255)  # Judul materi
    pdf = models.FileField(upload_to='pdf/')
    order = models.PositiveIntegerField()  # Urutan materi

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"


# Models untuk Video Mapel IPA Kelas 4
class Videoipa(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

# Models untuk Video Mapel IPA Kelas 5
class Videoipa2(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Videoipa2'  # Nama tabel di database
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"
       
# Models untuk Video Kelas 4 Matematika
class Video1mtkkls4(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

class Video2mtkkls4(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"
        
class Video3mtkkls4(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

class Video4mtkkls4(models.Model):
    title = models.CharField(max_length=255)  # Judul video
    url = models.URLField()  # Link video
    order = models.PositiveIntegerField()  # Urutan video

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Mengatur urutan berdasarkan kolom "order"

# MODELS QUIZ
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)  # "A", "B", "C", atau "D"

    def __str__(self):
        return self.question

class QuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1)  # "A", "B", "C", atau "D"
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.question}"