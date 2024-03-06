import os
from tab.refresh import create_refresh_button

import onegai.apps

def get_installed():
    return os.listdir('apps')

def uninstall(app_name):
    onegai.apps.uninstall(app_name)

def gr_tab(gr):
    with gr.Tab('uninstall'):
        info = gr.Markdown()
        installed = gr.Dropdown(choices=get_installed(), label='installed')
        uninstall_button = gr.Button(value='REMOVE DIRECTORY')

    uninstall_button.click(
        fn=uninstall,
        inputs=[installed],
        outputs=[info],
    )
