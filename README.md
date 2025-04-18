# Binary-Ninja-to-Gephi-Plugin
A Binary Ninja plugin that exports the call graph of a binary to a GEXF file for visualization in Gephi.

## Features
- Exports the complete call graph from a Binary Ninja analysis
- Includes function names, addresses, sizes, and instruction counts as node attributes
- Outputs in GEXF format, compatible with Gephi visualization software
- Integrated into Binary Ninja's UI with a simple tools menu option

## Installation

Clone the repo:
- ```git clone https://github.com/meerkatone/Binary-Ninja-to-Gephi-Plugin.git ```

Create a folder named gephi_callgraph_exporter in your Binary Ninja plugins directory:
- Linux: ~/.binaryninja/plugins/\
- macOS: ~/Library/Application Support/Binary Ninja/plugins/\
- Windows: %APPDATA%\Binary Ninja\plugins\

- Copy all the files from this repository into the folder you created
- Restart Binary Ninja

## Dependencies
This plugin requires the NetworkX library. You can install it in Binary Ninja's Python environment:
- ```pip install networkx```

## Usage
- Open a binary file in Binary Ninja\
- After analysis completes, go to Tools > Export Call Graph to Gephi\
- Choose a file location to save the GEXF file\
- Open the saved GEXF file in Gephi for visualization and analysis\

## Visualizing in Gephi
- Download and install Gephi if you haven't already
- Open Gephi and create a new project
- Import the generated GEXF file via File > Open
- Use Gephi's layout algorithms (e.g., ForceAtlas2) to arrange the nodes
- Use the appearance panel to color or size nodes based on attributes such as function size or instruction count

