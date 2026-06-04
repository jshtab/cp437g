 CP437 Graphics Codec
======================

Python text codec for Code Page 437 memory-mapped graphics data, which
replaces the control codes with icons and symbol glyphs. Works as a drop-in
replacement for the builtin 'cp437' codec.

Includes a subset of CP437 used in the Minecraft Classic network protocol.

> [!IMPORTANT]
> This work is not affiliated with Microsoft Corporation, Mojang AB, Minecraft,
> ClassiCube, International Business Machines Corporation, or Unicode, Inc.

 Included Codecs
-----------------

 |   Codec   |         Aliases           |          Description           |
 |-----------|---------------------------|--------------------------------|
 | cp437g    | 437g, ibm437g, classicube | All 255 code points            |
 | minecraft |                           | Only the first 127 code points |

 Installation
--------------

To install from the Python Package Index:

    $ python3 -m pip install cp437g

To install from this repository, use the PyPI build module:

    $ python3 -m pip install build
    $ python3 -m build
    $ python3 -m pip install dist/*.whl

 Examples
----------

To encode a string:

    >>> import cp437g
    >>> "••••".encode('cp437g')
    b'\x07\x07\x07\x07'

To decode a string:

    >>> import cp437g
    >>> b'\x0D\x20\x4C\x61\x20\x4C\x61\x20\x0D'.decode('cp437g')
    '♪ La La ♪'    
