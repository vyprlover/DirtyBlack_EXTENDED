from userbot import CMD_HELP
from userbot.events import register

from telethon import events
import asyncio
from collections import deque
@register(outgoing=True,pattern="^.weather(?: |$)(.*)")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		CMD_HELP.update({ "earth":
			"earth emoji"})
