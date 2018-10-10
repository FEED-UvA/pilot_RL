from psychopy import visual


rating_scale_args = dict(

    common_args=dict(
        stretch=2,
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
        scale='',
        labels=['Heel onprettig', '', 'Heel prettig']
    ),

    arousal=dict(
        low=0,
        high=8,
        tickMarks=[0, 8],
        scale='',
        labels=['Totaal niet opwindend', 'Heel opwindend']
    ),
    
    attractiveness=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale='',
        labels=['Heel onaantrekkelijk', '', 'Heel aantrekkeljk']
    ),

    dominance=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale='',
        labels=['Totaal niet dominant', '', 'Heel dominant']
    ),

    trustworthiness=dict(
        low=-4,
        high=4,
        tickMarks=[-4, 0, 4],
        scale='',
        labels=['Heel onbetrouwbaar', '', 'Heel betrouwbaar'],
    )

)


def construct_rating_scale(rating_attribute, win, pos=(0, -.75), name='pre_rating_scale', response='keyboard'):
    
    all_args = rating_scale_args['common_args'].copy()
    all_args.update(rating_scale_args[rating_attribute])
    
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
