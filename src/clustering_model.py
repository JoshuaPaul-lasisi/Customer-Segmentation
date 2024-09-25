from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def apply_kmeans(data, n_clusters=5):
    """Apply KMeans clustering algorithm."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return clusters, kmeans

def reduce_dimensionality(data, n_components=2):
    """Apply PCA for dimensionality reduction."""
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(data)
    return reduced_data

def plot_clusters(data, clusters):
    """Plot the clusters using the reduced data."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=clusters, palette='viridis')
    plt.title('Customer Segments')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()

def run_clustering(scaled_data):
    """Run the clustering pipeline."""
    clusters, kmeans_model = apply_kmeans(scaled_data)
    reduced_data = reduce_dimensionality(scaled_data)
    plot_clusters(reduced_data, clusters)
    
    return clusters, kmeans_model
