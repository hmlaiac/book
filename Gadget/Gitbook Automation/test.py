import unittest
import md_to_gitbook as _module
class GitbookTest(unittest.TestCase):
    def test_gitbook2dir(self):
        dir     = "C:\\Users\\user\\Desktop\\100-Gadget\\Gitbook Automation\\test"
        pattern = "C:\\Users\\user\\Desktop\\100-Gadget\\Gitbook Automation\\"
        result = _module.convert_dir2href(dir, pattern)
        self.assertEqual(result, "test")