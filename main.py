# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import argparse
import os
import lib.utils as utils

parser = argparse.ArgumentParser(description="Generate a cmake project.")
parser.add_argument("name", type=str, help="project name to generate")
parser.add_argument("directory", type=str, help="where to create project")
parser.add_argument("--fortran", dest="fortran", action="store_true", help="add fortran to enabled languages (overrides default)")
parser.add_argument("--cc", dest="cc", action="store_true", help="add C to enabled languages (overrides default)")
parser.add_argument("--cxx", dest="cxx", action="store_true", help="add C++ to enabled languages (overrides default)")
#parser.add_argument("version", type=str, help="minimum version")
##parser.add_argument("type", type=str, help="target type")
#parser.add_argument("lang", type=str, help="languages")
#parser.add_argument("compiler", type=str, help="compilers to support")
#parser.add_argument("override-fortran-mod", type=str, help="change Fortran mod location")
args = parser.parse_args()

if __name__ == "__main__":
    print(utils.gen_project("rob", args))
    utils.create_dirs(args)
