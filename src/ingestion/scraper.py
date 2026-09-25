"""
scraper — Multi-platform rental listing data collector.

TODO (Sprint 2):
    - Implement scraping logic for target platforms.
    - Respect robots.txt and rate-limit requests.
    - Store raw output in data/raw/ with timestamps.
"""

from __future__ import annotations

from pathlib import Path

RAW_DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "raw"


def scrape_listings(source: str, output_dir: Path = RAW_DATA_DIR) -> Path:
    """Scrape rental listings from *source* and save to *output_dir*.

    Parameters
    ----------
    source : str
        Identifier for the data source (e.g. ``"magicbricks"``, ``"99acres"``).
    output_dir : Path
        Directory to write the raw CSV/JSON file.

    Returns
    -------
    Path
        Path to the saved file.

    Raises
    ------
    NotImplementedError
        This function is a placeholder for Sprint 2.
    """
    raise NotImplementedError(
        f"Scraper for '{source}' is not yet implemented. See Sprint 2 backlog."
    )
