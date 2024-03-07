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
        with gr.Row():
            installed = gr.Dropdown(choices=get_installed(), label='installed')
            create_refresh_button(gr, installed, lambda: None, lambda: {'choices': get_installed()}, 'refresh-button', interactive=True)
        uninstall_button = gr.Button(value='REMOVE DIRECTORY')

    uninstall_button.click(
        fn=uninstall,
        inputs=[installed],
        outputs=[info],
    )
