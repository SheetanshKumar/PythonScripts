import os
import subprocess
files = [f for f in os.listdir('.') if os.path.isfile(f)]

ffmpedCmd = '''ffmpeg -i {} \
-c:v prores_ks \
-profile:v 1 \
-vendor apl0 \
-bits_per_mb 8000 \
-pix_fmt yuv422p10le \
{}.mov'''
for f in files:
    if len(f.split('.')[0]) == 0 or f.split('.')[-1].lower() != "mp4":
        print("file type not supported:", f)
        continue
    print(ffmpedCmd.format(f,f.split('.')[0]))
    subprocess.run(ffmpedCmd.format(f, f.split('.')[0]), shell=True)