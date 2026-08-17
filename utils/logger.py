"""
Centralized logger setup using loguru.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}")

__all__ = ["logger"]
