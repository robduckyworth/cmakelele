# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import argparse
import os

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

def enable_languages(args):
    languages = ""
    if args.cc:
        languages += "C"
    if args.cxx:
        if len(languages) > 0:
            languages += " "
        languages += "CXX"
    if args.fortran:
        if len(languages) > 0:
            languages += " "
        languages += "Fortran"
    if len(languages) == 0:
        return "C CXX Fortran"
    else:
        return languages

def gen_version(version):
    pass


def gen_project(name, args):
    lang = enable_languages(args)
    project_str = str("project(%s LANGUAGES %s)" % (name, lang))
    print(project_str)

def create_dirs(args):
    top_level = os.listdir(args.directory)
    if not os.path.exists(args.directory + "/CMakeLists.txt"):
        open(args.directory + "/CMakeLists.txt", "w").close()
    else:
        print("CMakeLists.txt found at root, not creating a new one.")
    for dir in top_level:
        check_src(dir)
    print(top_level)

def check_src(dirname):
    for pattern in ["src", "source", "lib"]:
        if pattern == dirname:
            print(dir)
            print("potential source dir found")

def find_header_files(dir):
    head_ext = [".h", ".hpp", ".mod"]
    found_headers = []
    dir_list = os.listdir(dir)
    for file in dir_list:
        for ext in head_ext:
            if ext in file:
                found_sources.append(file)
    return found_headers

def find_sources(dir):
    extensions = [".cpp", ".f", ".f90", ".F90", ".c", ".py",]
    found_sources = []
    dir_list = os.listdir(dir)
    for file in dir_list:
        for ext in extensions:
            if ext in file:
                found_sources.append(file)
    return found_sources

def add_targets(name, type, source_list):
        if type == "lib":
            target_str = str("add_library(%s %s %s)" % (name, type, source_list))
        else:
            target_str = str("add_executable(%s %s %s)" % (name, type, source_list))

        print(project_str)

def add_subdirs():
    pass

gen_project("rob", args)
create_dirs(args)
