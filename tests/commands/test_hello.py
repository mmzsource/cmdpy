"""Tests for our `prn hello` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['prn', 'hello'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['prn', 'hello'], stdout=PIPE).communicate()[0]
        self.assertTrue('Hello World' in output)

    def test_returns_hello_world_uppercase(self):
        output = popen(['prn', 'hello', '--uc'], stdout=PIPE).communicate()[0]
        self.assertTrue("HELLO WORLD" in output)

    def test_returns_hello_world_lowercase(self):
        output = popen(['prn', 'hello', '--lc'], stdout=PIPE).communicate()[0]
        self.assertTrue("hello world" in output)

