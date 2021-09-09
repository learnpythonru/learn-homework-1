import ephem
from datetime import datetime



date = datetime.now().date()
pl = getattr(ephem, 'Mars')
mars = pl(date)
const = ephem.constellation(mars)
print(const[1])

