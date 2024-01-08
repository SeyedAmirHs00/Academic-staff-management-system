from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from . import models
from django.db.models import ImageField


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser"
        ]


class PersonFilter(filters.FilterSet):
    user__username = filters.CharFilter(
        field_name="user__username", lookup_expr="iexact", label="Username"
    )
    user__email = filters.CharFilter(
        field_name="user__email", lookup_expr="exact", label="Email Address"
    )
    user__first_name = filters.CharFilter(
        field_name="user__first_name", lookup_expr="icontains", label="First Name"
    )
    user__last_name = filters.CharFilter(
        field_name="user__last_name", lookup_expr="icontains", label="Last Name"
    )
    persian_first_name = filters.CharFilter(
        field_name='persian_first_name', lookup_expr='icontains', label='Persian first name'
    )
    persian_last_name = filters.CharFilter(
        field_name='persian_last_name', lookup_expr='icontains', label='Persian last Name'
    )
    nationality = filters.CharFilter(
        field_name="nationality", lookup_expr="icontains", label="Nationality"
    )
    national_code = filters.CharFilter(
        field_name="national_code", lookup_expr="icontains", label="National code"
    )
    home_address__state = filters.CharFilter(
        field_name="home_address__state", lookup_expr="icontains", label="State"
    )
    home_address__city = filters.CharFilter(
        field_name="home_address__state", lookup_expr="icontains", label="City"
    )
    educations__institution_name = filters.CharFilter(
        field_name="educations__institution_name", lookup_expr="icontains", label="Institution Name"
    )
    phone_numbers__phone_number = filters.CharFilter(
        field_name="phone_numbers__phone_number", lookup_expr="icontains", label="Phone Number"
    )

    class Meta:
        model = models.Person
        fields = [
            "user",
            "user__username",
            "user__email",
            "user__first_name",
            "user__last_name",
            "persian_first_name",
            "persian_last_name",
            "nationality",
            "national_code",
            "home_address",
            "home_address__state",
            "home_address__city",
            "educations",
            "educations__institution_name",
            "phone_numbers",
            "phone_numbers__phone_number"
        ]
        filter_overrides = {
            ImageField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'label': 'Image'
                },
            },
        }


class AddressFilter(filters.FilterSet):
    state = filters.CharFilter(
        field_name="state", lookup_expr="icontains", label="State"
    )
    city = filters.CharFilter(
        field_name="city", lookup_expr="icontains", label="City"
    )
    street = filters.CharFilter(
        field_name="street", lookup_expr="icontains", label="Street"
    )
    building_name = filters.CharFilter(
        field_name="building_name", lookup_expr="icontains", label="Building Name"
    )
    district = filters.CharFilter(
        field_name="district", lookup_expr="icontains", label="District"
    )
    plate_number = filters.CharFilter(
        field_name="plate_number", lookup_expr="icontains", label="Plate Number"
    )
    postal_code = filters.CharFilter(
        field_name="postal_code", lookup_expr="icontains", label="Postal Code"
    )

    class Meta:
        model = models.Address
        exclude = ["note"]


class EducationFilter(filters.FilterSet):
    major = filters.CharFilter(
        field_name="major", lookup_expr="icontains", label="Major"
    )
    degree = filters.CharFilter(
        field_name="degree", lookup_expr="icontains", label="Degree"
    )
    institution_name = filters.CharFilter(
        field_name="institution_name", lookup_expr="icontains", label="Institution Name"
    )

    class Meta:
        model = models.Education
        fields = "__all__"


class PhoneNumberFilter(filters.FilterSet):
    phone_number = filters.CharFilter(
        field_name="phone_number", lookup_expr="icontains", label="Phone Number")

    class Meta:
        model = models.PhoneNumber
        fields = "__all__"


class BuildingFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Name")

    class Meta:
        model = models.Building
        fields = "__all__"


class FacultyFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Name"
    )
    building__name = filters.CharFilter(
        field_name="building__name", lookup_expr="icontains", label="Building Name"
    )

    class Meta:
        model = models.Faculty
        fields = "__all__"


class DepartmentFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Name"
    )
    faculty__name = filters.CharFilter(
        field_name="faculty__name", lookup_expr="icontains", label="Faculty Name"
    )
    faculty__building__name = filters.CharFilter(
        field_name="faculty__building__name", lookup_expr="icontains", label="Building Name"
    )

    class Meta:
        model = models.Department
        fields = "__all__"


class OfficeFilter(filters.FilterSet):
    phone_number__phone_number = filters.CharFilter(
        field_name="phone_number__phone_number", lookup_expr="icontains", label="Phone Number"
    )
    department__name = filters.CharFilter(
        field_name="department__name", lookup_expr="icontains", label="Department Name"
    )
    department__faculty__name = filters.CharFilter(
        field_name="department__faculty__name", lookup_expr="icontains", label="Faculty Name"
    )
    department__faculty__building__name = filters.CharFilter(
        field_name="department__faculty__building__name", lookup_expr="icontainst", label="Building Name"
    )

    class Meta:
        model = models.Office
        fields = [
            "phone_number__phone_number",
            "phone_number",
            "department__name",
            "department__faculty__name",
            "department__faculty__building__name",
            "department"
        ]


class EmployeeFilter(filters.FilterSet):
    
    class Meta:
        model = models.Employee
        fields = "__all__"


class FieldFilter(filters.FilterSet):

    class Meta:
        model = models.Field
        fields = "__all__"


class ProfessorFilter(filters.FilterSet):
    
    class Meta:
        model = models.Professor
        fields = "__all__"


class ResearcherFilter(filters.FilterSet):

    class Meta:
        model = models.Researcher
        fields = "__all__"


class ResearchFilter(filters.FilterSet):

    class Meta:
        model = models.Research
        fields = "__all__"


class ResearchMemberFilter(filters.FilterSet):

    class Meta:
        model = models.ResearchMember
        fields = "__all__"


class ScheduleFilter(filters.FilterSet):
    
    class Meta:
        model = models.Schedule
        fields = "__all__"


class LaboratoryFilter(filters.FilterSet):

    class Meta:
        model = models.Laboratory
        fields = "__all__"


class LibraryFilter(filters.FilterSet):

    class Meta:
        model = models.Library
        fields = "__all__"
