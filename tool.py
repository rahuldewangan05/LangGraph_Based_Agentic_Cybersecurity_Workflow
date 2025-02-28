from langchain_core.tools import tool

import subprocess

@tool
def run_nmap(target):
    """Finding Open Ports Through NMAP"""
    command = f"nmap -p 1-1000 {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout


