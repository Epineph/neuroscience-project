import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

time = np.linspace(0, 24, 100)

k_elim_ip = 0.1
k_elim_ic = 0.05
k_elim_iv = 0.2
k_elim_oral = 0.15
k_elim_in = 0.12

C0_scopolamine = 10
C0_d_amphetamine = 10

def drug_concentration(C, t, k_elim):
    return -k_elim * C

concentration_ip = odeint(drug_concentration, C0_scopolamine, time, args=(k_elim_ip,))
concentration_ic = odeint(drug_concentration, C0_scopolamine, time, args=(k_elim_ic,))
concentration_iv = odeint(drug_concentration, C0_scopolamine, time, args=(k_elim_iv,))
concentration_oral = odeint(drug_concentration, C0_scopolamine, time, args=(k_elim_oral,))
concentration_in = odeint(drug_concentration, C0_scopolamine, time, args=(k_elim_in,))

plt.figure(figsize=(12, 8))
plt.plot(time, concentration_ip, label='i.p. (Scopolamine)')
plt.plot(time, concentration_ic, label='i.c. (Scopolamine)')
plt.plot(time, concentration_iv, label='i.v. (Scopolamine)')
plt.plot(time, concentration_oral, label='Oral (Scopolamine)')
plt.plot(time, concentration_in, label='Intranasal (Scopolamine)')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration')
plt.title('Drug Concentration over Time for Different Routes of Administration (Scopolamine)')
plt.legend()
plt.show()
