import os.path as op
import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances


def select_stim_based_on_similarity(rating_df, face_gender='female', distance_metric='euclidean'):
    """ Selects pairs of stimuli (faces) based on the smallest distance
    between them in terms of ratings. """
    questions_df = pd.read_csv('ratings.csv')
    face_attr = np.unique(questions_df.loc[:, 'rating_attribute'].values)

    if 'stim_file' in rating_df.columns:
        rating_df = rating_df.set_index(keys='stim_file')
    
    ratings = rating_df.loc[rating_df.gender == face_gender, face_attr]
    rating_values = ratings.loc[:, face_attr].values
    dist = pairwise_distances(rating_values, metric=distance_metric)
    dist[np.diag_indices_from(dist)] = np.inf

    face_combis = []
    for _ in range(4):

        idx = np.unravel_index(dist.argmin(), dist.shape)
        face_combis.append([ratings.index[i] for i in idx])
        dist[idx[0], :] = np.inf
        dist[idx[1], :] = np.inf
        dist[:, idx[0]] = np.inf
        dist[:, idx[1]] = np.inf

    # Reorder such that the "best" pair goes together with the third best
    # pair (not the second best pair, etc.)
    face_combis = face_combis[0::2] + face_combis[1::2]
    half = int(len(face_combis) / 2)
    return [face_combis[:half], face_combis[half:]]

if __name__ == '__main__':

    rating_df = pd.read_csv('sub-99_face-ratings.csv', index_col='stim_file')
    select_stim_based_on_similarity(rating_df)