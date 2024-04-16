import os
from tab.refresh import create_refresh_button

from onegai.config import cfg
import onegai.apps

def get_installable():
    installable = []
    for sh in os.listdir('install'):
        if sh == 'old':
            continue
        if sh == 'akaspace.sh':
            continue

        installable.append(os.path.splitext(sh)[0])
        
    return installable

def get_installable_akaspace():
    akaspaces = []
    for app_name in cfg['apps'].keys():
        if 'is_akaspace' in cfg['apps'][app_name] and cfg['apps'][app_name]['is_akaspace']:
            akaspaces.append(app_name)
    return akaspaces

def install(app_name):
    onegai.apps.install(app_name)

def install_akaspace(app_name):
    onegai.apps.install_akaspace(app_name)

def gr_tab(gr):
    with gr.Tab('install'):
        info = gr.Markdown()
        with gr.Row():
            installable = gr.Dropdown(choices=get_installable(), label='installable')
            create_refresh_button(gr, installable, lambda: None, lambda: {'choices': get_installable()}, 'refresh-button', interactive=True)
        install_button = gr.Button(value='install')
        with gr.Row():
            installable_akaspace = gr.Dropdown(choices=get_installable_akaspace(), label='installable akaspace')
            create_refresh_button(gr, installable_akaspace, lambda: None, lambda: {'choices': get_installable_akaspace()}, 'refresh-button', interactive=True)
        install_akaspace_button = gr.Button(value='install')

    install_button.click(
        fn=install,
        inputs=[installable],
        outputs=[info],
    )

    install_akaspace_button.click(
        fn=install_akaspace,
        inputs=[installable_akaspace],
        outputs=[info],
    )
