"""
PLOT_EXEMPLO.PY
---------------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

AUTHOR:
-------
    Alexandre 'Jaguar' Fioravante de Siqueira
    Personal site: www.programandociencia.com/sobre/

POST:
-----
    Trabalhando com o Spyder / Working with Spyder (14/08/2015)

MODIFIED FROM:
--------------
http://matplotlib.org/examples/text_labels_and_annotations/text_demo_fontdict.html

Demo using fontdict to control style of text and labels.
"""

import numpy as np
import matplotlib.pyplot as plt


font = {'family': 'Serif',
        'color': 'black',
        'weight': 'normal',
        'size': 16,
        }

x = np.linspace(0.0, 5.0, 100)
y = np.cos(2 * np.pi * x) * np.exp(-x)

plt.plot(x, y, 'r')
plt.title('Damped exponential decay', fontdict=font)
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
