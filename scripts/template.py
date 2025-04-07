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
                # 값의 범위 조정 (최소-최대 정규화)
                min_val = torch.min(kwargs['d']['denoised'])
                max_val = torch.max(kwargs['d']['denoised'])
                normalized_tensor = (kwargs['d']['denoised'] - min_val) / (max_val - min_val) * 255

                # 텐서를 이미지로 변환
                image_tensor = normalized_tensor.cpu().squeeze(0).permute(1, 2, 0).numpy().astype('uint8')
                image = Image.fromarray(image_tensor)

                # 이미지 저장 또는 표시
                image.show()
                print("process_before_every_step")

        def run(self, p, angle, checkbox):
                proc = process_images(p)
                print(proc,angle,checkbox)
                return proc
                return proc

