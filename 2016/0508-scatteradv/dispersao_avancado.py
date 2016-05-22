"""
DISPERSAO_AVANCADO.PY

Material de apoio para a série de posts "Gráficos de dispersão complexos
no Python", no Programando Ciência.

* Autor: Alexandre 'Jaguar' Fioravante de Siqueira
* Contato: http://www.programandociencia.com/sobre/
* Material de apoio:
    http://www.github.com/alexandrejaguar/programandociencia

* Para citar esse material, por favor utilize a referência abaixo:
DE SIQUEIRA, Alexandre Fioravante. Gráficos de dispersão complexos no
Python [Parte I] - Obtendo dados e criando um gráfico preliminar.
Campinas: Programando Ciência, 08 de maio de 2016. Disponível em:
http://www.programandociencia.com/2016/05/08/graficos-de-dispersao-complexos-no-python-parte-i-obtendo-dados-e-criando-um-grafico-preliminar/
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

# importando os pacotes necessários.
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import pandas as pd

# lendo o arquivo dados_ibge.xls
dados_brasil = pd.read_excel('dados_ibge.xls', sheetname=2)

# paleta de cores 5-class Dark2, do ColorBrewer2: http://colorbrewer2.org/
cores = ['#1b9e77',
         '#d95f02',
         '#7570b3',
         '#e7298a',
         '#66a61e']


# a função atribui_cor() aponta a cor correspondente a cada região.
def atribui_cor(regiao):
    cores = {
        'Norte': '#1b9e77',
        'Nordeste': '#d95f02',
        'Sudeste': '#7570b3',
        'Sul': '#e7298a',
        'CentroOeste': '#66a61e'
    }
    return cores.get(regiao, 'black')

# criando o vetor de cores.
cor_regiao = list()
qtde_estados = len(dados_brasil['Regiao'])

for estado in range(qtde_estados):
    cor_regiao.append(atribui_cor(dados_brasil['Regiao'][estado]))

# gerando o gráfico.
plt.scatter(x=dados_brasil['ExpecVida'],
            y=dados_brasil['PIBperCapita'],
            s=dados_brasil['PopX1000'],
            c=cor_regiao,
            alpha=0.6)
plt.title('Desenvolvimento do Brasil em 2013, por estado', fontsize=22)
plt.xlabel('Expectativa de vida (anos)', fontsize=22)
plt.ylabel('PIB per capita (R$)', fontsize=22)
plt.grid(True)

# inserindo sigla dos estados em cada círculo.
for estado in range(len(dados_brasil['UF'])):
    plt.text(x=dados_brasil['ExpecVida'][estado],
             y=dados_brasil['PIBperCapita'][estado],
             s=dados_brasil['UF'][estado],
             fontsize=16)

# colocando legenda; como a legenda "normal" não funciona, a ideia
# é adaptar um objeto 2D com as cores que definimos.
regioes = ['Norte',
           'Nordeste',
           'Sudeste',
           'Sul',
           'Centro-Oeste']

# legenda 1
legend1_line2d = list()
for passo in range(len(cores)):
    legend1_line2d.append(mlines.Line2D([0], [0],
                                        linestyle="none",
                                        marker="o",
                                        alpha=0.6,
                                        markersize=15,
                                        markerfacecolor=cores[passo]))

legend1 = plt.legend(legend1_line2d,
                     regioes,
                     numpoints=1,
                     fontsize=22,
                     loc="best",
                     shadow=True)

# legenda 2
legend2_line2d = list()
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle="none",
                                    marker="o",
                                    alpha=0.6,
                                    markersize=np.sqrt(100),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle="none",
                                    marker="o",
                                    alpha=0.6,
                                    markersize=np.sqrt(1000),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle="none",
                                    marker="o",
                                    alpha=0.6,
                                    markersize=np.sqrt(10000),
                                    markerfacecolor='#D3D3D3'))

legend2 = plt.legend(legend2_line2d,
                     ['1', '10', '100'],
                     title='População (em 100.000)',
                     numpoints=1,
                     fontsize=20,
                     loc="upper left",
                     frameon=False,  # sem bordas
                     labelspacing=3,  # aumenta espaço entre rótulos
                     handlelength=5,  # aumenta espaço entre obj e texto
                     borderpad=4)  # aumenta a borda da legenda
plt.gca().add_artist(legend1)

plt.setp(legend2.get_title(), fontsize=22)  # aumenta tamanho da fonte
plt.show()
