from module_12_1_hw import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Stepan')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50) # Проверяем итоговое расстояние после всех шагов

    def test_run(self):
        runner = Runner('Svyat')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100) # Проверяем итоговое расстояние после всех пробежек

    def test_challenge(self):
        runner1 = Runner('Mir')
        runner2 = Runner('Nat')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance) # Проверяем, что расстояния разные


if __name__ == '__main__':
    unittest.main()

# Вывод на консоль: Ran 3 tests in 0.001s OK