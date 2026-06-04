import io
import unittest

MINECRAFT_CODECS = ['minecraft']
MINECRAFT_ENCODED = bytes(range(0,128))
MINECRAFT_DECODED = (
    '\x00☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&\'()*+,-./0123456789:;<=>?@'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂'
)

CP437_CODECS = ['cp437g', 'ibm437g', '437g', 'classicube']
CP437_ENCODED = bytes(range(0,256))
CP437_DECODED = MINECRAFT_DECODED + (
    'ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─'
    '┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■\xa0'
)

def zip_codecs():
    for codec in MINECRAFT_CODECS:
        yield codec, MINECRAFT_ENCODED, MINECRAFT_DECODED
    for codec in CP437_CODECS:
        yield codec, CP437_ENCODED, CP437_DECODED

def zip_codec_characters():
    for codec in MINECRAFT_CODECS:
        for encoded, decoded in zip(MINECRAFT_ENCODED, MINECRAFT_DECODED):
            yield codec, encoded, decoded
    for codec in CP437_CODECS:
        for encoded, decoded in zip(CP437_ENCODED, CP437_DECODED):
            yield codec, encoded, decoded

def setUpModule():
    import cp437g

class BytesTest(unittest.TestCase):
    def test_solo_encode(self):
        for codec, expected, unicode_char in zip_codec_characters():
            with self.subTest(codec=codec, unicode_char=unicode_char, expected=expected):
                self.assertEqual(unicode_char.encode(codec)[0], expected)

    def test_block_encode(self):
        for codec, encoded, decoded in zip_codecs():
            with self.subTest(codec=codec):
                self.assertEqual(decoded.encode(codec), encoded)

    def test_solo_decode(self):
        for codec, code_point, expected in zip_codec_characters():
            with self.subTest(codec=codec, code_point=code_point, expected=expected):
                self.assertEqual(bytes((code_point,)).decode(codec), expected)

    def test_block_decode(self):
        for codec, encoded, decoded in zip_codecs():
            with self.subTest(codec=codec):
                self.assertEqual(encoded.decode(codec), decoded)


class StreamsTest(unittest.TestCase):
    def test_stream_decode(self):
        for codec, encoded, decoded in zip_codecs():
            with self.subTest(codec=codec):
                encoded_stream = io.BytesIO(encoded)
                decoded_stream = io.TextIOWrapper(encoded_stream, encoding=codec)
                self.assertEqual(decoded_stream.read(), decoded)

    def test_stream_encode(self):
        for codec, encoded, decoded in zip_codecs():
            with self.subTest(codec=codec):
                encoded_stream = io.BytesIO()
                decoded_stream = io.TextIOWrapper(encoded_stream, codec)
                decoded_stream.write(decoded)
                decoded_stream.flush()
                self.assertEqual(encoded_stream.getvalue(), encoded)
