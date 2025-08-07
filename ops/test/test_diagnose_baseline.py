from pathlib import Path

from ops.scripts import diagnose_baseline


def test_diagnose_baseline_generates_markdown_tables():
    """diagnose_baseline.main should create a markdown file with tables."""
    output_path = Path(diagnose_baseline.__file__).with_name("diagnosis.md")
    if output_path.exists():
        output_path.unlink()

    diagnose_baseline.main()

    assert output_path.exists(), "diagnosis.md was not created"
    content = output_path.read_text()

    # Check the table header and category sections
    assert "| path | ext | version | size | date | sha1 |" in content
    assert "## Code" in content
    assert "## Documentation" in content
    assert "## Configuration" in content
    assert "## Other" in content

    output_path.unlink()
