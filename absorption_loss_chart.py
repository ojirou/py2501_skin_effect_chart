import matplotlib.pyplot as plt
import numpy as np
import subprocess
try:
    a0 = np.genfromtxt('data_chart\\250113absorption_loss_chart.csv', delimiter=",", skip_header=1)
except Exception as e:
    print(f"Error loading data: {e}")
    raise
fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(a0[:, 0] / 1e6, a0[:, 1], color="black", lw=1, ls='-', marker='o', markersize=0, label=r'iron, t=0.2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 2], color="black", lw=1, ls='--', marker='o', markersize=0, label=r'iron, t=2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 3], color="red", lw=1, ls='-', marker='o', markersize=0, label=r'aluminum, t=0.2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 4], color="red", lw=1, ls='--', marker='o', markersize=0, label=r'aluminum, t=2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 5], color="orange", lw=2, ls='-', marker='o', markersize=0, label=r'copper, t=0.2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 6], color="orange", lw=2, ls='--', marker='o', markersize=0, label=r'copper, t=2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 7], color="gray", lw=2, ls='-', marker='o', markersize=0, label=r'silver, t=0.2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 8], color="gray", lw=2, ls='--', marker='o', markersize=0, label=r'silver, t=2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 9], color="green", lw=1, ls='-', marker='o', markersize=0, label=r'graphite, t=0.2mm')
ax.plot(a0[:, 0] / 1e6, a0[:, 10], color="green", lw=1, ls='--', marker='o', markersize=0, label=r'graphite, t=2mm')
ax.set_xscale('log')
ax.set_yscale('linear')
ax.set_xlim([1, 1000])
ax.set_ylim([0, 200])
ax.set_title(r'Absorption Loss Chart')
ax.set_xlabel(r'Frequency [MHz]', fontsize=11)
ax.set_ylabel(r'Absorption Loss [dB]', fontsize=11)
ax.legend(loc='lower right', fontsize=7)
ax.grid(ls=':')
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.15, top=0.92)
PdfFile = 'data_chart\\250113absorption_loss_chart.pdf'
fig.savefig(PdfFile)
subprocess.Popen(['start', PdfFile], shell=True)