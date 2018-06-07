import _plotly_utils.basevalidators


class FixedrangeValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='fixedrange', parent_name='layout.xaxis', **kwargs
    ):
        super(FixedrangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )