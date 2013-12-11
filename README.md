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
