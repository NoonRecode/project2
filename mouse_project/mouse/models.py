from django.db import models

class MouseBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Mouse(models.Model):
    brand = models.ForeignKey(MouseBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='mouse_images/')
    description = models.TextField()

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)  # หัวข้อข่าว
    image = models.ImageField(upload_to='news_images/')  # อัปโหลดรูปภาพ
    content = models.TextField()  # เนื้อหาข่าว
    date_posted = models.DateTimeField(auto_now_add=True)  # วันที่โพสต์

    def __str__(self):
        return self.title
