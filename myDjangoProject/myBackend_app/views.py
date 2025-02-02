from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the FAQ API! Use /api/"})
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """Use caching to store and retrieve FAQ responses"""
        lang = request.query_params.get('lang', 'en')  # Get the language from the query params
        cache_key = f"faqs_{lang}"  # Unique cache key for each language
        cached_data = cache.get(cache_key)

        if cached_data:
            print("Cache Hit!")  # Debugging
            return Response(cached_data)  # Return cached response

        print("Cache Miss!")  # Debugging
        queryset = self.get_queryset()

        # Translate questions and answers for the requested language
        faqs = []
        for faq in queryset:
            translated_question = faq.get_translated_question(lang)
            translated_answer = faq.get_translated_answer(lang)
            faqs.append({
                'question': translated_question,
                'answer': translated_answer,
            })

        # Cache the translated FAQ data for the requested language
        cache.set(cache_key, faqs, timeout=60*15)  # Cache for 15 minutes

        return Response(faqs)
