Change Counter
--------------

In this challenge you need to find all combinations of ``coins`` that add up to
the amount ``money`` change required to be dispended.

The method ``change_count()`` takes on two arguments ``money`` total amount to
of change, and ``coins``, the set of change coins available.

The different the order of ``coins`` combinations to dispend do not matter.

.. code-block:: python

  [1,2,1] == [2,1,1] == [1,1,2] # correspond to the same combination
