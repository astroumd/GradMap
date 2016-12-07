from pylab import *

# simulation parameters

temperature_range = np.arange(3000, 9000, 1000) # 3,000 K to 8,000 K
wavelength_range = np.logspace(-7.0, -3.0, 1000) # 100 nm to 1 mm

# physical constants

h = 6.626e-34 # Planck constant (J s)
kB = 1.381e-23 # Boltzmann constant (J/K)
c = 2.998e8 # speed of light (m/s)

def planck(wavelength, temperature):
    return 2.0 * np.pi * h * c**2 / (wavelength**5 * (np.exp(h * c / (wavelength * kB * temperature)) - 1.0))

for temperature in temperature_range:
    plt.loglog(wavelength_range, planck(wavelength_range, temperature), label='T = {:,} K'.format(temperature))

sun_data = np.loadtxt('ASTM_E-490.dat')
plt.loglog(sun_data[:, 0] * 1.0e-6, sun_data[:, 1] * 1.0e6 * 4.624e4, 'b.', fillstyle='none', label='Sun')

plt.xlabel('Wavelength (m)')
plt.ylabel('Spectral Radiance (W sr$^{-1}$ m$^{-3}$)')
plt.legend(loc='upper right')
plt.title('Planck Curves')
plt.show()
