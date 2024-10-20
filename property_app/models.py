from django.db import models

# Property model represents a real estate property
class Property(models.Model):
    # Choices for property types
    PROPERTY_TYPES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Commercial', 'Commercial'),
    ]
    # Name of the property
    name = models.CharField(max_length=100)
    # Address where the property is located
    address = models.CharField(max_length=255)
    # Type of property 
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    # A brief description of the property
    description = models.TextField()
    # Total number of units in the property
    number_of_units = models.IntegerField()

    def __str__(self):
        #  displaying its name
        return self.name

# Unit model represents individual units within a property 
class Unit(models.Model):
    # ForeignKey links each unit to a specific property
    property = models.ForeignKey(Property, related_name='units', on_delete=models.CASCADE)
    # Unit number identifier within the property
    unit_number = models.CharField(max_length=10)
    # Number of bedrooms in the unit
    bedrooms = models.IntegerField()
    # Number of bathrooms in the unit
    bathrooms = models.IntegerField()
    # Rent amount for the unit
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    # Availability status of the unit (True if available, False if rented)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        #  displaying the unit number and property name
        return f'Unit {self.unit_number} - {self.property.name}'

# Tenant model represents a tenant who can lease units
class Tenant(models.Model):
    # Full name of the tenant
    name = models.CharField(max_length=100)
    # Email address of the tenant
    email = models.EmailField()
    # Phone number of the tenant
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        #displaying their name
        return self.name

# Lease model represents a lease agreement between a tenant and a unit
class Lease(models.Model):
    # ForeignKey linking the lease to a tenant
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # ForeignKey linking the lease to a unit
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # Start date of the lease agreement
    start_date = models.DateField()
    # End date of the lease agreement
    end_date = models.DateField()
    # Rent amount agreed upon in the lease
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       #displaying the tenant name and unit number
        return f'Lease for {self.tenant.name} - {self.unit.unit_number}'