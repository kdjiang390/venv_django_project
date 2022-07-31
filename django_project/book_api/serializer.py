#from asyncore import read
# from rest_framework import serializers
# from book_api.models import Book

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.quantity = data.get('quantity', instance.quantity)
#         instance.save()
#         return instance

# refactoring the code above to use the serializer class
from asyncore import read
from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value
    
    def validate_number_of_pages(self, data):
        if data["number_of_pages"] < 0:
            raise serializers.ValidationError("Number of pages must be positive")
        return data
    
    def get_description(self, data):
        return data.title + " has page count of " + str(data.number_of_pages)