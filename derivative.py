# Derivative of a noisy dataset (hard X-ray spectrum)
# Example for Lecture 8 from
# https://www.astro.gla.ac.uk/users/eduard/lectures/HEA1/lecture_notes_HEA1.pdf

import numpy as np
import matplotlib.pyplot as plt
N=90
eps =np.arange(N)+10.
randn= np.random.normal(0., 1., N)
dJ_deps=1./eps
# 1/eps spectrum between 10 and 100 keV
dJ_deps_noise=dJ_deps+dJ_deps*0.03*randn
# adding 3% noise
plt.plot(eps, dJ_deps, 'r--',eps, dJ_deps_noise, 'b-' )
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Spectrum $J(\epsilon)$')
plt.xlabel('Photon energy $\epsilon$ [keV]')
#plotting Photon spectrum
plt.show()

# let us calculate electron spectrum using derivatives
#F_E=np.diff(eps,dJ_deps)
F_E= - np.gradient(dJ_deps, 1.)
F_E_noise= - np.gradient(dJ_deps_noise, 1.)
plt.plot(eps, F_E , 'r--',eps, F_E_noise, 'b-' )
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Derivative of the spectrum, ${dJ}/{d\epsilon}$')
plt.xlabel('Electron energy $E$ [keV]')
plt.show()

