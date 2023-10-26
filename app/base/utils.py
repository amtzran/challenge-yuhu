import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    random_chain = "".join(random.choice(chars) for _ in range(size))
    return random_chain


def generate_random_slug(model, size=None):
    if size is None:
        size = model.SLUG_LENGTH
    while True:
        slug = id_generator(size=size)
        others = model.objects.filter(random_slug=slug)
        if others.count() == 0:
            return slug
        break
