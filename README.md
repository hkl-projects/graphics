# Visualizer for WAND<sup>2</sup> elastic peaks

install the venv environment
```bash
sudo apt install gfortran python3-venv
python3 -m venv --system-site-packages hklplots
source hklplots/bin/activate
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

### Automated
```
source install.sh
./run.sh
```
