from rest_framework import serializers
from api.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        company_id = serializers.ReadOnlyField()
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields="__all__"