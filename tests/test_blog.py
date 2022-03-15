from app.models import Blog,User
from app import db
import unittest

class BlogTest(unittest.TestCase):

    def setUp(self):
        self.user_Venus = User(username = 'venus',password = 'test', email = 'venus@gg.com')
        self.new_blog = Blog(title="Money",post= "Advertise good products",user = self.user_Venus )
            
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
            
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,"Money")
        self.assertEquals(self.new_blog.post,"Advertise good products")
        self.assertEquals(self.new_blog.category,"Product")
        self.assertEquals(self.new_blog.user,self.user_Venus)
        
    def test_save_blog(self):
        self.new_blog.save_review()
        self.assertTrue(len(Blog.query.all())>0)
        