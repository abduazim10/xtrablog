from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    
    def get_images(self):
        return BlogImage.objects.filter(blog_id=self.id)[1:]
    
    def get_birinchi_image(self):
        return BlogImage.objects.filter(blog_id=self.id)[0].image.url

    def __str__(self):
        return self.title

    
class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog')

    def __str__(self):
        return f"{self.blog_id.title} ning rasmi"
    

class Comment(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} - {self.blog_id.title}'
    
    