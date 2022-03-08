from django.db import models
from .validators import validate_file_size




class SendResumeModel(models.Model):
    fullname = models.CharField(max_length=250 , verbose_name='Full Name')
    email = models.EmailField(max_length=250 , verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    cv = models.FileField(null=True , blank=True , upload_to='uploads/cv' , validators=[validate_file_size] , verbose_name='CV')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='Created At')
    is_read_by_admin = models.BooleanField(default=False , verbose_name='Read By Admin')
    
    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
    
    def __str__(self) -> str:
        super(SendResumeModel , self).__str__()
        return self.fullname
    
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'List of Resumes'