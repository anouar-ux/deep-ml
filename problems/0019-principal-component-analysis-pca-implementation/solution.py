import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # 1. Centrage et réduction des données (standardisation)
    moy = np.mean(data, axis=0, keepdims=True)
    ecart_type = np.std(data, axis=0, ddof=1, keepdims=True)
    cdata = (data - moy) / ecart_type

    # 2. Matrice de corrélation
    V = (cdata.T @ cdata) / (data.shape[0] - 1)

    # 3. Valeurs et vecteurs propres (tri décroissant des k premiers)
    vals, eg = np.linalg.eigh(V)
    top_eg = eg[:, ::-1][:, :k]
    result = np.zeros_like(top_eg)

    for l in range(k):
        vec = top_eg[:, l]

        m = 0
        while m < len(vec) and np.abs(vec[m]) < 1e-10:
            m += 1
        
        if m < len(vec):
            vec = np.sign(vec[m]) * vec
            
        result[:, l] = vec

    return np.round(result, 4)
