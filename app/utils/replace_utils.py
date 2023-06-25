from typing import Union, Dict
import re


codecs = ["utf8", "cp1252"]


def custom_replace(to_replace: Union[str, bytes], strings_to_replace: Dict):
    codec_for_encode = None
    decoding_attempt = False

    if not isinstance(to_replace, str):
        decoding_attempt = True
        for codec in codecs:
            try:
                to_replace = to_replace.decode(codec)
                codec_for_encode = codec
                decoding_attempt = True
                break
            except UnicodeDecodeError:
                pass

    # Если нет подходящего кодека и входной элемент не строка, то просто вернем обратно
    if not codec_for_encode and decoding_attempt:
        return to_replace

    for old, new in strings_to_replace.items():
        pattern = re.compile(" .*".join(old.split(" ")), re.IGNORECASE)
        to_replace = pattern.sub(new, to_replace)

    return to_replace.encode(codec_for_encode) if codec_for_encode else to_replace
