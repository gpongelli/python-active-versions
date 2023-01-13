=====
Usage
=====

To use python_active_versions in a project:

  .. code-block:: python
    :linenos:

    from python_active_versions.python_active_versions import get_active_python_versions
    _only_python_dict = get_active_python_versions()
    _dict_with_docker = get_active_python_versions(docker_images=True)
    _dict_printing_debug_logs =  get_active_python_versions(log_level='DEBUG')

