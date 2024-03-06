import os
import json
import gradio as gr

import tab.control
import tab.install
import tab.uninstall

with gr.Blocks() as demo:
    title = gr.Markdown('# OneGAI')
    tab.control.gr_tab(gr)
    tab.install.gr_tab(gr)
    tab.uninstall.gr_tab(gr)

if __name__ == '__main__':
    demo.launch()
