"""

Available Commands:

.sux

.fuk

.kiss"""


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("fuck"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "fuk":

    await event.edit("fuk")

    animation_chars = ["👉 fuck bolte      ✊️", "👉   fuck  ✊️", "👉  fuck✊️", "👉fuck✊️💦"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


@borg.on(lightning_cmd("sux"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "sux":

    await event.edit("sux")

    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])


""


import asyncio


@borg.on(lightning_cmd("kiss"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 101)

    # input_str = event.pattern_match.group(1)

    # if input_str == "kiss":

    await event.edit("kiss")

    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])
