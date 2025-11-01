from pathlib import Path
from datetime import datetime, timedelta
import logging


def clean_old_files(
    target_dir: Path,
    logger: logging,
    extensions: tuple[str],
    days: int = 7,
    dry_run: bool = True,
) -> int:
    """Delete files older than N days. Return count of deleted files."""
    # datetime of now
    if not target_dir.exists():
        logger.warning("Tagret directory does not exist: %s", target_dir)
        return 0
    now = datetime.now()
    count = 0
    logger.info(
        "Starting cleanup in %s (extensions: %s, days: %d, dry_run: %s)",
        target_dir,
        extensions,
        days,
        dry_run,
    )
    for file in target_dir.iterdir():
        try:
            if dry_run:
                logger.info("[Dry-run] would delete: %s", file)
            if file.is_file():
                creation_day = datetime.fromtimestamp(file.stat().st_ctime)
                if file.suffix in extensions and (now - creation_day) > timedelta(
                    days=days
                ):
                    file.unlink()
                    count += 1
                    logger.info("%s deleted", file)
        except FileNotFoundError:
            logger.warning("%s skiped", file)
    logger.info("Cleanup completed: %d files deleted", count)
    return count


def main() -> None:
    """Program main entry point"""
    logging.basicConfig(
        filename="test.log",
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )
    logger = logging.getLogger()
    p = Path("data")
    deleted = clean_old_files(p, logger, (".log", ".txt"), days=0, dry_run=False)
    print(f"Total files (dry-run): {deleted}")


if __name__ == "__main__":
    main()
