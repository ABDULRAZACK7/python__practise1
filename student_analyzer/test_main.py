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

       
if __name__ == "__main__":
    unittest.main()