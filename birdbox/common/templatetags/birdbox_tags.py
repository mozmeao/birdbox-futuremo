# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Dict, List

from django.template import Library
from django.template.loader import render_to_string

from ..utils import get_frontend_media

register = Library()


@register.simple_tag
def frontend_media_for_page(page_obj) -> Dict[str, List[str]]:
    """Gather the frontend CSS and JS associated with any Protocol-styled
    blocks in the page"""
    css_files = []
    js_files = []

    for media_obj in get_frontend_media(page_obj.specific):
        css_files.extend(set([x for x in media_obj.render_css()]))
        js_files.extend(set([x for x in media_obj.render_js()]))

    return {
        "css": render_to_string(
            "templatetags/css_frontend_media.html",
            {
                "css_files": set(css_files),
            },
        ),
        "js": render_to_string(
            "templatetags/js_frontend_media.html",
            {
                "js_files": set(js_files),
            },
        ),
    }


@register.simple_tag
def get_alt_text_for_accessible_image_block(block_data):
    """Complements common.blocks.AccessibleImageBlock, which
    should be the block_data passed in.

    If the block is for a non-decorative image, we try to use custom
    alt-text, else fall back to the image's title, which is what
    Wagtail also uses by default"""

    retval = ""
    if not block_data.get("decorative_only"):
        retval = block_data.get("alt_text")
        if not retval:
            retval = block_data.get("image").title
    return retval
