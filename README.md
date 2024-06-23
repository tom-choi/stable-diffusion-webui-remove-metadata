# stable-diffusion-webui-remove-metadata

# Metadata 文件移除工具

![alt text](image.png)

Easy extension for removing images metadata.

很簡單就可以把文件的Meta移除

## How to use


1. Clone this repo to `extensions` folder.
   - `https://github.com/tom-choi/stable-diffusion-webui-remove-metadata`
2. Restart webui.

## basic design
```
├── install.py (optional)
└── scripts
    ├── ${extension_name}.py
    ... (if extension need module division)
```

## BUGS

右側無法正常顯示文件

## Features

- Remove metadata from images.
- Support for multiple image formats.
- Support for multiple image sources.
- Support for multiple image outputs.