## 1.19.0 (2024-07-25)

### Feat

- convert data to json before joining

## 1.18.0 (2024-07-15)

### Feat

- add dive tool
- trivy on github action
- trivy on local run
- trivy config file and cache folder

### Fix

- github permission and action
- load docker build to docker images
- pass package version from pyproject
- github action sha and join authors

## 1.17.2 (2024-07-11)

### Fix

- poetry lock on github action to avoid error

## 1.17.1 (2024-07-11)

### Fix

- poetry lock

## 1.17.0 (2024-07-11)

### Feat

- hadolint and docker parameter in github actions

### Fix

- remove interactive for CI/CD
- poetry lock

## 1.16.1 (2024-07-10)

### Fix

- poetry lock

## 1.16.0 (2024-07-10)

### Feat

- hadolint rules to match variable labels
- container labels, fixed versions, remove unneeded packages
- gather data and pass to podman label
- hadolint tool into nox session with config

### Fix

- container execution docs

## 1.15.0 (2024-06-26)

### Feat

- reuse for cache's sqlite file
- use cache for requests call

### Fix

- tests
- lint errors
- avoid clas between python and docker base OS version
- search into subfolders for reuse tool

## 1.14.1 (2024-05-01)

### Fix

- remove unused import

## 1.14.0 (2024-05-01)

### Feat

- align __init__.py with pyproject.toml during dev and not in built package
- remove pyproject needs in built package

### Fix

- run isort and black
- call same commands in CI/CD
- use rtoml that does not need gcc and g++
- docker image tag for local build

## 1.13.2 (2024-05-01)

### Fix

- docker image link

## 1.13.1 (2024-05-01)

### Fix

- github pages write permission

## 1.13.0 (2024-05-01)

### Feat

- using github trusted publisher

### Fix

- github action upload pages

## 1.12.1 (2024-05-01)

### Fix

- github actions upgrade

## 1.12.0 (2024-05-01)

### Feat

- license update
- new workflow to test container build
- pass tag as PKG_VERSION to docker image
- new nox session to build container

### Fix

- missing package to build pytomlpp into container

## 1.11.0 (2024-04-30)

### Feat

- use pytomlpp that's supported in python<3.11
- remove python 3.7, older version supports it
- remove tox in favor of nox

### Fix

- nox github command
- ensure pip for py3.12 and update actions
- python3.12 fixing call
- revert change to avoid stream closed

## 1.10.0 (2024-04-24)

### Feat

- new codecov action with secret token
- dockerfile and github actions
- add ruff linter
- skip main branch, redirect stdout to /dev/null

### Fix

- remove python3.12
- poetry call
- tox for python 3.12
- literla_eval break code
- lint checks
- alignment and latest python version
- ruff linter errors
- lxml clean splitted package

## 1.9.1 (2024-02-22)

### Fix

- cli description

## 1.9.0 (2024-02-22)

### Feat

- update cloup dependency

### Fix

- github action warning

## 1.8.0 (2023-04-02)

### Feat

- revert to published requests-html or pypi rejects, installing explicitly beautifulsoup4

## 1.7.0 (2023-04-02)

### Feat

- use requests-html as develop for pypi upload

## 1.6.0 (2023-04-01)

### Feat

- use requests-html project that does not use bs4 package but beautifulsoup4

## 1.5.0 (2023-02-03)

### Feat

- support since python3.7

### Fix

- set different dependencies for python3.7

## 1.4.0 (2023-02-03)

### Feat

- adding tests
- adding CLI tool
- adding cloup and cli call

## 1.3.0 (2023-01-30)

### Feat

- type hint on methods

## 1.2.1 (2023-01-30)

### Fix

- include py.typed files for mypy execution

## 1.2.0 (2023-01-29)

### Feat

- add multithreading

### Fix

- updated classifier

## 1.1.1 (2023-01-26)

### Fix

- readme

## 1.1.0 (2023-01-14)

### Feat

- python3.8
- info log messages

## 1.0.0 (2023-01-14)

### Feat

- fix lint stage
- reorder tox stages
- contributing docs
- license files

### Fix

- testpypi needs different username
- python 3.9 as minimum version
- remove template code
- remove unused tests
- added typed and files under doc folder
