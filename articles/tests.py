from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Article
# Create your tests here.
class ArticleTests(TestCase):

# Test for setting up/creating a user
    def setUp(self):
        self.user = get_user_model().objects.create_user (
            first_name= 'Gerald',
            last_name= 'Musa',
            username='testuser',
            email='test@email.com',
            password='secret'
            )

# Test for setting up/creating a article object
        self.article = Article.objects.create (
            author = self.user,
            title = 'this is a test title',
            body = "this is a body for the test",
        )

# # Test to check that there is a place/page for an article when it is  successfully submitted/created
#     # def test_get_absolute_url(self): # new
#     #     self.assertEqual(self.article.get_absolute_url(), '/articles/1/')
    
# Test to check that the article's content (title, body ...) is a string
    def test_string_representation(self):
        article = Article(title='A sample title')
        self.assertEqual(str(article), article.title)

# Test to ensure that the articles content is what we entered when 
    def test_article_content(self):
        self.assertEqual(f'{self.article.title}', 'this is a test title')
        self.assertEqual(f'{self.article.author}', 'testuser')
        self.assertEqual(f'{self.article.body}', "this is a body for the test")

# Test for List View     
    def test_article_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response.content, "this is a body for the test")
        self.assertTemplateUsed(response, 'home.html')

# # Test for Detail View 
#     def test_article_detail_view(self):
#         response = self.client.get('/articles/1/')
#         no_response = self.client.get('/articles/100000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'this is a test title')
#         self.assertTemplateUsed(response, 'article_detail.html')

# Test for Create View 
    # def test_article_create_view(self): # new
    #     response = self.client.post(reverse('create'), {
    #         'title': 'New title',
    #         'body': 'New text',
    #         'author': self.user.id,
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Article.objects.last().title, 'New title')
    #     self.assertEqual(Article.objects.last().body, 'New text')

# # Test for Update View 
#     def test_article_update_view(self): # new
#         response = self.client.post(reverse('update', args='1'), {
#             'title': 'Updated title',
#             'body': 'Updated text',
#         })
#         self.assertEqual(response.status_code, 302)

# # Test for Delete View 
#     def test_article_delete_view(self): # new
#         response = self.client.post(reverse('article_delete', args='1'))
#         self.assertEqual(response.status_code, 302)

