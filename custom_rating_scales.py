from psychopy import visual


rating_scale_args = dict(

    common_args=dict(
        stretch=1.5,
        marker=u'slider',
        size=1.0,
        precision=1,
        showValue=False,
        markerStart=0,
        showAccept=False,
        leftKeys = ['f'],
        rightKeys = ['j'],
        acceptKeys = ['space']
    ),

    valence=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale=''
    ),

    arousal=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale=''
    ),
    
    attractiveness=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale=''
    ),

    dominance=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale=''
    ),

    trustworthiness=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale=''
    )

)


def construct_rating_scale(rating_attribute, low_high, win, pos=(0, -.5), name='pre_rating_scale', response='keyboard'):
    
    all_args = rating_scale_args['common_args'].copy()
    these_args = rating_scale_args[rating_attribute]
    these_args['labels'] = [low_high[0]] + [''] + [low_high[1]]
    print(these_args)
    all_args.update(these_args)
    
    if response == 'mouse':
        all_args['mouseOnly'] = True
        all_args['singleClick'] = True        
    
    this_rating_scale = visual.RatingScale(
        win=win,
        name=name,
        pos=pos,
        **all_args
    )
    
    return this_rating_scale
