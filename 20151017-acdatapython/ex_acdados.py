"""
EX_ACDADOS.PY

Material de apoio para o post "Acessando dados na rede com Python", no
Programando Ciência.

* Autor: Alexandre 'Jaguar' Fioravante de Siqueira
* Contato: http://www.programandociencia.com/sobre/
* Material de apoio:
    http://www.github.com/alexandrejaguar/programandociencia

* Para citar esse material, por favor utilize a referência abaixo:
DE SIQUEIRA, Alexandre Fioravante. Acessando dados na rede com Python.
Campinas: Programando Ciência, 17 de outubro de 2015. Disponível em:
http://programandociencia.com/2015/10/17/acessando-dados-na-rede-com-python/.
Acesso em: <DATA DE ACESSO>.

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
"""

from urllib.request import urlopen

import matplotlib.pyplot as plt
import pandas

# Guardamos a URL na variável url
url = 'http://real-chart.finance.yahoo.com/table.csv?s=PETR4.SA&d=9&e=17&f=2015&g=d&a=0&b=3&c=2000&ignore=.csv'

# A função urlopen copia o conteúdo da URL para a variável petr_csv
petr_csv = urlopen(url)

# Aqui, o Pandas lê o csv que urlopen obteve. Na linha de baixo,
# Pandas plota o gráfico.
petr = pandas.read_csv(petr_csv, index_col=0, parse_dates=True)
petr.plot(y='Adj Close')

# Melhorando os parâmetros e mostrando o gráfico.
plt.xlabel('Ano')
plt.ylabel('Cotação')
plt.legend().set_visible(False)
plt.show()
