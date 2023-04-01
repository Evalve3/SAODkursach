import unittest


def run_all_test():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.discover("test"))
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    run_all_test()