from django.utils.functional import classproperty


class Units:
    gram = "g"
    ml = "mL"

    @classproperty
    def choices(cls):
        return tuple((__i.value, __i.name) for __i in cls)
