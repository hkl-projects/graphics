# Visualizer for WAND<sup>2</sup> elastic peaks

install the venv environment
```bash
python3 -m venv --system-site-packages /epics/graphics/WAND2/hklplots
source /epics/graphics/WAND2/hklplots/bin/activate
pip install -r requirements.txt
```

connect 
```bash
export GI_TYPELIB_PATH=/usr/local/lib/girepository-1.0
```

run the gui
```bash
python interactive_plot.py
```
