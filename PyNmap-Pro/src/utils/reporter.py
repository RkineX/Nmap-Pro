import json
from datetime import datetime
from typing import Dict
from tabulate import tabulate

class ReportGenerator:
    def __init__(self, scan_data: Dict):
        self.scan_data = scan_data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_report(self, format: str = "text") -> str:
        """Generate report in specified format"""
        if format == "json":
            return self._json_report()
        elif format == "html":
            return self._html_report()
        else:
            return self._text_report()

    def _text_report(self) -> str:
        """Format results in human-readable text"""
        report = [f"Scan Report ({self.timestamp})\n"]
        for host, data in self.scan_data.items():
            report.append(f"\nHost: {host}")
            report.append(tabulate(
                [(p['port'], p['state'], p['service'], p.get('version', '')) 
                for p in data.get('ports', [])],
                headers=["Port", "State", "Service", "Version"]
            ))
        return "\n".join(report)

    def _json_report(self) -> str:
        """Generate JSON formatted report"""
        return json.dumps({
            "metadata": {"scan_date": self.timestamp},
            "results": self.scan_data
        }, indent=2)

    def _html_report(self) -> str:
        """Generate HTML report"""
        html = f"""<html>
<head><title>Scan Report {self.timestamp}</title></head>
<body>
<h1>Network Scan Report</h1>
<p>Generated: {self.timestamp}</p>"""
        
        for host, data in self.scan_data.items():
            html += f"""
<h2>Host: {host}</h2>
<table border="1">
<tr><th>Port</th><th>State</th><th>Service</th><th>Version</th></tr>"""
            for port in data.get('ports', []):
                html += f"""
<tr>
<td>{port['port']}</td>
<td>{port['state']}</td>
<td>{port['service']}</td>
<td>{port.get('version', '')}</td>
</tr>"""
            html += "</table>"
        return html + "</body></html>"
