"""Loads settings from environment variables or a local .env file."""
import os

from dotenv import load_dotenv

load_dotenv()


def get_api_key():
    """Return the Anthropic API key, or None if it isn't set."""
    return os.environ.get("ANTHROPIC_API_KEY")
