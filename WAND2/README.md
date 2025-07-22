startup instructions

```
python3 -m venv --system-site-packages /epics/graphics/WAND2/hklplots
pip install -r requirements.txt
source /epics/graphics/WAND2/hklplots/bin/activate
export GI_TYPELIB_PATH=/usr/local/lib/girepository-1.0
python3 interactive_plot.py
```
