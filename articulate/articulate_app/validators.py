from django.core.exceptions import ValidationError


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    kb_limit = 1000
    if filesize > kb_limit*1024:
        raise ValidationError(f"Max file size is {kb_limit}kb")


def validate_rating(num):
    limit = 5
    if num <= 0 or num > limit:
        raise ValidationError(f"Rating can vary in 0.1 to {limit}")
    elif len(tuple(str(num))) > 3:
        raise ValidationError("Upto one decimal eg. 1.1(correct) 1.11(wrong)")


def validate_imdb_rating(num):
    limit = 10
    if num <= 0 or num > limit:
        raise ValidationError(f"Rating can vary in 0.1 to {limit}")
    elif len(tuple(str(num))) > 3:
        raise ValidationError("Upto one decimal eg. 1.1(correct) 1.11(wrong)")
