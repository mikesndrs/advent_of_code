.. _`code style and linting`:

Code style and linting
======================


Code style
----------

aoc follows `The Black Code Style
<https://black.readthedocs.io/en/stable/the_black_code_style/index.html>`_. All Python
files should be formatted with the ``black`` command line tool (this is checked in
:ref:`CI <ci configuration>`).


Why Black?
''''''''''

We use the black autoformatter, so the code style is uniform across all Python files,
regardless of the developer that created the code 🙂.

This improves efficiency of developers working on the project:

-   Uniform code style makes it easier to read, review and understand other's code.
-   Autoformatting code means that developers can save time and mental energy for the
    important matters.

More reasons for using black can be found on `their website
<https://black.readthedocs.io/en/stable/index.html>`_.


Using Black
'''''''''''

The easiest way to work with Black is by using an integration with your editor. See
https://black.readthedocs.io/en/stable/integrations/editors.html.

You can also ``pip install black`` and run it every time before committing (manually or
with pre-commit hooks):

.. code-block:: console

    $ black aoc
    All done! ✨ 🍰 ✨
    66 files left unchanged.


Linting
-------

aoc uses `flake8 <https://flake8.pycqa.org/en/latest/>`_ for linting (static code
analysis). Flake8 should not report any violations when running it on the ``aoc``
code base. Again, this is checked in CI.

In some exceptions we can ignore a violation. For example, if a violation cannot be
avoided, or fixing it would result in less readable code. This should be avoided as much
as possible though.


Why linting?
''''''''''''

Because it results in more readable code and can prevent some types of bugs!


Using flake8
''''''''''''

Again, the easiest way to work with the ``flake8`` linter is by using an integration
with your editor.

You can also ``pip install flake8`` and run it every time before comitting to check if
your code introduces any violations:

.. code-block:: console

    $ flake8 aoc


Type checking
-------------
aoc uses typing hinting which is checked at compile time using `mypy 
<https://www.mypy-lang.org/>`_. This tool can spot typing bugs and makes
for easier code maintenance and debugging.

Using mypy
''''''''''

.. code-block:: console

    $ mypy aoc
    Success: no issues found in 66 source files

Import sorting
--------------
aoc uses `isort <https://pycqa.github.io/isort/>`_ for automatic import sorting separated by type.

Using isort
'''''''''''

.. code-block:: console

    $ isort aoc

Docstring style
---------------
While not enforced, we recommend using `napoleon style docstrings <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_
