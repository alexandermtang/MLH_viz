mlh_viz
=======

Visualization of MLH Hackathon Communities

NOTE: Please do not distribute this data publicly


Installation
------------
Python Requirements:
- [Python 2.7](http://www.python.org/download/releases/2.7/)
- [networkx](http://networkx.lanl.gov/index.html)
- [matplotlib](http://matplotlib.org/)

For Windows:

For Linux/Mac:
Simply pip install -r requirements.txt. Note: matplotlib does require some dependencies not provided by pip such as freetype2. Please install these before pip installing. If you have any problems installing these via pip, visit the sites above.

We recommend you use a bundled python environment to run the code to make things simple. We recommend [WinPython](https://code.google.com/p/winpython/downloads/list)

Usage 
-----
###k-clique community visualization:

`python draw_cliques.py`

###d3 visualization:
- `python -m SimpleHTTPServer 8000`
- Open in browser:
- `localhost:8000/mlh_viz_us.html`
- `localhost:8000/clique_communities.html`
