import os
import subprocess
from tab.refresh import create_refresh_button

import onegai.apps

def get_status():
    st = []
    for app_name in os.listdir('apps'):
        st.append(onegai.apps.get_status(app_name))
    return "\n".join(st)

def get_lsof_i():
    cmd = 'lsof -iTCP | grep LISTEN'
    result = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return result.stdout

def get_installed():
    return os.listdir('apps')

def start(app_name):
    result = onegai.apps.start(app_name, False)
    return result, get_status(), get_lsof_i()

def stop(app_name):
    result = onegai.apps.stop(app_name)
    return result, get_status(), get_lsof_i()

def restart(app_name):
    result = onegai.apps.start(app_name, True)
    return result, get_status(), get_lsof_i()

def gr_tab(gr):
    with gr.Tab('control'):
        info = gr.Textbox(label='', interactive=False)
        status = gr.Textbox(value=get_status(), label='server status', interactive=False)
        create_refresh_button(gr, status, lambda: None, lambda: {'value': get_status()}, 'refresh-button', interactive=True)
        lsof_i = gr.Textbox(value=get_lsof_i(), label='lsof -iTCP | grep LISTEN', interactive=False)
        create_refresh_button(gr, lsof_i, lambda: None, lambda: {'value': get_lsof_i()}, 'refresh-button', interactive=True)
        with gr.Row():
            installed = gr.Dropdown(choices=get_installed(), label='installed')
            create_refresh_button(gr, installed, lambda: None, lambda: {'choices': get_installed()}, 'refresh-button', interactive=True)
        with gr.Row():
            start_button = gr.Button(value='start')
            stop_button = gr.Button(value='stop')
            restart_button = gr.Button(value='restart')

    start_button.click(
        fn=start,
        inputs=[installed],
        outputs=[info, status, lsof_i],
    )

    stop_button.click(
        fn=stop,
        inputs=[installed],
        outputs=[info, status, lsof_i],
    )

    restart_button.click(
        fn=restart,
        inputs=[installed],
        outputs=[info, status, lsof_i],
    )
