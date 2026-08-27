from rest_framework import generics
from .models import Testimonial
from .serializers import TestimonialSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.filter(is_approved=True)
    serializer_class = TestimonialSerializer

class TestimonialCreateView(CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestimonialUpdateView(UpdateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['patch']    