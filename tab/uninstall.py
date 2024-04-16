import os
from tab.refresh import create_refresh_button

import onegai.apps

def gr_tab(gr):
    with gr.Tab('uninstall'):
        info = gr.Markdown()
        with gr.Row():
            installed = gr.Dropdown(choices=onegai.apps.get_installed(), label='installed')
            create_refresh_button(gr, installed, lambda: None, lambda: {'choices': onegai.apps.get_installed()}, 'refresh-button', interactive=True)
        uninstall_button = gr.Button(value='REMOVE DIRECTORY')

    uninstall_button.click(
        fn=onegai.apps.uninstall,
        inputs=[installed],
        outputs=[],
    )
