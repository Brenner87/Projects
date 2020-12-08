import collection_in_collection
import unittest
import logging

logging.basicConfig(level=logging.INFO)

class test_collection(unittest.TestCase):
    config = {
        'name': 'test',
        'nexus': {
            'version': '1.96',
        },
        'banks': {
            2096: {
                'version': '1.33',
            },
        },
    }
    known_values = {
                       'name': 'test',
                       'nexus.version': '1.96',
                       'banks.2096.version': '1.33',
    }

    incorrect_values = {
                       'name': 'test1',
                       'nexus.version': '1.97',
                       'banks.2096.version': '1.34',
                       'version': '12.3',
                       'nexus.pattern': 'abc',
                       'nexus..version': '13',
                       '..value': 'foo',
    }

    values_to_update = {
                       'name': 'test1',
                       'nexus.version': '1.97',
                       'banks.2096.version': '1.34',
                       'version': '12.3',
                       'nexus.pattern': 'abc',
                       'nexus..version': '13',
                       '..value': 'foo',
    }

    def test_check_config_true(self):
        """If value is found have to return True"""
        for k, v in self.known_values.items():
            logging.info('Checking {}: {}'.format(k,v))
            self.assertTrue(collection_in_collection.check_config(self.config, k, v))

    def test_check_config_false(self):
        """If value is not found, return False"""
        for k, v in self.incorrect_values.items():
            logging.info('Checking {}: {}'.format(k, v))
            self.assertFalse(collection_in_collection.check_config(self.config, k, v))

    def test_set_value(self):
        """Check updated config"""
        for k, v in self.values_to_update.items():
            logging.info('Updating {}: {}'.format(k, v))
            config = collection_in_collection.set_value(self.config, k, v)
            self.assertTrue(collection_in_collection.check_config(config, k, v))


if __name__ == '__main__':
    unittest.main()