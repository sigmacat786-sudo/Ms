"""
decoding.py
─────────────────────────────────────────────────────────────────────────────
Helper for the "learnxpw" proxy URL shape (MS2), where the real video URL is
passed percent-encoded inside a "url=" query param, e.g.:

    https://www.learnxpw.site/api/play?url=https%3A%2F%2Fd1d34p8vz63oiq
    .cloudfront.net%2F....%2Fdash%2F480%2F4.mp4%3FSignature%3D...

decode_ms2_url() strips the fixed "https://www.learnxpw.site/api/play?url="
prefix (if present) and percent-decodes the remainder, returning the real
underlying (normal, non-encoded) video URL, ready to be passed on to the
existing .mpd / .mp4 -> .m3u8 conversion logic.
"""

from urllib.parse import unquote

MS2_PREFIX = "https://www.learnxpw.site/api/play?url="


def decode_ms2_url(url: str) -> str:
    """
    Given a full learnxpw proxy URL, strip the fixed prefix (if present) and
    percent-decode the remaining "url=" value to get back the real, normal
    (decoded) video URL.
    """
    if url.lower().startswith(MS2_PREFIX.lower()):
        encoded_part = url[len(MS2_PREFIX):]
    else:
        encoded_part = url
    return unquote(encoded_part)
