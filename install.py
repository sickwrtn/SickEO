import launch

if not launch.is_installed("pillow"):
    launch.run_pip("install pillow", "requirements for MagicPrompt")
if not launch.is_installed("torchvision"):
    launch.run_pip("install torchvision", "requirements for MagicPrompt")
# TODO: add pip dependency if need extra module only on extension

# if not launch.is_installed("aitextgen"):
#     launch.run_pip("install aitextgen==0.6.0", "requirements for MagicPrompt")
