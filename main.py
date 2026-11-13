# ai-joke-03 entry: writes one fixed one-liner about AI coding agents to /output/entry.txt.
# Deterministic: the same bytes on every run. Standard library only, no network.
import os

JOKE = "My AI agent invented a library that doesn't exist, imported it anyway, and the PR passed because nobody wanted to admit they'd never heard of it."
OUTPUT_PATH = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_PATH), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
