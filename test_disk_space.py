import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from disk_space import report
class T(unittest.TestCase):
    def test_root(self):
        r = report("/")
        self.assertGreater(r["total_gb"], 0)
        self.assertGreaterEqual(r["used_pct"], 0)
        self.assertLessEqual(r["used_pct"], 100)
if __name__ == "__main__": unittest.main()
