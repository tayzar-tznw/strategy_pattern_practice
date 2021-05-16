import os
import re
import sys


def do(path, env):
    __do(path, env)


__module_file_regexp = "(.+)\.py(c?)$"


def __get_module_names_in_dir(path):
    result = set()

    # Looks for all python files in the directory (not recursively) and add their name to result:
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            regexp_result = re.search(__module_file_regexp, entry)
            if regexp_result:  # is a module file name
                result.add(regexp_result.groups()[0])

    return result


def __do(path, env):
    sys.path.append(path)  # adds provided directory to list we can import from
    for module_name in sorted(__get_module_names_in_dir(path)):  # for each found module...
        env[module_name[:1]] = __import__(module_name)  # ... import
