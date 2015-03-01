# import datetime
#
# from haystack import indexes
# from task.models import Task
#
#
# class TaskIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     pub_date = indexes.DateTimeField(model_attr='pub_date')
#
#     content_auto = indexes.EdgeNgramField(model_attr='title')
#
#     def get_model(self):
#         return Task
#
#     """
#     return all the objects
#     """
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()
import datetime
from haystack import indexes
from task.models import cs499Item


# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     author = indexes.CharField(model_attr='user')
#     pub_date = indexes.DateTimeField(model_attr='pub_date')
#
#     def get_model(self):
#         return Note
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


# class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     title = indexes.CharField(model_attr='title')
#     body = indexes.CharField(model_attr='body')
#
#     def get_model(self):
#         return Article
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()

class cs499itemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    authors = indexes.NgramField(model_attr='authors')
    abstract = indexes.NgramField(model_attr='abstract')
    subjects = indexes.NgramField(model_attr='subjects')
    category = indexes.CharField(model_attr='category')
    date = indexes.DateTimeField(model_attr='date')
    likes = indexes.IntegerField(model_attr='likes', indexed=False)
    urllink = indexes.CharField(model_attr='urllink', indexed=False)
    pdflink = indexes.CharField(model_attr='pdflink', indexed=False)


    def get_model(self):
        return cs499Item

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    # def prepare_feed_text(self, obj):
    #     return "Feed"
    #
    # def prepare(self, obj):
    #     data = super(cs499itemIndex, self).prepare(obj)
    #     data['boost'] = 1.5
    #     return data
