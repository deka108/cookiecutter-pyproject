#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="Generate requirements.txt")
parser.add_argument("--path-to-requirements", type=str, help="Path to requirements.txt under production mode",
                    required=True)
parser.add_argument("--path-to-dev-requirements", type=str, help="Path to requirements.dev.txt under development mode",
                    required=True)
parser.add_argument("--path-to-test-requirements", type=str, help="Path to requirements.test.txt under development mode",
                    required=False)


# Default to jupyter lab / jupyter notebook libraries, which intended to be excluded from deployment pipelines
excluded_packages = {"appnope", "backcall", "bleach", "defusedxml", "entrypoints", "ipykernel", "ipython", "jedi",
                     "jupyter-client", "jupyterlab", "jupyterlab-server", "mistune", "nbconvert", "notebook",
                     "pandocfilters", "parso", "pexpect", "pickleshare", "prometheus-client", "prompt-toolkit",
                     "ptyprocess", "pygments", "pyzmq", "send2trash", "terminado", "testpath", "tornado", "wcwidth",
                     "webencodings"}


def is_pkg_excluded(package):
    pkg_name = package.split("==")[0]
    return any(pkg_name == pkg for pkg in excluded_packages)


if __name__ == "__main__":
    args = parser.parse_args()
    path_to_requirements = args.path_to_requirements
    path_to_dev_requirements = args.path_to_dev_requirements
    path_to_test_requirements = args.path_to_test_requirements or os.path.join(os.path.dirname(path_to_requirements),
                                                                               "requirements.test.txt")

    with open(path_to_requirements, "r") as fp:
        requirements = fp.readlines()

    with open(path_to_dev_requirements, "r") as fp:
        dev_requirements = fp.readlines()

    new_requirements = []
    test_requirements = []

    for req in requirements:
        if not is_pkg_excluded(req):
            test_requirements.append(req)

    for req in dev_requirements:
        if req not in test_requirements and not is_pkg_excluded(req):
            test_requirements.append(req)

    with open(path_to_test_requirements, "w") as fp:
        fp.write("".join(test_requirements))