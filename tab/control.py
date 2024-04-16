import os
import subprocess
from tab.refresh import create_refresh_button

import onegai.apps

def start(app_name):
    result = onegai.apps.start(app_name, False)
    return result, get_status()

def stop(app_name, kill):
    result = onegai.apps.stop(app_name, kill)
    return result, get_status()

def restart(app_name):
    result = onegai.apps.start(app_name, True)
    return result, get_status()

def gr_tab(gr):
    with gr.Tab('control'):
        with gr.Accordion('status'):
            app_name = gr.Textbox(label='app_name', interactive=False)
            configured = gr.Textbox(label='configured', interactive=False)
            port = gr.Textbox(label='port', interactive=False)
            pid = gr.Textbox(label='pid', interactive=False)
        info = gr.Textbox(label='', interactive=False)
        status = gr.Dataset(components=[app_name, configured, port, pid], samples=onegai.apps.get_status_list(), samples_per_page = -1, label='server status')
        create_refresh_button(gr, status, lambda: None, lambda: {'samples': onegai.apps.get_status_list()}, 'refresh-button', interactive=True)
        lsof_i = gr.Textbox(value=onegai.apps.get_lsof_i(), label='lsof -iTCP | grep LISTEN', interactive=False)
        create_refresh_button(gr, lsof_i, lambda: None, lambda: {'value': onegai.apps.get_lsof_i()}, 'refresh-button', interactive=True)
        with gr.Row():
            installed = gr.Dropdown(choices=onegai.apps.get_installed(), label='installed')
            create_refresh_button(gr, installed, lambda: None, lambda: {'choices': onegai.apps.get_installed()}, 'refresh-button', interactive=True)
        with gr.Row():
            start_button = gr.Button(value='start')
            kill = gr.Checkbox(label='kill')
            stop_button = gr.Button(value='stop')
            restart_button = gr.Button(value='restart')

    start_button.click(
        fn=start,
        inputs=[installed],
        outputs=[info, status],
    )

    stop_button.click(
        fn=stop,
        inputs=[installed, kill],
        outputs=[info, status],
    )

    restart_button.click(
        fn=restart,
        inputs=[installed],
        outputs=[info, status],
    )
