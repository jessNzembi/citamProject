from rest_framework import serializers
from .models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Teacher

        fields = ['first_name', 'last_name', 'password',
                  'email', 'phone_no', 'id_number', 'role']
        
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def create(self, validated_data):
        """
        Creates a new user profile from the request's data
        """
        account = Teacher(**validated_data)
        account.set_password(account.password)
        account.save()

        # user_profile = UserProfileModel.objects.create(account=account, **validated_data)
        return account
    
    def update(self, instance, validated_data):
        """
        Updates a user's profile from the request's data
        """
        instance.set_password(instance.password)
        validated_data["password"] = instance.password
        return super().update(instance, validated_data)
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = ['first_name', 'last_name', 'grade', 'parent']
        
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def create(self, validated_data):
        """
        Creates a new user profile from the request's data
        """
        account = Student(**validated_data)
        account.set_password(account.password)
        account.save()

        # user_profile = UserProfileModel.objects.create(account=account, **validated_data)
        return account
    
    def update(self, instance, validated_data):
        """
        Updates a user's profile from the request's data
        """
        instance.set_password(instance.password)
        validated_data["password"] = instance.password
        return super().update(instance, validated_data)