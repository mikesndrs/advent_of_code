.. _`installing`:

Installing aoc
=================================

Ubuntu installation
-------------------

* Install system packages

  .. code-block:: bash

    sudo apt update
    sudo apt install build-essential git-all python3-dev python-is-python3 \
      python3 python3-venv python3-pip python3-setuptools

* Setup a project folder and clone git repository

  .. code-block:: bash

    mkdir projects
    cd projects
    git clone git@github.com:mikesndrs/advent_of_code.git
    cd advent_of_code

* Setup a python virtual environment and install python dependencies

  .. code-block:: bash

    python3 -m venv ./venv
    . venv/bin/activate
    pip install --upgrade pip
    pip install --upgrade wheel setuptools
    # For development an installation in editable mode may be more convenient
    pip install .[all]

* Test the installation

  .. code-block:: bash

    python3 -c "import aoc; print(aoc.__version__)"
    pytest

* To build the aoc documentation, execute:

  .. code-block:: bash

    make -C docs html
