from django.db import models

class Movie(models.Model):
  name_film = models.CharField(max_length=50, verbose_name="movie title")
  description = models.TextField()
  genre = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  RATING_CHOICES = (
        ('🌟','🌟' ),
        ('🌟🌟','🌟🌟' ),
        ('🌟🌟🌟','🌟🌟🌟'),
        ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟','🌟🌟🌟🌟🌟' ),
)
  rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='🌟')
  teg = models.CharField(max_length=50)

  def __str__(self):
    return self.name_film
