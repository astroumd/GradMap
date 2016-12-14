from pylab import *

# simulation parameters

temperature_range = np.arange(3000, 9000, 1000) # 3,000 K to 8,000 K
wavelength_range = np.logspace(-7.0, -3.0, 1000) # 100 nm to 1 mm

sun_radius = 6.955e8 # in metres
sun_distance = 1.496e11 # 1 au in metres

# physical constants

h = 6.626e-34 # Planck constant (J s)
kB = 1.381e-23 # Boltzmann constant (J/K)
c = 2.998e8 # speed of light (m/s)

def planck(wavelength, temperature):
    return 2.0 * np.pi * h * c**2 / (wavelength**5 * (np.exp(h * c / (wavelength * kB * temperature)) - 1.0))

for temperature in temperature_range:
    plt.loglog(wavelength_range, planck(wavelength_range, temperature), label='T = {:,} K'.format(temperature))

sun_wave, sun_temp = np.loadtxt('ASTM_E-490.dat', unpack=True)
plt.loglog(sun_wave * 1.0e-6, sun_temp * 1.0e6 * (sun_distance / sun_radius)**2, 'b.', fillstyle='none', label='Sun')
#sun_data = np.loadtxt('ASTM_E-490.dat')
#plt.loglog(sun_data[:, 0] * 1.0e-6, sun_data[:, 1] * 1.0e6 * (sun_distance / sun_radius)**2, 'b.', fillstyle='none', label='Sun')

plt.xlabel('Wavelength (m)')
plt.ylabel('Spectral Radiance (W sr$^{-1}$ m$^{-3}$)')
plt.legend(loc='upper right')
plt.title('Planck Curves')
plt.show()
