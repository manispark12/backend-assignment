from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('tg', 'Telugu'),
    ]

    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support

    # Translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')

    def get_translated_answer(self, lang):
        """Returns the answer in the requested language, defaults to English if not available."""
        if lang == 'hi' and self.answer_hi:
            return self.answer_hi
        elif lang == 'bn' and self.answer_bn:
            return self.answer_bn
        return self.answer

    def get_translated_question(self, lang):
        """Returns the question in the requested language, defaults to English if not available."""
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  # Default to English

    def __str__(self):
        return self.question


# Create your models here.
