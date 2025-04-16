import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Supomos que cada evento sísmico tem medições de seis estações. 
# Para cada estação, extraímos 4 features por canal (por exemplo, para os canais T, R e V)
# Total de features por estação = 3 (canais) x 4 (features) = 12
# Com 6 estações, teremos um vetor de 72 features por evento.

# Exemplo: vamos criar dados simulados para 10 eventos
# Para simplicidade, usaremos valores aleatórios. No caso real, estes valores devem ser os extraídos dos ficheiros.

#Em vez de centroid entrar com RMS 

num_eventos = 10
num_estacoes = 6
features_por_estacao = {}

# Nome de cada feature extraída por estação (por exemplo, para um canal, podemos ter: pico, frequência dominante,
# amplitude do pico e centroide espectral). Aqui, vamos considerar os mesmos nomes para os três canais.
nomes_features = ['peak_T', 'peak_R', 'peak_V',
                  'dominant_freq_T', 'dominant_freq_R', 'dominant_freq_V',
                  'amp_peak_T', 'amp_peak_R', 'amp_peak_V',
                  'spectral_centroid_T', 'spectral_centroid_R', 'spectral_centroid_V'] # Utilizar RMS T, R, V no CF Json 

# Para cada estação, simula um DataFrame com as features para cada evento.
for estacao in range(1, num_estacoes+1):
    # Gerar dados simulados (valores aleatórios) para cada feature
    np.random.seed(estacao * 10)  # Seed para replicabilidade
    data_estacao = {
        nome: np.random.rand(num_eventos) * 10 for nome in nomes_features
    }
    df_estacao = pd.DataFrame(data_estacao)
    # Renomeia as colunas para indicar a estação
    df_estacao = df_estacao.add_prefix(f's{estacao}_')
    features_por_estacao[f'station_{estacao}'] = df_estacao

# Concatena os DataFrames de todas as estações na horizontal, um para cada evento.
df_eventos = pd.concat(features_por_estacao.values(), axis=1)

print("Exemplo de dados agregados para cada evento:")
print(df_eventos.head())

# Normalização dos dados para assegurar que todas as features têm a mesma escala.
scaler = StandardScaler()
features_scaled = scaler.fit_transform(df_eventos)

# Aplicação do K-Means. Escolhemos, por exemplo, k = 3 clusters (este valor pode ser ajustado).
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(features_scaled)

# Adiciona o rótulo de cluster ao DataFrame dos eventos
df_eventos['cluster'] = clusters
print("\nClusters atribuídos:")
print(df_eventos[['cluster']].head())

# Redução de dimensionalidade para visualização: usamos PCA para reduzir para 2 componentes.
pca = PCA(n_components=2)
pca_components = pca.fit_transform(features_scaled)

# Plotagem 
plt.figure(figsize=(8, 6))
plt.scatter(pca_components[:, 0], pca_components[:, 1], c=clusters, cmap='viridis', s=100)
plt.title('Clusters de Eventos Sísmicos Integrando 6 Estações')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.colorbar(label='Cluster')
plt.show()

# O que correposnde as componentes porncipais

