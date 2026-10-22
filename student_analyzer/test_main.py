import unittest

from main import analyze_marks


class TestStudentAnalyzer(unittest.TestCase):
    def test_analyze_marks(self):
        marks = [85, 90, 72, 96, 78]
        result = analyze_marks(marks)

        self.assertEqual(result["total"], 421)
        self.assertAlmostEqual(result["average"], 84.2)
        self.assertEqual(result["highest"], 96)
        self.assertEqual(result["lowest"], 72)
        self.assertEqual(result["count"], 5)
        self.assertEqual(result["grades"]["A"], 2)
        self.assertEqual(result["grades"]["B"], 1)
        self.assertEqual(result["grades"]["C"], 2)  
        self.assertEqual(result["grades"]["D"], 0)

    def test_average_marks(self):
        marks=[85, 90, 72, 96, 78]

        result=analyze_marks(marks)
        self.assertAlmostEqual(result["average"],84.2)

    def test_negative_marks(self):
        marks = [85, 90, -5, 96, 78]
        with self.assertRaises(ValueError):
            analyze_marks(marks)
    def test_marks_above_100(self):
        marks=[10,20,80,105,245]
        with self.assertRaises(ValueError):
            analyze_marks(marks)

    def test_mixed_marks(self):
        marks=[80,30,45,20,90]
        result=analyze_marks(marks)
        self.assertEqual(result["passed"],3)

    def test_all_failed(self):
        marks=[10,20,30,25,15]
        result=analyze_marks(marks)
        self.assertEqual(result["failed"],5)

    def test_all_passed(self):
        marks=[80,90,75,85,95]
        result=analyze_marks(marks)
        self.assertEqual(result["passed"],5)
    def test_boundary_marks(self):
        marks=[0,35,100]
        result=analyze_marks(marks)
        self.assertEqual(result["failed"],1)
        self.assertEqual(result["passed"],2)
       
if __name__ == "__main__":
    unittest.main()