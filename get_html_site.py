#video de instalação pentaho bi ser e pentaho pdi https://www.youtube.com/watch?v=f9jXIb0nHyo
#para adicionar os drivers de conexão com o banco é nesse caminho C:\Pentaho\pdi-ce-9.1.0.0-324\data-integration\lib
#criar banco no aws https://www.youtube.com/watch?v=PGhI-AmfhEs

#instalei com o comando python -m pip install requests
#instalei bs4
#instalei requests
#instalei lxml
#instalei html5lib

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL_REQUEST_MES = ["01","02"]

URL_REQUEST_MES_NOME = ["Janeiro","Fevereiro"]

URL_REQUEST_ANO = '2019'

df = pd.DataFrame(columns=["Nome","RemuneraçãoBruta (R$)","RemuneraçãoLíquida (R$)","Tributos (R$)","Mês","Ano"])

df.to_csv('remuneracao_servidores.csv', index=False)

for i in range(0, 2):    

    
    URL_REQUEST = 'https://www.al.sp.gov.br/repositorio/folha-de-pagamento/folha-'+URL_REQUEST_ANO+'-'+URL_REQUEST_MES[i]+'.html'

    req = requests.get(URL_REQUEST)

    if req.status_code == 200:
        print("A página html foi coletada")
        content = req.content
        
    soup = BeautifulSoup(content, 'html.parser')

    table_dados = soup.find_all(id="dados")

    table_dados_str = str(table_dados)
    
    df = pd.read_html(table_dados_str)[0]

    df['Mês'] = URL_REQUEST_MES_NOME[i]
    df['Ano'] = 2019
    
    print(df)    

    df.to_csv('remuneracao_servidores.csv',mode='a', index=False,header=False)#mode 'adiciona' informações ao arquivo existente ao inves de subescrever


