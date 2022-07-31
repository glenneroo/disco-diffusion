import subprocess

# !nvidia-smi
print(subprocess.run(['nvidia-smi', '-L'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
