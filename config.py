config.load_autoconfig()

import os
exec(open(os.path.expanduser("~/.config/qutebrowser/theme-config.py")).read())

c.auto_save.session=True
c.colors.webpage.darkmode.enabled=True
c.colors.webpage.preferred_color_scheme="dark"
#c.qt.workarounds.disable_accelerated_2d_canvas='never'
c.tabs.last_close='close'
c.tabs.indicator.width=0

config.set('content.user_stylesheets', 'greasemonkey/transparent-bg.user.css')

config.unbind('K')
config.unbind('<Ctrl+PgUp>')
config.unbind('J')
config.unbind('<Ctrl+PgDown>')
config.unbind('<Ctrl+d>')

config.bind('J', 'tab-prev')
config.bind('<Ctrl+PgDown>', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('<Ctrl+PgUp>', 'tab-next')

config.bind('<Ctrl-d>', 'tab-clone')  # Example: Ctrl+d duplicates tab

"""
c.qt.args = [
    'enable-features=CanvasOopRasterization,UseSkiaRenderer,VaapiVideoDecoder,VaapiVideoEncoder,WebRTCPipeWireCapturer,UseOzonePlatform,WaylandWindowDecorations',
    'enable-gpu-rasterization',
    'enable-zero-copy',
    'enable-accelerated-video',
    'enable-vulkan',
    'ignore-gpu-blocklist',
    'enable-native-gpu-memory-buffers',
    'disable-software-rasterizer',
    'enable-accelerated-2d-canvas'
]
"""
c.qt.args = [
    'enable-features=VaapiVideoDecoder,VaapiVideoEncoder'
    'enable-native-gpu-memory-buffers'
]
