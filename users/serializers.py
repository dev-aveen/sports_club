from rest_framework import serializers
from .models import User
from club.models import Gym

class UserSerializer(serializers.ModelSerializer):
    gym_name = serializers.CharField(write_only=True,required=True)
    class Meta:
        
        model = User
        fields = ['username','full_name','password','gym_name']
        extra_kwargs = {'password':{'write_only':True}}
    #للتعامل مع البيانات وتشفير كلمة المرور
    def create(self,validated_data):
            gym_name = validated_data.pop('gym_name')
            gym = Gym.objects.create(name=gym_name)
            user = User.objects.create_user(gym = gym,**validated_data)
            user.is_staff = True
            user.save()
            return user
    #لتحديث البيانات
    def update(self, instance, validated_data):
        password= validated_data.pop('password',None)
        for attr , value in validated_data.items():
             setattr(instance,attr,value)
        if password:
             instance.set_password(password)
        instance.save()
        return instance