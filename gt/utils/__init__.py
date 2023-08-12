"""
 Utilities
 github.com/TrevisanGMW - 2020-09-13
"""
import sys
import os

# Paths to Append
source_dir = os.path.dirname(__file__)
package_dir = os.path.dirname(source_dir)
parent_dir = os.path.dirname(package_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
