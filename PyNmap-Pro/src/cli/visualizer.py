try:
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go
    from graphviz import Digraph
except ImportError:
    raise ImportError("Visualization features require matplotlib, plotly, and graphviz")

class NetworkVisualizer:
    def __init__(self, scan_data: Dict):
        self.scan_data = scan_data

    def plot_port_status(self, output_file: str = "port_status.png"):
        """Generate bar chart of port status distribution"""
        status_counts = {'open': 0, 'closed': 0, 'filtered': 0}
        for host in self.scan_data.values():
            for port in host.get('ports', []):
                status_counts[port['state']] += 1

        fig = go.Figure([go.Bar(
            x=list(status_counts.keys()),
            y=list(status_counts.values()),
            marker_color=['#2ecc71', '#e74c3c', '#f1c40f']
        )])
        fig.update_layout(
            title='Port Status Distribution',
            xaxis_title='Status',
            yaxis_title='Count'
        )
        fig.write_image(output_file)

    def generate_network_map(self, output_file: str = "network_map.gv"):
        """Create interactive network diagram"""
        dot = Digraph(comment='Network Map')
        
        # Add scanner node
        dot.node('S', 'Scanner', shape='cylinder')
        
        # Add targets and connections
        for host, data in self.scan_data.items():
            dot.node(host, f"{host}\n{data.get('os', 'Unknown OS')}")
            dot.edge('S', host, label=f"{len(data.get('ports', []))} open ports")
            
        dot.render(output_file, view=True)
