from rest_framework import serializers
from .models import Books

from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id','title' , 'subtitle' , 'body' , 'author' , 'isbn' , 'price')


    def validate(self, data):
        title = data.get('title', None)
        isbn = data.get('isbn', None)
        price = data.get('price', None)

        if title == '' or title.isnumeric() == True:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Ensure valid data. Title is empty or invalid."
                }
            )
        
        if Books.objects.filter(title=title, isbn=isbn).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "The data is already recorded with this title and ISBN. Bear in mind title and ISBN fields must be unique."
                }
            )
        
        if price < 0 or price > 1000000:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Ensure us with valid price. Price value must be positive number and less than 1000000."
                }
            )
            
            
        return data