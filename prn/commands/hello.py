"""The hello command."""


from json import dumps

from .base import Base


class Hello(Base):
    """Say hello, world!"""

    def __init__(self, options, *args, **kwargs):
        super(Hello, self).__init__(options, *args, **kwargs)
        self.hello_world = 'Hello World'

    def run(self):
        if self.options['--uc']:
            print '\n' + self.hello_world.upper()
        elif self.options['--lc']:
            print '\n' + self.hello_world.lower()
        else:
            print '\n' + self.hello_world
        print '\nYou supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
