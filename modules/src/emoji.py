import random
from templates.text import TextTemplate


def process(input):
    emoji = [
        ':P',
        ':)',
        ':O',
        'B-)',
        '-_-',
        ':D'
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(emoji)).get_message(),
        'success': True
    }
    return output
