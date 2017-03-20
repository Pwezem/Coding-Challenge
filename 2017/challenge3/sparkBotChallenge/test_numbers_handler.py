import logging as log
import unittest

from sparkBot.handlers.numbers import Numbers

from utils.logging_utils import Utils


class testNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testNumbers, cls).setUpClass()
        log.getLogger("testFuturama")
        with open("test_logs/futurama_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/futurama_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testNumbers, self).setUp()
        self.numbers = Numbers()

    def test_100_numbers_no_options(self):
        """
            Simple test to check numbers works and returns a no game due to no options supplied.
        """
        self.utils.banner("Starting Test 100 numbers command no options")

        response = self.numbers.handle_message("{}".format("numbers"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>No options supplied."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 100")

    def test_101_numbers_with_options(self):
        """
            Simple test to check numbers works and returns a game.
        """
        self.utils.banner("Starting Test 101 numbers command with options")

        response = self.numbers.handle_message("{}".format("numbers s:2 l:4"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Numbers Game**<br>**Target:** %d<br>" \
                            "**Numbers:** %d, %d, %d, %d, %d, %d" \
                            % (self.numbers.target, self.numbers.numbers[0], self.numbers.numbers[1],
                               self.numbers.numbers[2], self.numbers.numbers[3], self.numbers.numbers[4],
                               self.numbers.numbers[5])

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 101")

    def test_102_numbers_with_large_option_too_high(self):
        """
            Simple test to check numbers works and returns no game due to large option too high.
        """
        self.utils.banner("Starting Test 102 numbers command with options too high.")

        response = self.numbers.handle_message("{}".format("numbers s:0 l:7"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Large number is too big 7."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 102")

    def test_103_numbers_with_small_option_too_high(self):
        """
            Simple test to check numbers works and returns no game due to small option too high.
        """
        self.utils.banner("Starting Test 103 numbers command with small too high.")

        response = self.numbers.handle_message("{}".format("numbers s:7 l:0"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Small number is too big 7."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 103")

    @classmethod
    def tearDownClass(cls):
        super(testNumbers, cls).tearDownClass()

    def tearDown(self):
        super(testNumbers, self).tearDownClass()
        self.numbers = None

if __name__ == '__main__':
    unittest.main()