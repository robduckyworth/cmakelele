import os

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
