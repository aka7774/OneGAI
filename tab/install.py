import os
from tab.refresh import create_refresh_button

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
    return [
    'llm',
    'faiss',
    'whisper',
    'reazonspeech',
    'stablediffusion',
    'katanuki',
    'ddg_bs4',
    'pke_ja',
    'pke_en',
    'audiosep',
    'ytdlp',
    ]

def install(app_name):
    onegai.apps.install(app_name)

def install_akaspace(app_name):
    onegai.apps.install_akaspace(app_name)

def gr_tab(gr):
    with gr.Tab('install'):
        info = gr.Markdown()
        installable = gr.Dropdown(choices=get_installable(), label='installable')
        install_button = gr.Button(value='install')
        installable_akaspace = gr.Dropdown(choices=get_installable_akaspace(), label='installable akaspace')
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
