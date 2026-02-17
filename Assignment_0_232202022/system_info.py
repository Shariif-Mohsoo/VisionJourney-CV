import platform
import psutil
import torch
import sys

print("=== SYSTEM INFORMATION ===")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
print(f"CPU Cores (Logical): {psutil.cpu_count(logical=True)}")
print(f"Total RAM (GB): {round(psutil.virtual_memory().total / (1024**3), 2)}")

print("\n=== PYTHON & LIBRARIES ===")
print(f"Python Version: {sys.version}")
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA Version: {torch.version.cuda}")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
else:
    print("GPU: Not Available")
