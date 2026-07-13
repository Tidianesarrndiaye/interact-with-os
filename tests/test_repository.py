from pathlib import Path


def test_readme_exists():
    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    assert readme_path.exists()


def test_readme_has_title():
    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    content = readme_path.read_text(encoding="utf-8")
    assert "# interact-with-os" in content
