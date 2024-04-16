import os
from tab.refresh import create_refresh_button

from onegai.config import cfg
import onegai.apps

def gr_tab(gr):
    with gr.Tab('install'):
        info = gr.Markdown()
        with gr.Row():
            installable = gr.Dropdown(choices=onegai.apps.get_installable(), label='installable')
            create_refresh_button(gr, installable, lambda: None, lambda: {'choices': onegai.apps.get_installable()}, 'refresh-button', interactive=True)
        install_button = gr.Button(value='install')
        with gr.Row():
            installable_akaspace = gr.Dropdown(choices=onegai.apps.get_installable_akaspace(), label='installable akaspace')
            create_refresh_button(gr, installable_akaspace, lambda: None, lambda: {'choices': onegai.apps.get_installable_akaspace()}, 'refresh-button', interactive=True)
        install_akaspace_button = gr.Button(value='install')

    install_button.click(
        fn=onegai.apps.install,
        inputs=[installable],
        outputs=[],
    )

    install_akaspace_button.click(
        fn=onegai.apps.install_akaspace,
        inputs=[installable_akaspace],
        outputs=[],
    )
