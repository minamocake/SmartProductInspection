
# Development Environment

OS：    
macOS Mojave10.14.3

Linbraries:   
tensorflow1.3.1
opencv-python4.0.0.21
keras 2.2.4
numpy 1.16.2


# How to Use

Clone this repository
```bash
cd SmartProductInspection
```

*When using for the first time, you must delete all files of list folder.

## Training


```bash
python ./CNN/train.py
```

## Evaluating

```bash
python ./CNN/test.py  --model ./CNN/YOUR_MODEL_NAME
```
## Realtime detection

```bash
python ./detect.py  --model ./CNN/YOUR_MODEL_NAME
```
## VIEW

Please access by Web browser(Reccomend: FireFox)
./SmartProductInspection/prtotypeUI/index_en.html
