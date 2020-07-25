import asyncpg
from .abstract import AsyncContextManagerABC


class PoolManager(AsyncContextManagerABC):
    """
    An async context manager that mimics the :func:`asyncpg.create_pool`
    function, used with subclasses of :class:`AsyncModel`.

    :param args:  Passed to :func:`asyncpg.create_pool` function.
    :param kwargs: Passed to :func:`asyncpg.create_pool` function.

    """
    __slots__ = ('_args', '_kwargs', '_connection', '_pool')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._connection = None
        self._pool = None

    async def __aenter__(self):
        pass

    async def connect(self):
        pool = await asyncpg.create_pool(*self._args, **self._kwargs)
        return pool

    async def __aexit__(self, exctype, excval, traceback):
        pass
