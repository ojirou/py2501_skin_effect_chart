import matplotlib.pyplot as plt
import numpy as np
import subprocess
try:
    a0 = np.genfromtxt('data_chart\\250113skin_effect_chart.csv', delimiter=",", skip_header=1)
except Exception as e:
    print(f"Error loading data: {e}")
    raise
fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(a0[:, 0] / 1e6, a0[:, 1]*1e6, color="black", lw=1, ls='-', marker='o', markersize=0, label=r'iron')
ax.plot(a0[:, 0] / 1e6, a0[:, 2]*1e6, color="red", lw=1, ls='-', marker='o', markersize=0, label=r'aluminum')
ax.plot(a0[:, 0] / 1e6, a0[:, 3]*1e6, color="orange", lw=2, ls='-', marker='o', markersize=0, label=r'copper')
ax.plot(a0[:, 0] / 1e6, a0[:, 4]*1e6, color="gray", lw=2, ls='-', marker='o', markersize=0, label=r'silver')
ax.plot(a0[:, 0] / 1e6, a0[:, 5]*1e6, color="green", lw=1, ls='-', marker='o', markersize=0, label=r'graphite')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([1, 10000])
ax.set_ylim([0.1, 1000])
ax.set_title(r'Skin Effect Chart')
ax.set_xlabel(r'Frequency [MHz]', fontsize=11)
ax.set_ylabel(r'Skin Depth [um]', fontsize=11)
ax.legend(loc='upper right', fontsize=8)
ax.grid(ls=':')
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.15, top=0.92)
PdfFile = 'data_chart\\250113skin_effect.pdf'
fig.savefig(PdfFile)
subprocess.Popen(['start', PdfFile], shell=True)