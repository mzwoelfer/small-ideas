import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path
import unittest

HOOK_PATH = Path(__file__).resolve().parents[1] / ".github" / "hooks" / "pre-commit"
loader = SourceFileLoader("pre_commit_hook", str(HOOK_PATH))
spec = importlib.util.spec_from_loader("pre_commit_hook", loader)
pre_commit = importlib.util.module_from_spec(spec)
loader.exec_module(pre_commit)


class TestPreCommitSlugify(unittest.TestCase):
    def test_slugify_various_filenames(self):
        """
        Test slugify transforms filenames to kebab-case correctly
        """
        cases = {
            "My File.md": "my-file.md",
            "Frankfurter Straße 107 - 5.200qm gut angebunden einfach leer.md": "frankfurter-strasse-107-5200qm-gut-angebunden-einfach-leer.md",
            "README.TXT": "readme.txt",
            "already-clean.md": "already-clean.md",
            "multiple   spaces_and__underscores.JPG": "multiple-spaces-and-underscores.jpg",
            "special!@#$%^&*()chars.md": "specialchars.md",
            "Ümläuts Öff.md": "uemlaeuts-oeff.md",
        }

        for original, expected in cases.items():
            with self.subTest(filename=original):
                self.assertEqual(pre_commit.slugify(original), expected)


if __name__ == "__main__":
    unittest.main()
