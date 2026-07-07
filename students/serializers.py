from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


    #Name Validation
    def validate_name(self,value):
        if len(value)<3:
            raise serializers.ValidationError("Name must contain at least 3 characters.")
        return value
    
    #Phone Validation
    def validate_phone(self, value):
        if len(value)!=10:
            raise serializers.ValidationError("Phone Number must contain 10 digits.")
        if not value.isdigit():
            raise serializers.ValidationError("Phone number should contain only digits.")
        return value
    
    #Age Validation
    def validate_age(self, value):
        if value<18:
            raise serializers.ValidationError("Student must be 18 years old.")
        return value
        
    
        