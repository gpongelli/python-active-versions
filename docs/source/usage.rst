=====
Usage
=====

To use python_active_versions in a python project:

  .. code-block:: python
    :linenos:

    from python_active_versions.python_active_versions import get_active_python_versions
    _only_python_dict = get_active_python_versions()
    _dict_with_docker = get_active_python_versions(docker_images=True)
    _dict_printing_debug_logs =  get_active_python_versions(log_level='DEBUG')

This library can be used in combination with nox, to run sessions on current active python versions:

  .. code-block:: python
    :linenos:

    from python_active_versions.python_active_versions import get_active_python_versions
    from typing import List

    def _get_active_version(_active_versions: List[dict]) -> List[str]:
        return [_av['version'] for _av in _active_versions]

    @nox.session(python=_get_active_version(get_active_python_versions()))
    def test_something(session):
        ...


Otherwise it's possible to call it directly as CLI:

  .. code-block:: bash
    :linenos:

    $ python-active-versions --help
    $ python-active-versions -m -l WARNING


Or it can be used also from its docker image:

  .. code-block:: bash
    :linenos:

    $ docker run --rm -it gpongelli/python-active-versions:1.10.0 --help
