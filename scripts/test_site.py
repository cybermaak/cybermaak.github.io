"""Regression checks for the boundary between repository and public artifact."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("website", Path(__file__).with_name("site.py"))
website = importlib.util.module_from_spec(spec)
spec.loader.exec_module(website)


class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.public = self.root / "public"
        self.public.mkdir()
        for route in ("", "polytray/", "maakdown/", "khatmah/"):
            page = self.public / route / "index.html"
            page.parent.mkdir(exist_ok=True)
            page.write_text(
                '<!doctype html><html><head><title>Fixture</title>'
                f'<link rel="canonical" href="https://cybermaak.dev/{route}">'
                '</head><body><h1>Fixture</h1><a href="/">Home</a></body></html>'
            )
        (self.public / "404.html").write_text('<title>Missing</title><a href="/">Home</a>')
        (self.public / "CNAME").write_text("cybermaak.dev\n")
        (self.public / ".nojekyll").touch()

    def build(self):
        with patch.multiple(website, ROOT=self.root, PUBLIC=self.public, DIST=self.root / "dist"):
            website.build()

    def test_build_excludes_repository_files_and_cleans_stale_output(self):
        (self.root / "AGENTS.md").write_text("Repository instructions, not a web page")
        (self.root / ".git").mkdir()
        (self.root / ".git/HEAD").write_text("fixture repository metadata")
        (self.root / "dist").mkdir()
        (self.root / "dist/AGENTS.md").write_text("stale artifact")
        self.build()
        artifact = self.root / "dist"
        self.assertTrue((artifact / "maakdown/index.html").is_file())
        self.assertFalse((artifact / "AGENTS.md").exists())
        self.assertFalse((artifact / ".git").exists())
        self.assertTrue((self.root / ".git/HEAD").is_file())

    def test_missing_asset_and_anchor_fail_validation(self):
        page = self.public / "index.html"
        original = page.read_text()
        for reference in ('<img alt="Fixture" src="missing.png">', '<a href="/maakdown/#missing">Read</a>'):
            with self.subTest(reference=reference):
                page.write_text(original + reference)
                with self.assertRaisesRegex(ValueError, "missing (local destination|anchor)"):
                    website.validate(self.public)

    def test_hidden_content_and_maintenance_docs_are_rejected(self):
        for filename in (".env", "AGENTS.md", "capture.py"):
            with self.subTest(filename=filename):
                path = self.public / filename
                path.write_text("fixture")
                with self.assertRaisesRegex(ValueError, "not publishable|unsupported public file type"):
                    website.validate(self.public)
                path.unlink()

    def test_symlink_cannot_import_a_file_from_outside_public(self):
        private = self.root / "private.txt"
        private.write_text("fixture")
        (self.public / "image.png").symlink_to(private)
        with self.assertRaisesRegex(ValueError, "symlinks are not publishable"):
            website.validate(self.public)

    def test_hard_link_is_not_published(self):
        private = self.root / "private.txt"
        private.write_text("fixture")
        os.link(private, self.public / "image.png")
        with self.assertRaisesRegex(ValueError, "hard links are not publishable"):
            website.validate(self.public)

    def test_build_does_not_follow_a_dist_symlink(self):
        other = self.root / "other"
        other.mkdir()
        sentinel = other / "keep.txt"
        sentinel.write_text("preserve")
        (self.root / "dist").symlink_to(other, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "dist must be a generated directory"):
            self.build()
        self.assertEqual(sentinel.read_text(), "preserve")


if __name__ == "__main__":
    unittest.main()
