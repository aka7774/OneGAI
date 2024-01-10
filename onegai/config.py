import os
import json

config_path = './config.json'

cfg = {}
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        cfg = json.load(f)

cfg_default = {
    "loapi": {
        "mata": {
            "chunk_tsv_dir": "mata",
            "char_tsv_path": "char.tsv",
            "scenario_txt_path": "scenario.txt"
        },
        "message": {
            "server": "127.0.0.1:58083",
            "sys_txt_path": "message_sys.txt",
            "inst_txt_path": "message_inst.txt",
            "log_dir": "logs/llm",
            "args": {
                "model_name": "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct",
                "max_new_tokens": 256,
                "temperature": 1.0,
                "top_p": 1.0,
                "repetition_penalty": 1.0
            }
        },
        "topics": {
            "server": "127.0.0.1:58083",
            "sys_txt_path": "topics_sys.txt",
            "inst_txt_path": "topics_inst.txt",
            "log_dir": "logs/llm",
            "args": {
                "model_name": "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct",
                "max_new_tokens": 512,
                "temperature": 0.8,
                "top_p": 0.9,
                "repetition_penalty": 1.2
            }
        },
        "novel": {
            "server": "127.0.0.1:58083",
            "sys_txt_path": "novel_sys.txt",
            "inst_txt_path": "novel_inst.txt",
            "log_dir": "logs/llm",
            "args": {
                "model_name": "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct",
                "max_new_tokens": 1024,
                "temperature": 1.0,
                "top_p": 0.9,
                "repetition_penalty": 1.2
            }
        },
        "rvctts": {
            "server": "127.0.0.1:58083",
            "cache_dir": "rvctts",
            "ttsdic_tsv_path": "ttsdic.txt",
            "args": {
                "model_name": "",
                "f0_key_up": 0
            }
        },
        "vitstts": {
            "cache_dir": "/mnt/c/CurrenTTC/logs/vitstts",
            "ttsdic_tsv_path": "/mnt/c/CurrenTTC/text/ttsdic.tsv",
            "args": {}
        },
        "llamasrv": {
            "args": {}
        },
        "perf": {
        },
        "sdimage": {
            "server": "127.0.0.1:58083",
            "args": {
                "prompt": "masterpiece, best quality, 1girl",
                "width": 1024,
                "height": 1024,
                "steps": 20,
                "sampler_name": "Euler"
            },
            "image_webp_path": "image.webp",
            "output_dir": "sdimage"
        }
    },
    "openai_key": "",
    "username": "username",
    "password": "password",
    "stop_children": 0,
    "disable_docs": 0,
    "_": ""
}

for k, v in cfg_default.items():
    cfg.setdefault(k, v)

del cfg['_']
cfg['_'] = ''

with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(cfg, f, indent=4)

