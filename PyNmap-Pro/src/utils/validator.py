import ipaddress
import re
from typing import Union

class InputValidator:
    @staticmethod
    def validate_target(target: str) -> bool:
        """Validate IP/Hostname input"""
        try:
            ipaddress.ip_address(target)
            return True
        except ValueError:
            return bool(re.match(r"^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$", target))

    @staticmethod
    def validate_port_range(ports: str) -> bool:
        """Validate port range format"""
        if ports == "-":
            return False
        parts = ports.split('-')
        if len(parts) > 2:
            return False
        try:
            start = int(parts[0])
            end = int(parts[-1])
            return 1 <= start <= end <= 65535
        except ValueError:
            return False

    @staticmethod
    def validate_scan_mode(mode: str) -> bool:
        """Validate scanning mode selection"""
        return mode in {"fast", "full", "stealth"}

    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """Sanitize user input to prevent injection attacks"""
        return re.sub(r"[^\w\.\-\/:]", "", input_str)
