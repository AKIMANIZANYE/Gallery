



from django.test import TestCase
from .models import Image,Category,Location

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Location()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Location))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Category()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Category))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_cat()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Image( photo='image(5).jpeg',name = 'potato', description='food in potato')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Image))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0) 
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)           
          