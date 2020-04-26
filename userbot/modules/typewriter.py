#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from telethon import events
import asyncio
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.typ(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    # https://t.me/DirtyBlack_EXTENDED
    input_str = event.pattern_match.group(1)
    typing_symbol = "|"
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await event.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        await event.edit(typing_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        await event.edit(previous_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)

        CMD_HELP.update({
"typewriter":
"text writing animation.\
\nUse:- .typ (text)"
})
