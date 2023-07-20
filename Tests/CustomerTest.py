from unittest import TestCase


class TestCustomer(TestCase):
    def test1(self):
        my_name = "Hello" + " Test!"
        self.assertEqual("Hello Test!", my_name)
