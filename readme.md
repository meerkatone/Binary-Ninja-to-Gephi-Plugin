# Gephi Callgraph Exporter

A Binary Ninja plugin that exports the call graph of a binary to a GEXF file for visualization in Gephi.

## Features

- Exports the complete call graph from a Binary Ninja analysis
- Includes function names, addresses, sizes, and instruction counts as node attributes
- Outputs in GEXF format, compatible with Gephi visualization software
- Integrated into Binary Ninja's UI with a simple tools menu option

## Installation

### Method 1: Using the Plugin Manager (Recommended)

1. In Binary Ninja, go to `Settings > Manage Plugins`
2. Click on "Install Plugin" and select the folder containing this plugin
3. Restart Binary Ninja

### Method 2: Manual Installation

1. Create a folder named `gephi_callgraph_exporter` in your Binary Ninja plugins directory:
   - Linux: `~/.binaryninja/plugins/`
   - macOS: `~/Library/Application Support/Binary Ninja/plugins/`
   - Windows: `%APPDATA%\Binary Ninja\plugins\`
2. Copy all the files from this repository into the folder you created
3. Restart Binary Ninja

## Dependencies

This plugin requires the NetworkX library. You can install it in Binary Ninja's Python environment:

```
pip install networkx
```

## Usage

1. Open a binary file in Binary Ninja
2. After analysis completes, go to `Tools > Export Call Graph to Gephi`
3. Choose a file location to save the GEXF file
4. Open the saved GEXF file in Gephi for visualization and analysis

## Visualizing in Gephi

1. Download and install [Gephi](https://gephi.org/) if you haven't already
2. Open Gephi and create a new project
3. Import the generated GEXF file via `File > Open`
4. Use Gephi's layout algorithms (e.g., ForceAtlas2) to arrange the nodes
5. Use the appearance panel to color or size nodes based on attributes such as function size or instruction count

## License

This plugin is released under the MIT License. See the LICENSE file for details.
