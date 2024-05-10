from random import randint

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# from config.settings import emails_list, EMAIL_HOST_USER

from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
def insert_email_4_reset_password(request):
    email = request.data['email']
    user = get_user_model()
    if user.objects.filter(email=email).exists():
        num = randint(100000, 999999)
        emails_list[email] = num
        send_mail(
            subject="Code for reset password",
            message=f"Code for change your password: {num}\n",
            from_email=EMAIL_HOST_USER,
                    # f"URL: http://localhost:8000/api/v1/accounts/password_reset/confirm/",
            recipient_list=[email],
        )
        return Response({'message': 'Code for reset password sent to your email.'}, status=200)
    else:
        return Response({'message': 'Email does not exist'}, status=400)


@api_view(['POST'])
def reset_password(request):
    code = request.data['code']
    email = request.data['email']
    password1 = request.data['password1']
    password2 = request.data['password2']

    if password1 == password2:
        try:
            if code == emails_list[email]:
                user = get_user_model().objects.get(email=email)
                user.set_password(password1)
                user.save()
                # print(emails_list)
                del emails_list[email]
                # print(emails_list)
                return Response('Password reset successful.', status=200)
            else:
                return Response({'message': 'Email or code do not match'}, status=400)
        except:
            return Response({'message': 'Email or code do not match'}, status=400)


