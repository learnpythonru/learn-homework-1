import ephem
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

mars = ephem.Mars('2000/01/01')
const = ephem.constellation(mars)
print(const)

j = ephem.Jupiter()
j.compute('1986/2/8')
print('%s %s' % (j.ra, j.dec))


