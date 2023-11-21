__author__ = 'Alex Rogozhnikov'
__version__ = '0.7.0'


class EinopsError(RuntimeError):
    """ Runtime error thrown by opt_einops """
    pass


__all__ = ['rearrange', 'reduce', 'repeat', 'einsum',
           'pack', 'unpack',
           'parse_shape', 'asnumpy', 'EinopsError']

from .opt_einops import rearrange, reduce, repeat, einsum, parse_shape, asnumpy
from .packing import pack, unpack