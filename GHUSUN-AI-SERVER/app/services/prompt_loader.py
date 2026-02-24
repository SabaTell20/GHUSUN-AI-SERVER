from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # points to /app


def load_prompt(filename: str) -> str:
    prompt_path = BASE_DIR / "prompts" / filename
    return prompt_path.read_text(encoding="utf-8")