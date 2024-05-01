# SPDX-FileCopyrightText: 2024 Gabriele Pongelli
#
# SPDX-License-Identifier: MIT

import nox
import sys
from datetime import datetime
from pathlib import Path
from python_active_versions.python_active_versions import get_active_python_versions
from python_active_versions import __version__
from typing import List


def dev_commands(session):
    session.run("poetry", "run", "python", "--version", external=True)
    session.run("python", "--version", external=True)
    session.run("poetry", "lock", "--no-update", external=True)
    session.run("poetry", "install", "-v", "--with", "devel", "--no-root", "--sync", external=True)
    session.run("poetry", "run", "nox", "--version", external=True)
    session.run("poetry", "run", "pip", "--version", external=True)
    session.run("poetry", "run", "pip", "list", "--format=freeze", external=True)


@nox.session(name='format')
def format_code(session):
    """Format the code"""
    dev_commands(session)
    session.run("poetry", "run", "isort", "python_active_versions", "tests",
                external=True)
    session.run("poetry", "run", "black", "python_active_versions", "tests",
                external=True)


@nox.session
def update_license(session):
    """License files according to REUSE 3.0"""
    dev_commands(session)
    _year = str(datetime.now().year)

    # python files
    _py = list(Path().glob('./python_active_versions/*.py'))
    _py = list(Path().glob('./*.py'))
    _py.extend(list(Path().glob('./tests/*.py')))
    _py.extend(list(Path().glob('./docs/*.py')))
    _absolute = list(map(lambda x: x.absolute(), _py))
    if _absolute:
        session.run("poetry", "run", "reuse", "annotate", "--license=MIT", "--copyright=Gabriele Pongelli",
                    f"--year={_year}", "--merge-copyrights", *_absolute,
                    external=True)

    # json dotted license
    _dot = list(Path().glob('./python_active_versions/*.json'))
    _dot.extend(list(Path().glob('./tests/*.json')))
    _dot.extend(list(Path().glob('./docs/*.json')))
    if _dot:
        session.run("poetry", "run", "reuse", "annotate", "--license=MIT", "--copyright=Gabriele Pongelli",
                    f"--year={_year}", "--merge-copyrights", "--force-dot-license", *_dot,
                    external=True)

    # yaml - md
    _yaml = list(Path().glob('./github/*.yml'))
    _yaml.extend(list(Path().glob('./github/*.md')))
    _yaml.extend(list(Path().glob('./docs/Makefile')))
    _yaml.extend(list(Path().glob('./docs/make.bat')))
    _yaml.extend(list(Path().glob('./pyproject.toml')))
    if _yaml:
        session.run("poetry", "run", "reuse", "annotate", "--license=MIT", "--copyright=Gabriele Pongelli",
                    f"--year={_year}", "--merge-copyrights", *_yaml,
                    external=True)

    # dot-files
    _dot_files = list(Path().glob('./.editorconfig'))
    _dot_files.extend(list(Path().glob('./.gitignore')))
    _dot_files.extend(list(Path().glob('./.yamllint')))
    _dot_files.extend(list(Path().glob('./.pre-commit-config.yaml')))
    if _dot_files:
        session.run("poetry", "run", "reuse", "annotate", "--license=MIT", "--copyright=Gabriele Pongelli",
                    f"--year={_year}", "--merge-copyrights", "--style", "python", *_dot_files,
                    external=True)

    # various files
    _various = list(Path().glob('./*.rst'))
    _various.extend(list(Path().glob('./*.md')))
    _various.extend(list(Path().glob('./*.lock')))
    _various.extend(list(Path().glob('./*.cfg')))
    if _various:
        session.run("poetry", "run", "reuse", "annotate", "--license=MIT", "--copyright=Gabriele Pongelli",
                    f"--year={_year}", "--merge-copyrights", "--force-dot-license", *_various,
                    external=True)

    # download license
    session.run("poetry", "run", "reuse", "download", "--all")

    # fix license file
    with Path(Path.cwd() / 'LICENSES/MIT.txt') as f:
        _text = f.read_text()
        _text.replace('2023 Gabriele Pongelli', f'2023 - {_year} Gabriele Pongelli').replace('<year>', '2023').replace('<copyright holders>', 'Gabriele Pongelli')
        f.write_text(_text)


@nox.session
def lint(session):
    """Lint the code"""
    dev_commands(session)

    session.run("poetry", "build", external=True)
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "flake8", "python_active_versions", "tests", external=True)
    session.run("poetry", "run", "mypy", "--install-types", "python_active_versions", "tests", external=True)
    session.run("poetry", "run", "yamllint", "-f", "colored", "python_active_versions", external=True)
    session.run("poetry", "run", "codespell", "python_active_versions", "docs/source", external=True)
    session.run("poetry", "run", "pylint", "python_active_versions", external=True)
    session.run("poetry", "run", "darglint", "-v", "2", "python_active_versions", external=True)
    session.run("poetry", "run", "bandit", "-r", "python_active_versions", external=True)
    session.run("poetry", "run", "ruff", "python_active_versions", external=True)
    session.run("poetry", "run", "reuse", "lint", external=True)
    # session.run("poetry", "run", "python-active-versions", external=True)
    session.run("poetry", "run", "check-python-versions", ".", external=True, success_codes=[0, 1])


@nox.session
def build(session):
    """Build package"""
    dev_commands(session)
    session.run("poetry", "build", external=True)
    session.run("poetry", "run", "twine", "check", "dist/*", external=True)


@nox.session
def docs(session):
    """Build docs"""
    dev_commands(session)

    session.run("poetry", "run", "sphinx-build", "-b", "html", "docs/source/", "docs/build/html",
                env={'PY_PKG_YEAR': str(datetime.now().year)}, external=True)


def _get_active_version(_active_versions: List[dict]) -> List[str]:
    return [_av['version'] for _av in _active_versions]


@nox.session(python=_get_active_version(get_active_python_versions()))
def test(session):
    """Run tests."""
    _plat = sys.platform

    # print(f"py: {session.python} - plat: {_plat}")

    if _plat == 'win32':
        _pyth = 'python'
    else:
        _pyth = f"python{session.python}"

    session.env['COVERAGE_FILE'] = f'.coverage_{session.name}'
    session.env['PYTHONWARNINGS'] = 'ignore'

    session.run("poetry", "env", "use", _pyth, external=True)

    dev_commands(session)

    session.run("poetry", "build", external=True)
    session.run("poetry", "run", "twine", "check", "dist/*", external=True)
    session.run("poetry", "install", external=True)

    if session.posargs:
        # explicitly pass test file to nox -> nox -- test.py
        test_files = session.posargs
    else:
        # call nox without arguments
        test_files = list(Path().glob('./tests/*.py'))

    session.run('poetry', 'run', 'pytest', *test_files, f"--cov-report=html:html_coverage_{session.name}",
                f"--cov-report=xml:xml_coverage_{session.name}.xml", external=True)


@nox.session
def release(session):
    """Run release task"""
    dev_commands(session)

    session.run("poetry", "run", "cz", "-nr", "3", "bump", "--changelog", "--yes", external=True)
    session.run("poetry", "build", external=True)
    # session.run("poetry", "run", "PyInstaller", "python_active_versions.spec", external=True)
    # session.run("poetry", "publish", "-r", "...", external=True)


@nox.session(name='container')
def container_build(session):
    session.run("poetry", "build", external=True)
    session.run("podman", "build", "-t", f"python-active-version-{__version__}",
                f"--build-arg=PKG_VERSION={__version__}", ".", external=True)
