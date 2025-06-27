from rest_framework import serializers


class BaseAuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")
        if request and not request.user.is_anonymous:
            validated_data["author"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("author", None)
        return super().update(instance, validated_data)
