from django.contrib.auth.models import User

class UserSerializer(models.ModelSerializer)
    class Meta:
        model = User
        fields = "__all__"
