from django.core.exceptions import ValidationError




def validate_file_size(value):
    if (value.size > 50582960):
        raise ValidationError("The Maximum File size is 50MB")
    else:
        return value