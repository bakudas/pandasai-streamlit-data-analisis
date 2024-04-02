#%%
import pandas as pd
import random

# %%
# Gera listas aleatórias de dados
def generate_random_data(size):
    campanhas = [f'C{i}' for i in range(1, size+1)]
    datas = pd.to_datetime([f'2023-{random.randint(1, 12)}-{random.randint(1, 28)}' for _ in range(size)])
    canais = random.choices(['Facebook', 'Email', 'TV'], k=size)
    custos = [random.randint(500, 5000) for _ in range(size)]
    impressoes = [random.randint(5000, 50000) for _ in range(size)]
    cliques = [int(imp * 0.05) for imp in impressoes]
    leads = [int(cli * 0.2) for cli in cliques]
    conversoes = [random.randint(int(lead * 0.1), int(lead * 0.4)) for lead in leads]
    receitas = [conversão * random.randint(100, 1000) for conversão in conversoes]
    ticket_medio = [receita / max(conversão, 1) for receita, conversão in zip(receitas, conversoes)]
    rois = [receita / custo if custo > 0 else 0 for receita, custo in zip(receitas, custos)]
    clientes = [f'Cliente {i}' for i in range(1, size+1)]
    idades = [random.randint(20, 65) for _ in range(size)]
    sexos = random.choices(['M', 'F'], k=size)
    localizacoes = random.choices(['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Curitiba', 'Brasília'], k=size)
    rendas = [random.randint(20000, 100000) for _ in range(size)]
    produtos = [f'P{i}' for i in range(1, size+1)]
    categorias = random.choices(['Eletrônicos', 'Vestuário', 'Casa'], k=size)
    precos = [random.randint(100, 500) for _ in range(size)]

    return pd.DataFrame({
        'Campanha': campanhas,
        'Data': datas,
        'Canal': canais,
        'Custo': custos,
        'Impressões': impressoes,
        'Cliques': cliques,
        'Leads': leads,
        'Conversões': conversoes,
        'Receita': receitas,
        'Ticket Médio': ticket_medio,
        'ROI': rois,
        'Cliente': clientes,
        'Idade': idades,
        'Sexo': sexos,
        'Localização': localizacoes,
        'Renda': rendas,
        'Produto': produtos,
        'Categoria': categorias,
        'Preço': precos
    })

# %%
# Salva o DataFrame como CSV
df = generate_random_data(100)
df.to_csv('dataset_marketing.csv', index=False)
print('CSV gerado com sucesso! (dataset_marketing.csv)')

#%%
