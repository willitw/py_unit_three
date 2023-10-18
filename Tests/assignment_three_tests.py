import unittest
import assignment_three

class TestAssignmentThree(unittest.TestCase):

    def test_area_of_rectangle(self):

        self.assertEqual(assignment_three.area_of_rectangle(4, 5), 20)

        self.assertAlmostEqual(assignment_three.area_of_rectangle(3.5, 2.5), 8.75, places=2)

        self.assertEqual(assignment_three.area_of_rectangle(0, 5), 0)
        self.assertEqual(assignment_three.area_of_rectangle(3.5, 0), 0)

        self.assertEqual(assignment_three.area_of_rectangle(-4, 5), -20)
        self.assertEqual(assignment_three.area_of_rectangle(3.5, -2.5), -8.75)

if __name__ == "__main__":
    unittest.main()
