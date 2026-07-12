"""
Athena Bootstrap

Creates the initial folder structure for Athena OS.

Author: Mario (Product Owner)
Architecture: YUI (Chief Architect)
Version: 1.0
"""
from pathlib import Path

PROJECT_STRUCTURE = [
    "backend",
    "frontend",
    "database",
    "docker",
    "docs",
    "tests",
    "scripts",
    ".github",
]

def create_structure():
    root = Path(__file__).parent

    for folder in PROJECT_STRUCTURE:
        path = root / folder
        path.mkdir(exist_ok=True)

        readme = path / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# {folder}\n\n"
                f"Directory created automatically by Athena Bootstrap.\n",
                encoding="utf-8"
            )

    print("🏛️ Athena Bootstrap v1.0 completed successfully.")

if __name__ == "__main__":
    create_structure()