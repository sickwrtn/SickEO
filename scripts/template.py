import modules.scripts as scripts
import gradio as gr
import os

from modules import images, script_callbacks
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
import torch
from PIL import Image

class ExtensionTemplateScript(scripts.Script):
        # Extension title in menu UI
        def title(self):
                return "FastEO"

        # Decide to show menu in txt2img or img2img
        # - in "txt2img" -> is_img2img is `False`
        # - in "img2img" -> is_img2img is `True`
        #
        # below code always show extension menu
        def show(self, is_img2img):
                return scripts.AlwaysVisible

        # Setup menu ui detail
        def ui(self, is_img2img):
                with gr.Accordion('이오님이 개발할 예정', open=False):
                        with gr.Row():
                                checkbox = gr.Checkbox(
                                        False,
                                        label="USE THIS OPTION"
                                )
                return [checkbox]
        
        def process(self, p, *args):
                print("process Event")

        def process_before_every_sampling(self, p, *args, **kwargs):
                print("process_before_every_sampling")

        def process_before_every_step(self, p, *args, **kwargs):
                proc = process_images(p)
                if (len(proc.images) != 0):
                        proc.images[0].show()
                print("process_before_every_step")
                return proc

        def run(self, p, angle, checkbox):
                proc = process_images(p)
                return proc
        

