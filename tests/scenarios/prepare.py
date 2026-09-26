"""Prepare isolated behavioral fixtures; does not run or grade an agent."""

import argparse
import json
from pathlib import Path
import shutil


def prepare(destination):
    source = Path(__file__).resolve().parent
    destination.mkdir(parents=True, exist_ok=False)
    for case in json.loads((source / "cases.json").read_text(encoding="utf-8")):
        folder = destination / case["id"]
        project = folder / "project"
        project.mkdir(parents=True)
        for name, content in case["files"].items():
            path = project / name
            # H08 intentionally includes a sibling project, inside its case only.
            path.resolve().relative_to(folder.resolve())
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        for name, target in case.get("symlinks", {}).items():
            link = project / name
            link.resolve().relative_to(folder.resolve())
            (link.parent / target).resolve().relative_to(folder.resolve())
            link.symlink_to(target)
        (folder / "request.md").write_text(case["prompt"] + "\n", encoding="utf-8")
    shutil.copytree(source.parents[1] / "skills/dev-mind", destination / "skill-baseline")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New output directory (must not exist)")
    prepare(parser.parse_args().output)
