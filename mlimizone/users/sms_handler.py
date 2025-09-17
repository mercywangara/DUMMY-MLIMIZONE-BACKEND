def register_farmer_from_sms(name, location, phone_number):
    farmer, created = User.objects.get_or_create(
        phone_number=phone_number,
        defaults={
            'name': name,
            'location': location,
            'role': 'farmer',
            'email': None,
        }
    )
    if created:
        farmer.set_unusable_password()
        farmer.save()
    else:
        farmer.name = name
        farmer.location = location
        farmer.save()
    return farmer