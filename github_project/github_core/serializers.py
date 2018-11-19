from rest_framework.serializers import ModelSerializer
from .models import Github

class GithubSerializer(ModelSerializer):
    class Meta:
        model = Github
        fields = ('__all__')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Person` instance, given the validated data.
    #     :param validated_data:
    #     """
    #     return Github.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Person` instance, given the validated data.
    #     """

    #     instance.login = validated_data.get('login', instance.login)
    #     instance.url = validated_data.get('url', instance.url)
    #     instance.save()
    #     return instance