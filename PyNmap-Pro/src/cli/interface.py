import argparse
from tabulate import tabulate
from ..scanner.core_engine import PyNmapPro

class NmapCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="PyNmap Pro - Next-Gen Network Scanner")
        self._setup_arguments()
        self.scanner = PyNmapPro()

    def _setup_arguments(self):
        self.parser.add_argument('targets', nargs='+', 
                               help="Target IP(s) or range")
        self.parser.add_argument('-p', '--ports', default='1-1000',
                               help="Port range to scan")
        self.parser.add_argument('-m', '--mode', choices=['fast','full','stealth'],
                               default='fast', help="Scanning mode")
        self.parser.add_argument('-o', '--output', 
                               choices=['text','json','xml'], default='text')
        self.parser.add_argument('-v', '--vulnerability', 
                               action='store_true', help="Enable vuln check")

    def _select_arguments(self, mode: str) -> str:
        presets = {
            'fast': '-T4 -F',
            'full': '-sS -sV -O -A -T4',
            'stealth': '-sS -sV -T2 --max-parallelism 1'
        }
        return presets.get(mode, '-T4')

    def run(self):
        args = self.parser.parse_args()
        scan_args = self._select_arguments(args.mode)
        
        results = self.scanner.async_scan(args.targets)
        
        if args.vulnerability:
            results = self.scanner.vulnerability_check(results)
        
        self._display_results(results, args.output)

    def _display_results(self, data: Dict, format: str):
        # Implementation for different output formats
        pass
