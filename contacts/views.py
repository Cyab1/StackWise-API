from rest_framework import generics, status
from rest_framework.response import Response
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView, UpdateAPIView

@method_decorator(ratelimit(key='ip', rate='5/h', method='POST', block=True), name='post')
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        send_mail(
            subject=f"New contact form: {contact.subject}",
            message=(
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Phone: {contact.phone}\n"
                f"Service interest: {contact.service_interest}\n\n"
                f"Message:\n{contact.message}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['stackwiseza@gmail.com'],
            fail_silently=True,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['patch']    