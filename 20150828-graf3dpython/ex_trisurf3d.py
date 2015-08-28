"""
EX_TRISURF3D.PY

Material de apoio para o post "Gráficos tridimensionais no Python
[PARTE I]", no Programando Ciência.

Support material for the blog post "Three-dimensional plots on Python
[PART I]", on Programando Ciência.

* Autor/Author: Alexandre 'Jaguar' Fioravante de Siqueira
* Contato/Contact: http://www.programandociencia.com/sobre/
* Material de apoio/Support material:
    http://www.github.com/alexandrejaguar/programandociencia

* Para citar esse material, por favor utilize a referência abaixo:
DE SIQUEIRA, Alexandre Fioravante. Gráficos tridimensionais no Python
[PARTE I]. Campinas: Programando Ciência, 28 de agosto de 2015.
Disponível em:
http://programandociencia.com/2015/08/28/
graficos-tridimensionais-no-python-parte-i-three-dimensional-plots-on-python-part-i/.
Acesso em: <DATA DE ACESSO>.

* In order to cite this material, please use the reference below
(this is a Chicago-like style):
de Siqueira, Alexandre Fioravante. “Three-dimensional plots on Python
[PART I]”. Programando Ciência. 2015, August 28. Available at
http://programandociencia.com/2015/08/28/
graficos-tridimensionais-no-python-parte-i-three-dimensional-plots-on-python-part-i/.
Access date: <ACCESS DATE>.

Copyright (C) Alexandre Fioravante de Siqueira

Este programa é um software livre; você pode redistribuí-lo e/ou
modificá-lo dentro dos termos da Licença Pública Geral GNU como publicada
pela Fundação do Software Livre (FSF); na versão 3 da Licença, ou qualquer
versão posterior.

Este programa é distribuído na esperança de que possa ser útil, mas SEM
NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO a qualquer
MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para
maiores detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com
este programa. Se não, veja <http://www.gnu.org/licenses/>.

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

import matplotlib.pyplot as plt
import numpy as np

n_angles = 72
n_radii = 4

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)

# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=True)

# Repeat all angles for each radius
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Surface
z = np.sin(-x*(y**2))+np.cos((x**2)*-y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap='Oranges', linewidth=0.1)
plt.show()
