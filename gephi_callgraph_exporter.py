from binaryninja import *
import networkx as nx
import os

class GephiCallgraphExporter(BackgroundTaskThread):
    def __init__(self, bv, output_file):
        BackgroundTaskThread.__init__(self, "Exporting call graph to Gephi...", True)
        self.bv = bv
        self.output_file = output_file

    def run(self):
        try:
            # Create a directed graph
            G = nx.DiGraph()

            # Add nodes (functions)
            for function in self.bv.functions:
                # Add the function as a node with attributes
                G.add_node(function.start,
                          name=function.name,
                          address="0x%x" % function.start,
                          size=function.total_bytes,
                          instruction_count=len(list(function.instructions)))

            # Add edges (calls between functions)
            for caller in self.bv.functions:
                for callee in caller.callees:
                    G.add_edge(caller.start, callee.start)

            # Export to GEXF format
            nx.write_gexf(G, self.output_file)
            log_info(f"Call graph exported to {self.output_file}")
        except Exception as e:
            log_error(f"Error exporting call graph: {str(e)}")


def export_callgraph_for_gephi(bv):
    # Create a default filename based on the current binary
    default_name = os.path.splitext(bv.file.filename)[0] + "_callgraph.gexf"

    # Open a file save dialog to let the user choose where to save the file
    output_file = get_save_filename_input("Save Call Graph as GEXF", "*.gexf", default_name)

    # If the user selected a file
    if output_file:
        # Ensure the file has the correct extension
        if not output_file.endswith(".gexf"):
            output_file += ".gexf"

        # Run the export in a background task
        task = GephiCallgraphExporter(bv, output_file)
        task.start()


# Register the plugin command in the tools menu
PluginCommand.register(
    "Export Call Graph to Gephi",
    "Exports the current binary's call graph to a GEXF file for visualization in Gephi",
    export_callgraph_for_gephi
)
