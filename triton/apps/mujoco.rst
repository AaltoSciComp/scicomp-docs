Mujoco
======

:supportlevel: A
:pagelastupdated:
:maintainer:

.. highlight:: bash

`Mujoco <https://mujoco.org/>`_ is an advanced physics engine owned and
maintained by DeepMind.

Installing Mujoco
-----------------

Prior to version 2.1.2 Mujoco was provided via the module system. However,
Since version 2.1.2, Mujoco can be
`installed via pip <https://mujoco.readthedocs.io/en/latest/python.html#installation>`_.

This means that you can install Mujoco into a global path, virtual environment
or a conda environment. For information on environment creation, you should
check instructions in our :doc:`Python page <python>`. Here we create a new
minimal :ref:`conda environment <_conda>`.

.. code-block:: shell

  module load miniconda

  conda create --name mujoco --channel conda-forge python pip

  source activate mujoco

  pip install mujoco

Using Mujoco with ``dm_control``
--------------------------------

`dm_control <https://github.com/deepmind/dm_control>`_ is DeepMind's software
stack for physics-based simulation and reinforcement learning environments.
It uses Mujoco for physics simulations.

Installing ``dm_control``
~~~~~~~~~~~~~~~~~~~~~~~~~

``dm_control`` is available via pip. Installation is similar as with Mujoco.

.. code-block:: shell

  module load miniconda

  conda create --name dm_control --channel conda-forge "python<3.10" pip

  source activate dm_control

  pip install dm_control

.. warning::

  At the time of writing (6.4.2022) the version of ``dm_control`` for Python
  3.10 is an older version that does not utilize new ``mujoco``-package. Thus
  in the environment creation command we specify a limit to Python version.

Testing installed ``dm_control``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run
`an example <https://github.com/deepmind/dm_control/blob/master/dm_control/mujoco/README.md>`_
from ``dm_control``'s repository:

.. code-block:: python

  from dm_control import mujoco

  # Load a model from an MJCF XML string.
  xml_string = """
  <mujoco>
    <worldbody>
      <light name="top" pos="0 0 1.5"/>
      <geom name="floor" type="plane" size="1 1 .1"/>
      <body name="box" pos="0 0 .3">
        <joint name="up_down" type="slide" axis="0 0 1"/>
        <geom name="box" type="box" size=".2 .2 .2" rgba="1 0 0 1"/>
        <geom name="sphere" pos=".2 .2 .2" size=".1" rgba="0 1 0 1"/>
      </body>
    </worldbody>
  </mujoco>
  """
  physics = mujoco.Physics.from_xml_string(xml_string)

  # Render the default camera view as a numpy array of pixels.
  pixels = physics.render()

  # Reset the simulation, move the slide joint upwards and recompute derived
  # quantities (e.g. the positions of the body and geoms).
  with physics.reset_context():
    physics.named.data.qpos['up_down'] = 0.5

  # Print the positions of the geoms.
  print(physics.named.data.geom_xpos)
  # FieldIndexer(geom_xpos):
  #            x         y         z
  # 0  floor [ 0         0         0       ]
  # 1    box [ 0         0         0.8     ]
  # 2 sphere [ 0.2       0.2       1       ]

  # Advance the simulation for 1 second.
  while physics.time() < 1.:
    physics.step()

  # Print the new z-positions of the 'box' and 'sphere' geoms.
  print(physics.named.data.geom_xpos[['box', 'sphere'], 'z'])
  # [ 0.19996362  0.39996362]
