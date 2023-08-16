Usage
=====

Recipes
-------

To retrieve a list of ingredients,
you can use the ``primer.get_random_ingredients()`` function:

.. autofunction:: primer.get_random_ingredients

The ``kind`` parameter should be either ``"cook"``, ``"craft"``,
or ``"consume"``. Otherwise, :py:func:`primer.get_random_ingredients`
will raise an exception.

.. autoexception:: primer.InvalidKindError

