"""Command-line entry point for the study bot."""
import argparse

from course_notes_rag import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="notesbot",
        description="Ask questions about your course notes.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.parse_args()
    print("notesbot is set up. Ingestion and Q&A arrive in later phases.")


if __name__ == "__main__":
    main()
