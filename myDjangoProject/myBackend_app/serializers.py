from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'language', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn']

    def get_translated_question(self, obj):
        """Fetches translated question based on query parameter"""
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en')  # Default to English
        return obj.get_translated_question(lang)
