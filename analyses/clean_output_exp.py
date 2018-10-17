import os
import os.path as op
import pandas as pd
import numpy as np


def clean(file, out_dir=op.abspath('data')):

    RATING_COLS = {'rating_attribute': 'attribute', 'session_name': 'session_condition',
                   'number_str': 'session_order', 'stim_file': 'image',
                   'pre_rating_scale.response': 'pre_rating_response',
                   'pre_rating_scale.rt': 'pre_rating_rt',
                   'post_rating_scale.response': 'post_rating_response',
                   'post_rating_scale.rt': 'post_rating_rt'}
    
    sub_name = op.basename(file).split('_')[0]
    df = pd.read_csv(file)
    
    rating_df = (df.loc[df.phase == 'pre_rating', RATING_COLS.keys()]
        .rename(columns=RATING_COLS)
        .melt(id_vars=['attribute', 'session_condition', 'session_order', 'image'],
              var_name='pre_post', value_name='rating',
              value_vars=['pre_rating_response', 'post_rating_response'])
        .dropna()
        .replace({'pre_rating_response': 'pre', 'post_rating_response': 'post'})
        .replace({'eerste': 'first', 'tweede': 'second'})
        .replace({'logs/%s/' % sub_name: ''}, regex=True)
    )

    rating_df = (rating_df.assign(rewardprob=[s.split('rewardprob-')[-1].split('_')[0] for s in rating_df.image])
        .assign(face_gender=[s.split('gender-')[-1].split('_')[0] for s in rating_df.image])
        .assign(face_id=[s.split('id-')[-1].split('_')[0] for s in rating_df.image])
        .assign(sub_id=sub_name)
    )

    LEARNING_COLS = {'condition': 'reward_choice', 'left_face': 'left_face', 'right_face': 'right_face',
                     'rewarded_resp': 'rewarded_resp', 'real_RL_response.rt': 'RT',
                     'real_RL_response.keys': 'actual_resp', 'real_RL_response.corr': 'rewarded',
                     'session_name': 'session'}

    learning_df = df.loc[df.phase == 'learning', LEARNING_COLS.keys()]
    learning_df = (learning_df
        .rename(columns=LEARNING_COLS)
        .replace({'logs/%s/' % sub_name: ''}, regex=True)
        .assign(correct_resp=['f' if int(op.basename(s).split('rewardprob-')[-1].split('_')[0]) in [80, 64] else 'j'
                              for s in learning_df.left_face])  # change this to use correct_resp
    )

    learning_df['correct'] = (learning_df.correct_resp == learning_df.actual_resp).astype(int)

    if not op.isdir(out_dir):
        os.makedirs(out_dir)
    
    rating_df.to_csv(op.join(out_dir, f'{sub_name}_phase-rating_events.tsv'), sep='\t', index=False)
    learning_df.to_csv(op.join(out_dir, f'{sub_name}_phase-learning_events.tsv'), sep='\t', index=False)


if __name__ == '__main__':

    test_file = 'backup_data/sub-99/sub-99_events.csv'
    clean(test_file)
