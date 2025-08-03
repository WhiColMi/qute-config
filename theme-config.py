





exec(open(os.path.expanduser("~/.config/qutebrowser/theme.py")).read())

c.colors.completion.category.bg = bg_alt
c.colors.completion.category.fg = fg
c.colors.completion.even.bg = bg
c.colors.completion.odd.bg = bg_alt
c.colors.completion.item.selected.bg = accent
c.colors.completion.item.selected.fg = bg
c.colors.completion.item.selected.border.top = border
c.colors.completion.item.selected.border.bottom = border
c.colors.completion.match.fg = yellow
c.colors.completion.scrollbar.bg = bg
c.colors.completion.scrollbar.fg = fg

c.colors.statusbar.normal.bg = bg
c.colors.statusbar.normal.fg = fg
c.colors.statusbar.insert.bg = green
c.colors.statusbar.insert.fg = bg
c.colors.statusbar.passthrough.bg = blue
c.colors.statusbar.passthrough.fg = bg
c.colors.statusbar.private.bg = purple
c.colors.statusbar.private.fg = fg
c.colors.statusbar.command.bg = bg_alt
c.colors.statusbar.command.fg = fg
c.colors.statusbar.url.fg = fg
c.colors.statusbar.url.success.http.fg = green
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = yellow
c.colors.statusbar.url.error.fg = red

c.colors.contextmenu.menu.bg = bg
c.colors.contextmenu.menu.fg = fg
c.colors.contextmenu.selected.bg = accent
c.colors.contextmenu.selected.fg = dark
c.colors.contextmenu.disabled.fg = text_secondary

c.colors.tabs.bar.bg = bg
c.colors.tabs.even.bg = bg
c.colors.tabs.even.fg = text_secondary
c.colors.tabs.odd.bg = bg_alt
c.colors.tabs.odd.fg = text_secondary
c.colors.tabs.selected.even.bg = accent
c.colors.tabs.selected.even.fg = bg
c.colors.tabs.selected.odd.bg = accent
c.colors.tabs.selected.odd.fg = bg

c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = blue
c.colors.downloads.start.fg = bg
c.colors.downloads.stop.bg = green
c.colors.downloads.stop.fg = bg
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = fg

c.colors.messages.error.bg = red
c.colors.messages.error.fg = fg
c.colors.messages.warning.bg = yellow
c.colors.messages.warning.fg = dark
c.colors.messages.info.bg = bg
c.colors.messages.info.fg = fg

c.colors.prompts.bg = bg_alt
c.colors.prompts.fg = fg
c.colors.prompts.border = f'1px solid {border}'

c.colors.hints.bg = yellow
c.colors.hints.fg = dark
c.colors.hints.match.fg = red

c.colors.keyhint.bg = bg
c.colors.keyhint.fg = fg
c.colors.keyhint.suffix.fg = yellow

c.colors.webpage.bg = bg

