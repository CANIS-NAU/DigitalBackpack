from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('roll','phone', 'address', 'subject')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    profile = UserProfileSerializer(required=True)
    password = serializers.CharField(max_length=100,style={'input_type': 'password'})
    password2 = serializers.CharField(max_length=100,label='Confirm Password',style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id','email', 'first_name', 'last_name', 'password', 'password2','profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password == password2:
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, **profile_data)
            
        else:
            raise serializers.ValidationError(' Password: passwords are not matched')
        return user
    


    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        
        profile.roll = profile_data.get('roll', profile.roll)
        profile.phone = profile_data.get('dob', profile.phone)
        profile.address = profile_data.get('address', profile.address)
        profile.subject = profile_data.get('country', profile.subject)
        profile.save()

        return instance