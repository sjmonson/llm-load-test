#!/usr/bin/env python3

"""Legacy adapter for load_test"""

from pathlib import Path
import sys

# HACK: Load llm_load_test from ./src
src_dir = Path(__file__).parent / 'src'
sys.path.insert(1, src_dir.as_posix())

from llm_load_test.load_test import main

if __name__ == "__main__":
    main()
