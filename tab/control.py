import os
from tab.refresh import create_refresh_button

import onegai.services

def get_status():
    st = []
    for app_name in os.listdir('apps'):
        st.append(onegai.services.get_status(app_name))
    return "\n".join(st)

def get_installed():
    return os.listdir('apps')

def start(app_name):
    result = onegai.services.start(app_name, False)
    return result, get_status()

def stop(app_name):
    result = onegai.services.stop(app_name)
    return result, get_status()

def restart(app_name):
    result = onegai.services.start(app_name, True)
    return result, get_status()

def gr_tab(gr):
    with gr.Tab('control'):
        info = gr.Textbox(label='', interactive=False)
        status = gr.Textbox(value=get_status(), label='server status', interactive=False)
        installed = gr.Dropdown(choices=get_installed(), label='installed')
        with gr.Row():
            start_button = gr.Button(value='start')
            stop_button = gr.Button(value='stop')
            restart_button = gr.Button(value='restart')

    start_button.click(
        fn=start,
        inputs=[installed],
        outputs=[info, status],
    )

    stop_button.click(
        fn=stop,
        inputs=[installed],
        outputs=[info, status],
    )

    restart_button.click(
        fn=restart,
        inputs=[installed],
        outputs=[info, status],
    )
