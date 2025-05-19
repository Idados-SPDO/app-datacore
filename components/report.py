import streamlit as st

def render_report(selected_base):
    """
    Renderiza o relatório de metadados.
    """
    st.write("### Relatório de Metadados")
    
    st.html("""
    <div>
        <p><a href="#introducao">1. Introdução</a></p>
        <p><a href="#descricao-fontes">2. Descrição das Fontes de Dados</a></p>
        <p><a href="#tratamento-dados">3. Tratamento dos Dados</a></p>
        <p><a href="#qualidade-dados">4. Qualidade dos Dados</a></p>
        <p><a href="#disponibilizacao-dados">5. Disponibilização dos Dados</a></p>
        <p><a href="#overview-dados">6. Overview dos Dados</a></p>
    </div>
    """)

    if selected_base == "alagoas":
        st.html("<h2 id='introducao' style='text-align: left; font-size:18px;'>1. Introdução</h2>")
        st.markdown("""
            Este relatório apresenta uma análise detalhada dos metadados associados aos conjuntos de dados utilizados em nossos projetos recentes.
        
            Metadados, que são informações sobre os dados, desempenham um papel crucial na organização, acesso e interpretação eficaz das informações. Através da avaliação dos metadados, buscamos entender a estrutura, o contexto e a origem dos dados, facilitando a gestão e a utilização adequada das informações em nossos processos analíticos. 
        
            Este documento fornece uma visão abrangente dos principais elementos dos metadados, incluindo descrições, formatos e relações entre os dados, oferecendo uma base sólida para futuras análises, utilizações e otimizações.

            **Objetivo:** O Economiza Alagoas é um projeto da Secretaria de Fazenda do Estado de Alagoas que tem o objetivo de divulgar informações públicas sobre as vendas de produtos realizadas utilizando a Nota Fiscal de Consumidor Eletrônica – NFC-e. A plataforma é constituída de uma página WEB e um conjunto de serviços públicos na forma de uma API. Nenhuma informação que possa ser considerada privada é fornecida.

            **Histórico:** Com o objetivo de aprimorar o processo de análise para o contrato da SEFAZ-AL, que envolve a entrega dos PMPFs para uma lista específica de bebidas frias e ocorre de forma recorrente, foi estabelecida uma conexão com a API disponibilizada pela SEFAZ-AL.

            Identificou-se, então, a possibilidade de utilizar essa API tanto para balizar os preços calculados quanto para acompanhar continuamente suas variações. 

            A partir disso, foi desenvolvido um dashboard que consolida todos os preços obtidos pela API para a lista de interesse, facilitando a análise dos PMPFs e permitindo a identificação de possíveis sazonalidades.

            **Sigla:** Economiza Alagoas.

            **Temática:** Comércio varejista, atualmente foco em bebidas frias.
        
            **Situação do Processo:** Ativo.
        """)
        st.markdown("")
        st.html("<h2 id='descricao-fontes' style='text-align: left; font-size:18px;'>2. Descrição das Fontes de Dados</h2>")
        st.markdown("""
            2.1. **Fontes:** API Economiza Alagoas.

            2.2. **Forma obtenção:** Extração via API.

            2.3. **Periodicidade:** Mensal.

            2.4. **Início da série:** Maio de 2023.

            2.5. **Instituição Responsável:** Secretaria de Fazenda do Estado de Alagoas.

            2.6. **Área interna Responsável:** Coleta não tradicional – SPDO.

            2.7. **Unidade(s) de Análise:** Preços oriundos da Nota Fiscal de Consumidor Eletrônica.

            2.8. **Técnica de Investigação:** Amostra contendo o último preço registrado por estabelecimento.

            2.9. **População Alvo:** Varejo, estabelecimentos emitentes de NFC-e.

            2.10. **Abrangência Geográfica:** Estado de Alagoas, com detalhamento no nível municipal e bairro.
        """)
        st.markdown("")
        st.html("<h2 id='tratamento-dados' style='text-align: left; font-size:18px;'>3. Tratamento dos Dados</h2>")
        st.markdown("""
            3.1. **Processos de Limpeza:** Para trabalhar com uma base limpa, foram filtrados apenas os registros relacionados aos itens correspondentes à pauta da SEFAZ-AL, observando o GTIN de cada item, resultando em uma lista com cerca de 1600 itens que são solicitados na extração via API.

            3.2. **Transformações:** Não foi realizada nenhuma transformação nos dados.

            3.3. **Padronização:** Não foi realizado nenhum tipo de padronização.

            3.4. **Metodologia:** Todas as informações disponibilizadas pela plataforma, como descrição, código de barras e valor do produto, são obtidas a partir de vendas reais realizadas por todos os estabelecimentos que emitem NFC-e no Estado de Alagoas. Cada estabelecimento define e informa sua própria descrição do produto. Assim, leve em consideração as abreviações no momento da pesquisa. Caso o estabelecimento não informe o código de barras na NFC-e, o produto poderá ser encontrado apenas pela sua descrição. Os preços apresentados refletem o valor sem desconto e o da última venda realizada pelo estabelecimento no período de até 10 dias e não significa que são ofertas. Não há obrigação do estabelecimento seguir o mesmo preço praticado, já que pode ser oriundo de algum programa de relacionamento ou promoção temporária.

            3.5. **Época da Coleta:** Mensal, ocorrendo no dia 10 de cada mês.

            3.6. **Tempo Previsto entre o Início da Coleta e a Liberação dos Dados:** 3 dias.
        """)
        st.markdown("")
        st.html("<h2 id='qualidade-dados' style='text-align: left; font-size:18px;'>4. Qualidade dos Dados</h2>")
        st.markdown("""
            4.1. **Dicionário de Variáveis:**
        """)
        st.markdown("")
        st.markdown("""
                | Variável                | Tipo de Variável | Descrição                                                                        | Constraints |
            |-------------------------|------------------|----------------------------------------------------------------------------------|-------------|
            | codGetin                | integer          | Código EAN/GTIN do produto                                                       | NOT NULL    |
            | codNcm                  | integer          | Código NCM do produto                                                            | NOT NULL    |
            | dscProduto              | string           | Descrição completa do produto, de acordo com o estabelecimento                   | NOT NULL    |
            | valMinimoVendido        | numeric          | Valor mínimo vendido pelo estabelecimento para o produto, no período de 10 dias  | NOT NULL    |
            | valMaximoVendido        | numeric          | Valor máximo vendido pelo estabelecimento para o produto, no período de 10 dias  | NOT NULL    |
            | dthEmissaoUltimaVenda   | datetime         | Data e hora da última venda realizada pelo estabelecimento para o produto        | NOT NULL    |
            | valUnitarioUltimaVenda  | numeric          | Valor unitário da última venda realizada pelo estabelecimento para o produto     | NOT NULL    |
            | valUltimaVenda          | numeric          | Valor total da última venda realizada pelo estabelecimento para o produto        | NOT NULL    |
            | numCNPJ                 | string           | CNPJ do estabelecimento                                                          | NOT NULL    |
            | nomRazaoSocial          | string           | Razão social do estabelecimento                                                  | NOT NULL    |
            | nomFantasia             | string           | Nome fantasia do estabelecimento                                                 | -           |
            | numTelefone             | string           | Telefone do estabelecimento                                                      | -           |
            | nomLogradouro           | string           | Endereço do estabelecimento                                                      | NOT NULL    |
            | numImovel               | string           | Número imóvel do estabelecimento                                                 | NOT NULL    |
            | nomBairro               | string           | Nome do bairro do estabelecimento                                                | NOT NULL    |
            | numCep                  | integer          | Número do CEP do estabelecimento                                                 | NOT NULL    |
            | nomMunicipio            | string           | Município do estabelecimento                                                     | NOT NULL    |
            | numLatitude             | numeric          | Número da latitude do estabelecimento                                            | NOT NULL    |
            | numLongitude            | numeric          | Número da longitude do estabelecimento                                           | NOT NULL    |
        """)
        st.markdown("")
        st.markdown("""
                4.2. **Métricas:**
        """)
        st.markdown("""
                        4.2.1. **Quantidade de registros:** 1.639.127.

                        4.2.2. **Referência:** Agosto de 2024.

                        4.2.3. **Última atualização:** 31 de agosto de 2024.

                        4.2.4. **Quantidade de estabelecimentos:** 1.208.

                        4.2.5. **Quantidade de produtos:** 530.

                        4.2.6. **Última data registrada:** 31 de agosto de 2024.

                        4.2.7. **Primeira data registrada:** 04 de junho de 2023.
            
                        4.2.8. **Completude:**
        """)
        st.markdown("")
        st.markdown("""
                | Variável | Preenchimento |
                |----------|---------------|
                | codGetin | 100% |
                | codNcm | 100% |
                | dscProduto | 100% |
                | valMinimoVendido | 100% |
                | valMaximoVendido | 100% |
                | dthEmissaoUltimaVenda | 100% |
                | valUnitarioUltimaVenda | 100% |
                | valUltimaVenda | 100% |
                | numCNPJ | 100% |
                | nomRazaoSocial | 100% |
                | nomFantasia | 77% |
                | numTelefone | 62% |
                | nomLogradouro | 100% |
                | numImovel | 100% |
                | nomBairro | 100% |
                | numCep | 100% |
                | nomMunicipio | 100% |
                | numLatitude | 100% |
                | numLongitude | 100% |
        """)
        st.markdown("")
        st.markdown("""
                    4.2.9. **Problemas Identificados:** No mês de agosto de 2024 não foi possível realizar a extração no período previsto, por conta de uma instabilidade na API. Os dados somente foram coletados no dia 01 de setembro de 2024.
        """)
        st.markdown("")
        st.html("<h2 id='disponibilizacao-dados' style='text-align: left; font-size:18px;'>5. Disponibilização dos Dados</h2>")
        st.markdown("""
                5.1. **Armazenamento e Formatado:** Arquivo em csv, salvo na rede (Y:\Mineração e Metodologia\Projetos\\00_Metodologia\\2. Desenvolvimento\Economiza Alagoas\Rproject\input).

                5.2. **Método de acesso aos dados:** Página de Relatórios.

                5.3. **Interface de Acesso:** Dashboard em Power BI.

                5.4. **Funcionalidades:** Estatísticas descritivas da base, lista de itens, percentual de cobertura dos itens e segmentos, estatística relacionados a preços por item e segmento, PMPF por item, peso por segmento, análise histórica do PMPF e acesso aos microdados.

                5.5. **Nível de Divulgação:** Estadual, contemplando os municípios de Arapiraca, Palmeira dos Índios, Maceió, União dos Palmares, São Miguel dos Campos, Penedo, Maragogi, Marechal Deodoro, Rio Largo, Coruripe, Delmiro Gouveia e Santana do Ipanema.

                5.6. **Área responsável pelo acesso:** Gestão de Dados – SPDO.
        """)
        st.markdown("")
        st.html("<h2 id='overview-dados' style='text-align: left; font-size:18px;'>6. Overview dos Dados</h2>")
        st.markdown("""
                6.1. **Demonstração dos Dados:**
        """)
        #st.image("assets/alagoas/demonstracao.png",use_container_width =True)
        st.markdown("")
        st.markdown("""
                6.2. **Estatísticas Descritivas:**
        """)
        #st.image("assets/alagoas/descritiva1.png", use_container_width =True)
        #st.image("assets/alagoas/descritiva2.png", use_container_width =True)
        st.markdown("")
    elif selected_base == "pastorinho":
        st.html("<h2 id='introducao' style='text-align: left; font-size:18px;'>1. Introdução</h2>")
        st.markdown("""
            Este relatório apresenta uma análise detalhada dos metadados associados aos conjuntos de dados utilizados em nossos projetos recentes. 
            
            Metadados, que são informações sobre os dados, desempenham um papel crucial na organização, acesso e interpretação eficaz das informações. Através da avaliação dos metadados, buscamos entender a estrutura, o contexto e a origem dos dados, facilitando a gestão e a utilização adequada das informações em nossos processos analíticos. 
            
            Este documento fornece uma visão abrangente dos principais elementos dos metadados, incluindo descrições, formatos e relações entre os dados, oferecendo uma base sólida para futuras análises, utilizações e otimizações.

            **Objetivo:** Levantar informações dos equipamentos sociais da proteção básica – Centros de Referência da Assistência social (CRAS) para aquisição de conhecimento a respeito do funcionamento e das atividades realizadas nesses centros.

            **Histórico:** A partir de agosto de 2023, passamos a receber os lotes mensais de quatro filiais do Supermercado Pastorinho, situadas nos bairros Santana, Perdizes, Vila Mariana e Jardim Iris, todos localizados no município de São Paulo. Cada lote compreende, em média, 45 mil itens de preços variados. Importante destacar que os preços contidos em cada lote permanecem válidos ao longo do mês até a chegada do próximo lote, garantindo consistência e estabilidade durante esse período.

            **Sigla:** Pastorinho.

            **Temática:** Comércio varejista de alimentos

            **Situação do Processo:** Ativo.
        """)
        st.markdown("")
        st.html("<h2 id='descricao-fontes' style='text-align: left; font-size:18px;'>2. Descrição das Fontes de Dados</h2>")
        st.markdown("""
            2.1. **Fontes:** Parceria de dados.

            2.2. **Forma obtenção:** Recebimento via parceiro.

            2.3. **Periodicidade:** Mensal.

            2.4. **Início da série:** Agosto de 2023.

            2.5. **Instituição Responsável:** Pastorinho.

            2.6. **Área interna Responsável:** Coleta não tradicional – SPDO.
            
            2.7. **Unidade(s) de Análise:** Preços oriundos da Nota Fiscal de supermercados parceiros.
           
            2.8. **Técnica de Investigação:** Censitária, considerando dados transacionais.
            
            2.9. **População Alvo:** Varejo.
            
            2.10. **Abrangência Geográfica:** Santana, Perdizes, Vila Mariana e Jardim Iris, todos localizados no município de São Paulo.
        """)
        st.markdown("")
        st.html("<h2 id='tratamento-dados' style='text-align: left; font-size:18px;'>3. Tratamento dos Dados</h2>")
        st.markdown("""
            3.1. **Processos de Limpeza:** -.

            3.2. **Transformações:** -.

            3.3. **Padronização:** -.

            3.4. **Metodologia:** -.

            3.5. **Época da Coleta:** -.

            3.6. **Tempo Previsto entre o Início da Coleta e a Liberação dos Dados:**.
        """)
        st.markdown("")
        st.html("<h2 id='qualidade-dados' style='text-align: left; font-size:18px;'>4. Qualidade dos Dados</h2>")
        st.markdown("""
            4.1. **Dicionário de Variáveis:**
        """)
        st.markdown("")
        st.markdown("""
            | Variável          | Tipo de Variável | Descrição                                        | Constraints |
            |------------------|----------------|------------------------------------------------|------------|
            | ano_mes         |                | Data de referência da coleta                   |            |
            | data_coleta     | datetime       | Data de envio                                  |            |
            | Município      | string         | Município da loja                              |            |
            | Endereço       | string         | Endereço da loja                               |            |
            | Bairro         | string         | Bairro da loja                                 |            |
            | nome_fantasia  | string         | Nome fantasia da rede                         |            |
            | Rede           | string         | Rede de supermercado                          |            |
            | id_loja        |                | Identificação da loja                         |            |
            | Secao          |                | Seção do supermercado do produto              |            |
            | Categoria      | string         | Categoria do produto                          |            |
            | Subcategoria   | string         | Subcategoria do produto                       |            |
            | id_produto     |                | Identificação do produto (codificação do cliente) |       |
            | GTIN_EAN       |                | Código de barras do produto                   |            |
            | Sku            | string         | Descrição completa do produto                 |            |
            | Preco          | numeric        | Preço do produto                              |            |
            | Fabricante     | string         | Fabricante do produto                         |            |
            | Marca          | string         | Marca do produto                              |            |
            | Qtd           | numeric        | Quantidade do produto                         |            |
            | Und            | string         | Unidade de medida do produto                 |            |
            | Cesta          |                | Produto selecionado para cálculo da cesta de consumo |        |
            | cesta_categoria |                | Produto selecionado para cálculo da cesta de consumo |        |
            | fator_correc   | numeric        | Fator de correção para cálculo do preço em Kg |            |
            | preco_KG       | numeric        | Preço em Kg para o cálculo da cesta           |            |

        """)
        st.markdown("")
        st.markdown("""
                4.2. **Métricas:**
        """)
        st.markdown("""
                        4.2.1.	**Quantidade de registros:** 229.083.
                        
                        4.2.2.	**Referência:** -.
                        
                        4.2.3.	**Última atualização:** -.
                        
                        4.2.4.	**Quantidade de fabricantes:** 1.132.
                       
                        4.2.5.	**Quantidade de marcas:** 801.
                        
                        4.2.6.	**Quantidade de produtos:** 23.866.
                        
                        4.2.7.	**Última data registrada:** -.
                        
                        4.2.8.	**Primeira data registrada:** -.
                        
                        4.2.9.	**Completude:** -
                        
                        4.2.10.	**Problemas Identificados:** -.
        """)

        st.markdown("")
        st.html("<h2 id='disponibilizacao-dados' style='text-align: left; font-size:18px;'>5. Disponibilização dos Dados</h2>")
        st.markdown("""
                5.1. **Armazenamento e Formatado:** -.

                5.2. **Método de acesso aos dados:** -.

                5.3. **Interface de Acesso:** -.

                5.4. **Funcionalidades:** -.

                5.5. **Nível de Divulgação:** -.

                5.6. **Área responsável pelo acesso:** Gestão de Dados – SPDO.

        """)
        st.markdown("")
        st.html("<h2 id='overview-dados' style='text-align: left; font-size:18px;'>6. Overview dos Dados</h2>")
        st.markdown("""
                6.1. **Demonstração dos Dados:**
        """)
        st.write("Ainda não disponível.")
        #st.image("assets/pastorinho/demonstracao.png",use_container_width =True)
        st.markdown("")
        st.markdown("""
                6.2. **Estatísticas Descritivas:**
        """)
        #st.image("assets/pastorinho/descritiva1.png",use_container_width =True)
        #st.image("assets/pastorinho/descritiva2.png",use_container_width =True)
        st.markdown("")
    elif selected_base == "receita":
        st.html("<h2 id='introducao' style='text-align: left; font-size:18px;'>1. Introdução</h2>")
        st.markdown("""
            Este relatório apresenta uma análise detalhada dos metadados associados aos conjuntos de dados utilizados em nossos projetos recentes. 
            
            Metadados, que são informações sobre os dados, desempenham um papel crucial na organização, acesso e interpretação eficaz das informações. Através da avaliação dos metadados, buscamos entender a estrutura, o contexto e a origem dos dados, facilitando a gestão e a utilização adequada das informações em nossos processos analíticos. 
            
            Este documento fornece uma visão abrangente dos principais elementos dos metadados, incluindo descrições, formatos e relações entre os dados, oferecendo uma base sólida para futuras análises, utilizações e otimizações.

            **Objetivo:**  O Cadastro Nacional da Pessoa Jurídica (CNPJ) é um banco de dados gerenciado pela Secretaria Especial da Receita Federal do Brasil (RFB), que armazena informações cadastrais das pessoas jurídicas e outras entidades de interesse das administrações tributárias da União, dos Estados, do Distrito Federal e dos Municípios.
            
            **Histórico:** Buscando aprimorar o processo de mapeamento de estabelecimentos, foi desenvolvido o app “Sistema Web Empresas”, e para isso, é preciso acessar a base de CNPJs da RFB, disponibilizando as empresas ativas por CNAE, UF e município.
            
            **Sigla:** RFB.

            **Temática:** Empresas cadastradas na Receita Federal Brasileira.
        
            **Situação do Processo:** Ativo.
        """)
        st.markdown("")
        st.html("<h2 id='descricao-fontes' style='text-align: left; font-size:18px;'>2. Descrição das Fontes de Dados</h2>")
        st.markdown("""
            2.1. **Fontes:** Site disponibilizado pela RFB (https://200.152.38.155/CNPJ/).

            2.2. **Forma obtenção:** : Extração via robô (python).

            2.3. **Periodicidade:** Trimestral.

            2.4. **Início da série:** Julho de 2022.

            2.5. **Instituição Responsável:** : Secretaria Especial da Receita Federal do Brasil (RFB).

            2.6. **Área interna Responsável:** Coleta não tradicional – SPDO.

            2.7. **Unidade(s) de Análise:** Dados cadastrais.

            2.8. **Técnica de Investigação:** Censitária.

            2.9. **População Alvo:** CNPJs em território brasileiro, focado nas empresas ativas.

            2.10. **Abrangência Geográfica:** Nacional.
        """)
        st.markdown("")
        st.html("<h2 id='tratamento-dados' style='text-align: left; font-size:18px;'>3. Tratamento dos Dados</h2>")
        st.markdown("""
            3.1. **Processos de Limpeza:** : Para trabalhar com uma base de empresas ativas, foram filtrados apenas os registros com STATUS ativo no momento da coleta.

            3.2. **Transformações:** Para consolidar as 10 tabelas obtidas na extração, é realizada a seguinte Query no SQL:

            """"""""")
        st.code("""
        CREATE TABLE mvp_cons AS(
SELECT 
   concat(e.cnpj,'', e.cnpj_ordem,'', e.cnpj_dv) as cnpj, 
   e.nome as nome_fantasia, 
   emp.razao as razao_social, 
   e.matriz_filial, 
   emp.porte,
   emp.capital, 
   e.situacao, 
   e.cnae_fiscal, 
   concat(e.cnae_fiscal, ' - ', c.descricao) as cnae_descr, 
   e.cnae_secundario, 
   e.logradouro, 
   e.numero, 
   e.complemento, 
   e.bairro, 
   e.cep, 
   e.uf, 
   m.descricao as municipio, 
   e.ddd_1, 
   e.telefone_1, 
   e.ddd_2, 
   e.telefone_2, 
   e.email 
FROM 
   public.estabelecimentos e
   LEFT JOIN public.municipios m ON e.municipio = m.codigo
   LEFT JOIN public.empresas emp ON e.cnpj = emp.cnpj
   LEFT JOIN public.cnaes c ON e.cnae_fiscal = c.codigo
WHERE 
   e.situacao='2'
);


        """)
        
        st.markdown("""
         3.3. **Padronização:** Não foi realizado nenhum tipo de padronização.

            3.4. **Metodologia:** : A base é disponibilizada mensalmente no site da RFB, considerando as alterações cadastrais, como endereço, telefone, CNAE ou até mesmo o status da empresa, além de incluir novos CNPJs que foram cadastrados.
            
            3.5. **Época da Coleta:** Trimestral (Janeiro – Abril – Julho – Outubro).

            3.6. **Tempo Previsto entre o Início da Coleta e a Liberação dos Dados:** 5 dias.
        """)
           
        st.markdown("")
        st.html("<h2 id='qualidade-dados' style='text-align: left; font-size:18px;'>4. Qualidade dos Dados</h2>")
        st.markdown("""
            4.1. **Dicionário de Variáveis:**
        """)
        st.markdown("")
        st.markdown("""
            4.1.1. **CNAEs:**
        """)
        st.markdown("""
                | Variável                | Tipo de Variável | Descrição                                                                        | Constraints |
            |-------------------------|------------------|----------------------------------------------------------------------------------|-------------|
            | CÓDIGO                  | string           | CÓDIGO DA ATIVIDADE ECONÔMICA                                                    | PK          |
            | DESCRIÇÃO               | string           | NOME DA ATIVIDADE ECONÔMICA                                                      | NOT NULL    |
            
        """)

        st.markdown("""
            4.1.2. **Dados simples:**
        """)
        st.markdown("""
            | Variável                     | Tipo de Variável | Descrição                                      | Constraints   |
            |------------------------------|------------------|------------------------------------------------|---------------|
            | CNPJ BÁSICO                 | string           | NÚMERO BASE DE INSCRIÇÃO NO CNPJ (OITO PRIMEIROS DÍGITOS DO CNPJ). | NOT NULL      |
            | OPÇÃO PELO SIMPLES          | string           | INDICADOR DA EXISTÊNCIA DA OPÇÃO PELO SIMPLES. |               |
            | DATA DE OPÇÃO PELO SIMPLES  | date             | DATA DE OPÇÃO PELO SIMPLES                     | NOT NULL      |
            | DATA DE EXCLUSÃO DO SIMPLES | date             | DATA DE EXCLUSÃO DO SIMPLES                    | -             |
            | OPÇÃO PELO MEI              | string           | INDICADOR DA EXISTÊNCIA DA OPÇÃO PELO MEI      |               |
            | DATA DE OPÇÃO PELO MEI      | date             | DATA DE OPÇÃO PELO MEI                         | -             |
            | DATA DE EXCLUSÃO DO MEI     | date             | DATA DE EXCLUSÃO DO MEI                        | -             |

        """)
        st.markdown("""
            4.1.3. **Empresas:**
        """)
        st.markdown("""
            | Variável                          | Tipo de Variável | Descrição                                                                                                      | Constraints   |
            |-----------------------------------|------------------|----------------------------------------------------------------------------------------------------------------|---------------|
            | CNPJ BÁSICO                      | string           | NÚMERO BASE DE INSCRIÇÃO NO CNPJ (OITO PRIMEIROS DÍGITOS DO CNPJ).                                             | NOT NULL      |
            | RAZÃO SOCIAL / NOME EMPRESARIAL  | string           | NOME EMPRESARIAL DA PESSOA JURÍDICA                                                                            | -             |
            | NATUREZA JURÍDICA                | integer          | CÓDIGO DA NATUREZA JURÍDICA                                                                                    | NOT NULL      |
            | QUALIFICAÇÃO DO RESPONSÁVEL      | integer          | QUALIFICAÇÃO DA PESSOA FÍSICA RESPONSÁVEL PELA EMPRESA                                                         | NOT NULL      |
            | CAPITAL SOCIAL DA EMPRESA        | integer          | CAPITAL SOCIAL DA EMPRESA                                                                                      | NOT NULL      |
            | PORTE DA EMPRESA                 | integer          | CÓDIGO DO PORTE DA EMPRESA: 00 – NÃO INFORMADO, 01 - MICRO EMPRESA, 05 - DEMAIS | 03 - EMPRESA DE PEQUENO PORTE                                                                               | -             |
            | ENTE FEDERATIVO RESPONSÁVEL      | integer          | O ENTE FEDERATIVO RESPONSÁVEL É PREENCHIDO PARA OS CASOS DE ÓRGÃOS E ENTIDADES DO GRUPO DE NATUREZA JURÍDICA 1XXX. PARA AS DEMAIS NATUREZAS, ESTE ATRIBUTO FICA EM BRANCO. | -             |

        """)
        st.markdown("""
            4.1.4. **Estabelecimentos:**
        """)
        st.markdown("""
            | Variável                       | Tipo de Variável | Descrição                                                                                              | Constraints   |
|--------------------------------|------------------|--------------------------------------------------------------------------------------------------------|---------------|
| CNPJ BÁSICO                   | string           | NÚMERO BASE DE INSCRIÇÃO NO CNPJ (OITO PRIMEIROS DÍGITOS DO CNPJ).                                     | NOT NULL      |
| CNPJ ORDEM                    | string           | NÚMERO DO ESTABELECIMENTO DE INSCRIÇÃO NO CNPJ (DO NONO ATÉ O DÉCIMO SEGUNDO DÍGITO DO CNPJ).          | NOT NULL      |
| CNPJ DV                       | string           | DÍGITO VERIFICADOR DO NÚMERO DE INSCRIÇÃO NO CNPJ (DOIS ÚLTIMOS DÍGITOS DO CNPJ).                      | NOT NULL      |
| IDENTIFICADOR MATRIZ/FILIAL   | integer          | CÓDIGO DO IDENTIFICADOR MATRIZ/FILIAL: 1 – MATRIZ, 2 – FILIAL                                          | NOT NULL      |
| NOME FANTASIA                 | string           | CORRESPONDE AO NOME FANTASIA                                                                           | -             |
| SITUAÇÃO CADASTRAL            | integer          | CÓDIGO DA SITUAÇÃO CADASTRAL: 01 – NULA, 2 – ATIVA, 3 – SUSPENSA, 4 – INAPTA, 08 – BAIXADA             | NOT NULL      |
| DATA SITUAÇÃO CADASTRAL       | date             | DATA DO EVENTO DA SITUAÇÃO CADASTRAL                                                                   | -             |
| MOTIVO SITUAÇÃO CADASTRAL     | string           | CÓDIGO DO MOTIVO DA SITUAÇÃO CADASTRAL                                                                 | NOT NULL      |
| NOME DA CIDADE NO EXTERIOR    | string           | NOME DA CIDADE NO EXTERIOR                                                                             | -             |
| PAIS                          | integer          | CÓDIGO DO PAIS                                                                                         | -             |
| DATA DE INÍCIO ATIVIDADE      | date             | DATA DE INÍCIO DA ATIVIDADE                                                                            | NOT NULL      |
| CNAE FISCAL PRINCIPAL         | string           | CÓDIGO DA ATIVIDADE ECONÔMICA PRINCIPAL DO ESTABELECIMENTO                                             | NOT NULL      |
| CNAE FISCAL SECUNDÁRIA        | string           | CÓDIGO DA(S) ATIVIDADE(S) ECONÔMICA(S) SECUNDÁRIA(S) DO ESTABELECIMENTO                                | -             |
| TIPO DE LOGRADOURO            | string           | DESCRIÇÃO DO TIPO DE LOGRADOURO                                                                        | -             |
| LOGRADOURO                   | string           | NOME DO LOGRADOURO ONDE SE LOCALIZA O ESTABELECIMENTO                                                  | -             |
| NÚMERO                        | string           | NÚMERO ONDE SE LOCALIZA O ESTABELECIMENTO. QUANDO NÃO HOUVER PREENCHIMENTO DO NÚMERO HAVERÁ ‘S/N’.     | NOT NULL      |
| COMPLEMENTO                   | string           | COMPLEMENTO PARA O ENDEREÇO DE LOCALIZAÇÃO DO ESTABELECIMENTO                                          | -             |
| BAIRRO                        | string           | BAIRRO ONDE SE LOCALIZA O ESTABELECIMENTO                                                              | -             |
| CEP                           | string           | CÓDIGO DE ENDEREÇAMENTO POSTAL REFERENTE AO LOGRADOURO NO QUAL O ESTABELECIMENTO ESTÁ LOCALIZADO       | -             |
| UF                            | string           | SIGLA DA UNIDADE DA FEDERAÇÃO EM QUE SE ENCONTRA O ESTABELECIMENTO                                     | NOT NULL      |
| MUNICÍPIO                     | integer          | CÓDIGO DO MUNICÍPIO DE JURISDIÇÃO ONDE SE ENCONTRA O ESTABELECIMENTO                                   | NOT NULL      |
| DDD 1                         | string           | CONTÉM O DDD 1                                                                                         | -             |
| TELEFONE 1                    | string           | CONTÉM O NÚMERO DO TELEFONE 1                                                                          | NOT NULL      |
| DDD 2                         | string           | CONTÉM O DDD 2                                                                                         | -             |
| TELEFONE 2                    | string           | CONTÉM O NÚMERO DO TELEFONE 2                                                                          | -             |
| DDD DO FAX                    | string           | CONTÉM O DDD DO FAX                                                                                    | -             |
| FAX                           | string           | CONTÉM O NÚMERO DO FAX                                                                                 | -             |
| CORREIO ELETRÔNICO            | string           | CONTÉM O E-MAIL DO CONTRIBUINTE                                                                        | -             |
| SITUAÇÃO ESPECIAL             | string           | SITUAÇÃO ESPECIAL DA EMPRESA                                                                           | -             |
| DATA DA SITUAÇÃO ESPECIAL     | date             | DATA EM QUE A EMPRESA ENTROU EM SITUAÇÃO ESPECIAL                                                      | -             |

        """)

        st.markdown("""
            4.1.5. **Motivo Cadastral**
        """)
        st.markdown("""
            | Variável   | Tipo de Variável | Descrição                     | Constraints |
|------------|------------------|-------------------------------|-------------|
| CÓDIGO     | integer          | CÓDIGO DO MOTIVO CADASTRAL    | PK          |
| DESCRIÇÃO  | string           | NOME DO MOTIVO CADASTRAL      | NOT NULL    |

        """)
        st.markdown("""
            4.1.6. **Municípios**
        """)
        st.markdown("""
            | Variável   | Tipo de Variável | Descrição          | Constraints |
|------------|------------------|--------------------|-------------|
| CÓDIGO     | integer          | CÓDIGO DO MUNICÍPIO | PK          |
| DESCRIÇÃO  | string           | NOME DO MUNICÍPIO   | NOT NULL    |

        """)

        st.markdown("""
            4.1.7. **Naturezas**
        """)
        st.markdown("""
            | Variável   | Tipo de Variável | Descrição                  | Constraints |
|------------|------------------|----------------------------|-------------|
| CÓDIGO     | integer          | CÓDIGO DA NATUREZA JURÍDICA | PK          |
| DESCRIÇÃO  | string           | NOME DA NATUREZA JURÍDICA   | NOT NULL    |

        """)

        st.markdown("""
            4.1.8. **Países**
        """)
        st.markdown("""
            | Variável   | Tipo de Variável | Descrição         | Constraints |
|------------|------------------|-------------------|-------------|
| CÓDIGO     | integer          | CÓDIGO DO PAÍS    | PK          |
| DESCRIÇÃO  | string           | NOME DO PAÍS      | NOT NULL    |

        """)

        st.markdown("""
            4.1.9. **Qualificações**
        """)
        st.markdown("""
            | Variável   | Tipo de Variável | Descrição                        | Constraints |
|------------|------------------|----------------------------------|-------------|
| CÓDIGO     | integer          | CÓDIGO DA QUALIFICAÇÃO DO SÓCIO  | PK          |
| DESCRIÇÃO  | string           | NOME DA QUALIFICAÇÃO DO SÓCIO    | NOT NULL    |

        """)
        st.markdown("""
            4.1.10. **CNAEs**
        """)
        st.markdown("""
            | Variável                                    | Tipo de Variável | Descrição                                                                                                                                               | Constraints |
|---------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| CNPJ BÁSICO                                | string           | NÚMERO BASE DE INSCRIÇÃO NO CNPJ (CADASTRO NACIONAL DA PESSOA JURÍDICA).                                                                                | NOT NULL    |
| IDENTIFICADOR DE SÓCIO                     | integer          | CÓDIGO DO IDENTIFICADOR DE SÓCIO: 1 – PESSOA JURÍDICA, 2 – PESSOA FÍSICA, 3 – ESTRANGEIRO                                                               | NOT NULL    |
| NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ) | string           | NOME DO SÓCIO PESSOA FÍSICA OU A RAZÃO SOCIAL E/OU NOME EMPRESARIAL DA PESSOA JURÍDICA E/OU NOME DO SÓCIO/RAZÃO SOCIAL DO SÓCIO ESTRANGEIRO              | -           |
| CNPJ/CPF DO SÓCIO                          | string           | CPF OU CNPJ DO SÓCIO (SÓCIO ESTRANGEIRO NÃO TEM ESTA INFORMAÇÃO).                                                                                       | -           |
| QUALIFICAÇÃO DO SÓCIO                      | integer          | CÓDIGO DA QUALIFICAÇÃO DO SÓCIO                                                                                                                         | NOT NULL    |
| DATA DE ENTRADA SOCIEDADE                  | date             | DATA DE ENTRADA NA SOCIEDADE                                                                                                                            | NOT NULL    |
| PAIS                                       | integer          | CÓDIGO PAÍS DO SÓCIO ESTRANGEIRO                                                                                                                        | -           |
| REPRESENTANTE LEGAL                        | string           | NÚMERO DO CPF DO REPRESENTANTE LEGAL                                                                                                                    | NOT NULL    |
| NOME DO REPRESENTANTE                      | string           | NOME DO REPRESENTANTE LEGAL                                                                                                                             | -           |
| QUALIFICAÇÃO DO REPRESENTANTE LEGAL        | integer          | CÓDIGO DA QUALIFICAÇÃO DO REPRESENTANTE LEGAL                                                                                                           | NOT NULL    |
| FAIXA ETÁRIA                               | integer          | CÓDIGO CORRESPONDENTE À FAIXA ETÁRIA DO SÓCIO                                                                                                           | NOT NULL    |

        """)
        st.markdown("""
            4.1.11. **Consolidada (Tabela utilizada pelos usuários)**
        """)
        st.markdown("""
            | Variável                                    | Tipo de Variável | Descrição                                                                                                                                               | Constraints |
|---------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| CNPJ BÁSICO                                | string           | NÚMERO BASE DE INSCRIÇÃO NO CNPJ (CADASTRO NACIONAL DA PESSOA JURÍDICA).                                                                                | NOT NULL    |
| IDENTIFICADOR DE SÓCIO                     | integer          | CÓDIGO DO IDENTIFICADOR DE SÓCIO: 1 – PESSOA JURÍDICA, 2 – PESSOA FÍSICA, 3 – ESTRANGEIRO                                                               | NOT NULL    |
| NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ) | string           | NOME DO SÓCIO PESSOA FÍSICA OU A RAZÃO SOCIAL E/OU NOME EMPRESARIAL DA PESSOA JURÍDICA E/OU NOME DO SÓCIO/RAZÃO SOCIAL DO SÓCIO ESTRANGEIRO              | -           |
| CNPJ/CPF DO SÓCIO                          | string           | CPF OU CNPJ DO SÓCIO (SÓCIO ESTRANGEIRO NÃO TEM ESTA INFORMAÇÃO).                                                                                       | -           |
| QUALIFICAÇÃO DO SÓCIO                      | integer          | CÓDIGO DA QUALIFICAÇÃO DO SÓCIO                                                                                                                         | NOT NULL    |
| DATA DE ENTRADA SOCIEDADE                  | date             | DATA DE ENTRADA NA SOCIEDADE                                                                                                                            | NOT NULL    |
| PAIS                                       | integer          | CÓDIGO PAÍS DO SÓCIO ESTRANGEIRO                                                                                                                        | -           |
| REPRESENTANTE LEGAL                        | string           | NÚMERO DO CPF DO REPRESENTANTE LEGAL                                                                                                                    | NOT NULL    |
| NOME DO REPRESENTANTE                      | string           | NOME DO REPRESENTANTE LEGAL                                                                                                                             | -           |
| QUALIFICAÇÃO DO REPRESENTANTE LEGAL        | integer          | CÓDIGO DA QUALIFICAÇÃO DO REPRESENTANTE LEGAL                                                                                                           | NOT NULL    |
| FAIXA ETÁRIA                               | integer          | CÓDIGO CORRESPONDENTE À FAIXA ETÁRIA DO SÓCIO                                                                                                           | NOT NULL    |

        """)
        st.markdown("")
        st.markdown("""
                4.2. **Métricas:**
        """)
        st.markdown("""
                        4.2.1. **Quantidade de registros:** 24.861.758.

                        4.2.2. **Referência:** Agosto de 2024.

                        4.2.3. **Última atualização:** 14 de agosto de 2024.

                        4.2.4. **Problemas Identificados:** Nenhum problema foi identificado até o momento.
        """)
        
        st.markdown("")
        st.html("<h2 id='disponibilizacao-dados' style='text-align: left; font-size:18px;'>5. Disponibilização dos Dados</h2>")
        st.markdown("""
                5.1. **Armazenamento e Formatado:** Estrutura de banco de dados organizada no PgAdmin (cada usuário precisa dessa estrutura armazenada em seu computador, atualmente).

                5.2. **Método de acesso aos dados:** Aplicativo instalado na máquina de cada usuário.

                5.3. **Interface de Acesso:** Aplicativo em RShiny.

                5.4. **Funcionalidades:** Consulta por CNAE, UF e município, auxiliando o mapeamento de novas empresas.

                5.5. **Nível de Divulgação:** Estadual e municipal, a depender da consulta realizada.

                5.6. **Área responsável pelo acesso:** Gestão de Dados – SPDO.
        """)
        st.markdown("")
        st.html("<h2 id='overview-dados' style='text-align: left; font-size:18px;'>6. Overview dos Dados</h2>")
        st.markdown("""
                6.1. **Demonstração dos Dados:**
        """)
        #st.image("assets/receita/demonstracao.png",use_container_width =True)
        st.markdown("")
        st.markdown("""
                6.2. **Estatísticas Descritivas:**
        """)
        #st.image("assets/receita/descritiva1.png",use_container_width =True)
        #st.image("assets/receita/descritiva2.png",use_container_width =True)
        st.markdown("")


def render_summary(selected_base):
    """
    Renderiza o resumo do relatório de metadados.
    """
    st.write("### Resumo do Relatório")
    
    if(selected_base == "alagoas" or selected_base =="pastorinho"):
        # Introdução
        st.markdown("**1. Introdução:**")
        st.write("""
        O relatório apresenta uma análise detalhada dos metadados utilizados nos projetos. Ele destaca a importância dos metadados na gestão, organização e interpretação eficaz das informações, com foco no projeto Economiza Alagoas, que visa divulgar informações públicas sobre vendas de produtos por meio da NFC-e.
        """)

        # Descrição das Fontes de Dados
        st.markdown("**2. Descrição das Fontes de Dados:**")
        st.write("""
        - Fonte: API Economiza Alagoas.
        - Forma de obtenção: Extração via API.
        - Periodicidade: Mensal, iniciada em maio de 2023.
        - Instituição responsável: SEFAZ-AL.
        """)

        # Tratamento dos Dados
        st.markdown("**3. Tratamento dos Dados:**")
        st.write("""
        - Apenas registros relacionados aos itens da pauta da SEFAZ-AL foram filtrados.
        - Transformações e padronizações não foram realizadas.
        - Os preços refletem o valor sem desconto e da última venda no período de 10 dias.
        """)

        # Qualidade dos Dados
        st.markdown("**4. Qualidade dos Dados:**")
        st.write("""
        - Total de registros: 1.639.127.
        - Estabelecimentos analisados: 1.208.
        - Problema identificado: Instabilidade na API em agosto de 2024.
        """)

        # Disponibilização dos Dados
        st.markdown("**5. Disponibilização dos Dados:**")
        st.write("""
        - Armazenamento: Arquivos CSV na rede local.
        - Acesso: Dashboard em Power BI com funcionalidades de análise de preços e cobertura.
        """)

        # Overview dos Dados
        st.markdown("**6. Overview dos Dados:**")
        st.write("""
        - Estatísticas descritivas e visualização dos dados são apresentadas no dashboard.
        """)
    elif(selected_base =="receita"):


        # Introdução
        st.markdown("**1. Introdução:**")
        st.write(
            """
            O relatório apresenta uma análise dos metadados associados a conjuntos de dados utilizados em projetos, 
            destacando a importância dos metadados para organização, acesso e interpretação eficaz dos dados. 
            Foca no Cadastro Nacional da Pessoa Jurídica (CNPJ), gerido pela Receita Federal do Brasil (RFB), 
            contendo informações sobre empresas e entidades de interesse tributário.
            """
        )

        # Descrição das Fontes de Dados
        st.markdown("**2. Descrição das Fontes de Dados:**")
        st.write(
            """
            - **Fonte:** Dados extraídos do site da RFB.
            - **Forma de obtenção:** Automação via Python.
            - **Periodicidade:** Trimestral, iniciada em julho de 2022.
            - **Responsabilidade:** Secretaria da Receita Federal e área de coleta não tradicional (SPDO).
            - **Unidade de análise:** Dados cadastrais, com abrangência nacional.
            - **Metodologia:** Investigação censitária com foco em empresas ativas.
            """
        )

        # Tratamento dos Dados
        st.markdown("**3. Tratamento dos Dados:**")
        st.write(
            """
            - **Limpeza:** Filtragem de empresas ativas com status específico.
            - **Transformações:** Consolidação de dados por meio de query SQL para unificar 10 tabelas.
            - **Padronização:** Não houve padronização adicional.
            - **Metodologia:** Atualizações mensais para incorporar alterações cadastrais e novos CNPJs.
            - **Coleta:** Realizada trimestralmente, com liberação em até 5 dias.
            """
        )

        # Qualidade dos Dados
        st.markdown("**4. Qualidade dos Dados:**")
        st.write(
            """
            - **Dicionário de Variáveis:** Listagem detalhada das variáveis, tipos e restrições em diferentes tabelas, como CNAEs, empresas, estabelecimentos e municípios.
            - **Métricas:** Base com 24.861.758 registros, atualizados até agosto de 2024, sem problemas identificados.
            """
        )

        # Disponibilização dos Dados
        st.markdown("**5. Disponibilização dos Dados:**")
        st.write(
            """
            - **Armazenamento:** Estrutura no PgAdmin, acessível por aplicativo local.
            - **Interface:** Aplicativo em RShiny para consultas dinâmicas por CNAE, UF e município.
            - **Nível de Divulgação:** Resultados estaduais e municipais.
            - **Responsável:** Gestão de Dados (SPDO).
            """
        )

        # Overview dos Dados
        st.markdown("**6. Overview dos Dados:**")
        st.write(
            """
            - **Demonstração:** Exemplos de dados disponíveis em tabelas ilustrativas.
            - **Estatísticas Descritivas:** Gráficos com informações detalhadas sobre a distribuição e características dos dados coletados.
            """
        )

