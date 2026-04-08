import os
import subprocess
import sys

CLI = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "thumbnail.py")


def test_cli_generates_png(tmp_path):
    output = str(tmp_path / "out.png")
    result = subprocess.run(
        [sys.executable, CLI, "--title", "テスト", "--output", output],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert os.path.exists(output)


def test_cli_default_output_name(tmp_path):
    result = subprocess.run(
        [sys.executable, CLI, "--title", "テストタイトル"],
        capture_output=True, text=True, cwd=str(tmp_path),
    )
    assert result.returncode == 0, result.stderr
    expected = tmp_path / "thumbnail-テストタイトル.png"
    assert expected.exists()


def test_cli_dark_template(tmp_path):
    output = str(tmp_path / "dark.png")
    result = subprocess.run(
        [sys.executable, CLI, "--title", "ダーク", "--template", "dark", "--output", output],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert os.path.exists(output)


def test_cli_all_options(tmp_path):
    output = str(tmp_path / "full.png")
    result = subprocess.run(
        [
            sys.executable, CLI,
            "--title", "タイトル",
            "--subtitle", "サブタイトル",
            "--author", "著者名",
            "--template", "gradient",
            "--output", output,
        ],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert os.path.exists(output)


def test_cli_missing_title_exits_nonzero():
    result = subprocess.run(
        [sys.executable, CLI],
        capture_output=True, text=True,
    )
    assert result.returncode != 0


def test_sanitize_filename():
    from thumbnail import sanitize_filename
    assert sanitize_filename("Hello World") == "Hello-World"
    assert "/" not in sanitize_filename("path/to/file")
    assert "\\" not in sanitize_filename("path\\to\\file")
    assert len(sanitize_filename("a" * 200)) <= 80
