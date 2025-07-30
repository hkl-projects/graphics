sudo apt install gfortran python3-venv
python3 -m venv --system-site-packages hklplots
source hklplots/bin/activate
pip install -r requirements.txt
export GI_TYPELIB_PATH=/usr/local/lib/girepository-1.0

git clone https://gitlab.com/soleil-data-treatment/soleil-software-projects/cif2hkl.git /usr/bin/
cd /usr/bin/cif2hkl
make
sudo make install
