import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('Результаты забегов:')
        for key in sorted(cls.all_result.keys()):
            print(cls.all_result[key])

    def test_runner1_vs_runner3(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_result[1] = {1: result[1].name, 2: result[2].name}
        self.assertTrue(result[max(result)] == 'Ник')

    def test_runner2_vs_runner3(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_result[2] = {1: result[1].name, 2: result[2].name}
        self.assertTrue(result[max(result)] == 'Ник')

    def test_runner1_runner2_runner3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        self.all_result[3] = {1: result[1].name, 2: result[2].name, 3: result[3].name}
        self.assertTrue(result[max(result)] == 'Ник')


if __name__ == '__main__':
    unittest.main()