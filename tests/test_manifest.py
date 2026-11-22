import unittest
from magic_mead.cli import make_manifest
class TestManifest(unittest.TestCase):
 def test_three_phases(self):
  m=make_manifest("SP_010_011")
  self.assertEqual([x["name"] for x in m["phases"]],["illustration","typesetting","audit"])
  self.assertIn("text_verbatim",m["phases"][2]["checks"])
if __name__=="__main__": unittest.main()
