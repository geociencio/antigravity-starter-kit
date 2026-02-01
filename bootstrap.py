#!/usr/bin/env python3
"""
Bootstrap script for Antigravity-powered projects.
Automates project name replacement and environment initialization.
"""

import os
import subprocess
import sys
from pathlib import Path

def setup_project():
    print("🚀 Antigravity Project Bootstrapper")
    print("-----------------------------------")
    
    # Get project name
    project_name = input("Enter the new project name: ").strip()
    if not project_name:
        print("❌ Error: Project name cannot be empty.")
        sys.exit(1)
    
    # Files to process
    files_to_process = [
        Path("pyproject.toml"),
        Path("README.md"),
    ]
    
    # Placeholder
    placeholder = "{{PROJECT_NAME}}"
    
    print(f"\n📝 Replacing placeholders in {len(files_to_process)} files...")
    
    for file_path in files_to_process:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding="utf-8")
                if placeholder in content:
                    new_content = content.replace(placeholder, project_name)
                    file_path.write_text(new_content, encoding="utf-8")
                    print(f"  ✅ Updated {file_path}")
                else:
                    print(f"  ⚠️  Placeholder not found in {file_path}")
            except Exception as e:
                print(f"  ❌ Error processing {file_path}: {e}")
        else:
            print(f"  ⚠️  File {file_path} not found.")

    # Initialize uv environment
    print("\n📦 Initializing environment with `uv sync`...")
    try:
        subprocess.run(["uv", "sync"], check=True)
        print("  ✅ Environment initialized successfully.")
    except subprocess.CalledProcessError:
        print("  ❌ Error: Failed to run `uv sync`. Make sure `uv` is installed.")
        sys.exit(1)
    except FileNotFoundError:
        print("  ❌ Error: `uv` command not found. Please install `uv` (https://github.com/astral-sh/uv).")
        sys.exit(1)

    print("\n✨ Bootstrap complete! Your project is ready.")
    print(f"Next steps:")
    print(f"1. Explore AGENTS.md in scaffold/")
    print(f"2. Run `/inicia-sesion` to start collaborating with your agent.")
    
    # Self-destruct? (Optional: The user might want to keep it or delete it manually)
    delete_self = input("\nDo you want to delete this bootstrap script? (y/N): ").lower()
    if delete_self == 'y':
        try:
            os.remove(__file__)
            print("  ✅ bootstrap.py removed.")
        except Exception as e:
            print(f"  ⚠️  Could not remove bootstrap.py: {e}")

if __name__ == "__main__":
    setup_project()
