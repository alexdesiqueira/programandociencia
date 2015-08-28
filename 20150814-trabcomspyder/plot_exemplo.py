"""
PLOT_EXEMPLO.PY

Material de apoio para o post "Trabalhando com o Spyder", no Programando
Ciência.

Support material for the blog post "Working with Spyder", on Programando
Ciência.

* Autor/Author: Alexandre 'Jaguar' Fioravante de Siqueira
* Contato/Contact: http://www.programandociencia.com/sobre/
* Material de apoio/Support material:
    http://www.github.com/alexandrejaguar/programandociencia

* Para citar esse material, por favor utilize a referência abaixo:
DE SIQUEIRA, Alexandre Fioravante. Trabalhando com o Spyder. Campinas:
Programando Ciência, 28 de agosto de 2015.
Disponível em: http://programandociencia.com/2015/08/14/
trabalhando-com-o-spyder-working-with-spyder/
Acesso em: <DATA DE ACESSO>.

* In order to cite this material, please use the reference below
(this is a Chicago-like style):
de Siqueira, Alexandre Fioravante. “Working with Spyder”. Programando
Ciência. 2015, August 28. Available at http://programandociencia.com/
2015/08/14/trabalhando-com-o-spyder-working-with-spyder/.
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
