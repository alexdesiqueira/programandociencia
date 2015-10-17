"""
EX_ACDATA.PY

Support material for the blog post "Getting data from the web using Python", on
Programando Ciência.

* Author: Alexandre 'Jaguar' Fioravante de Siqueira
* Contact: http://www.programandociencia.com/sobre/
* Support material:
    http://www.github.com/alexandrejaguar/programandociencia

* In order to cite this material, please use the reference below
(this is a Chicago-like style):
de Siqueira, Alexandre Fioravante. “Getting data from the web using Python”.
Programando Ciência. 2015, October 17. Available at
http://programandociencia.com/2015/10/17/getting-data-from-the-web-using-python/.
Access date: <ACCESS DATE>.

Copyright (C) Alexandre Fioravante de Siqueira

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from urllib.request import urlopen

import matplotlib.pyplot as plt
import pandas

# Saving the URL on url
url = 'http://real-chart.finance.yahoo.com/table.csv?s=YHOO&d=9&e=17&f=2015&g=d&a=3&b=12&c=1996&ignore=.csv'

# urlopen copies the content of URL to yahoo_csv
yahoo_csv = urlopen(url)

# Here, Pandas reads the csv from urlopen. On the other line,
# Pandas plots the series.
yahoo = pandas.read_csv(yahoo_csv, index_col=0, parse_dates=True)
yahoo.plot(y='Adj Close')

# Improving the plot and showing it.
plt.xlabel('Year')
plt.ylabel('Adj Close')
plt.legend().set_visible(False)
plt.show()
