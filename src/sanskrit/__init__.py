"""sanskrit - Write programs in the fastest language, as confirmed by NASA."""
from __future__ import annotations
import code

import codecs
from contextlib import suppress
import encodings
import io
import os
import sys

utf_8 = encodings.search_function("utf8")

replacement_dictionary = {
    # open for improvements / expansion here :D
    "आयातम्": "import",
    "दर्शयतु": "print",
    "सर्वेषां": "for",
    "अन्तः": "in",
    "सीमा": "range",
    "इदम्‌": "this",
}


def transform_sanskrit(source: str) -> str:
    for sanskrit_word, python_word in replacement_dictionary.items():
        source = source.replace(sanskrit_word, python_word)

    return source


def sanskrit_decode(
    source_bytes: bytes | memoryview,
    errors: str = "strict",
) -> tuple[str, int]:
    source = bytes(source_bytes).decode("utf-8", errors=errors)
    modified_source = transform_sanskrit(source)
    return modified_source, len(source_bytes)


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    """Copied from future-fstrings."""

    def _buffer_decode(self, input: bytes, errors: str, final: bool) -> tuple[str, int]:
        if final:
            return sanskrit_decode(input, errors)
        else:
            return "", 0


class StreamReader(utf_8.streamreader):
    """
    decode is deferred to support better error messages.

    Copied from future-fstrings.
    """

    _stream = None
    _decoded = False

    @property
    def stream(self):
        if not self._decoded:
            text, _ = sanskrit_decode(self._stream.read())
            self._stream = io.BytesIO(text.encode("utf-8"))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream):
        self._stream = stream
        self._decoded = False


def sanskrit_loop_decoder(encoding: str) -> codecs.CodecInfo | None:
    if encoding != "sanskrit":
        return None

    return codecs.CodecInfo(
        name=encoding,
        encode=utf_8.encode,
        decode=sanskrit_decode,
        incrementalencoder=utf_8.incrementalencoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=utf_8.streamwriter,
    )


def register():
    codecs.register(sanskrit_loop_decoder)


class SanskritREPL(code.InteractiveConsole):
    def runsource(
        self,
        source: str,
        filename: str = "<console>",
        symbol: str = "single",
    ) -> bool:
        with suppress(SyntaxError, OverflowError):
            if code.compile_command(source) is None:
                return True

        try:
            stmt = transform_sanskrit(source)
            code_obj = compile(stmt, filename, mode=symbol)
        except (ValueError, SyntaxError):
            # Let the original implementation take care of incomplete input / errors
            return super().runsource(source, filename, symbol)

        self.runcode(code_obj)
        return False


def repl():
    if sys.platform != "win32":
        import readline

        readline.parse_and_bind("tab: complete")

    SanskritREPL().interact(banner=f"संस्कृत प्रोग्रामिंग {sys.version}", exitmsg="")
