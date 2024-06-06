import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInputNumber(
                id='input-number-debounce-demo',
                debounceWait=500,
                style={'width': 200},
            ),
            fac.AntdText(id='input-number-debounce-demo-output'),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


@app.callback(
    Output('input-number-debounce-demo-output', 'children'),
    Input('input-number-debounce-demo', 'debounceValue'),
    prevent_initial_call=True,
)
def show_input_number_debounce_value(debounceValue):
    return f'debounceValue: {debounceValue}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInputNumber(
            id='input-number-debounce-demo',
            debounceWait=500,
            style={'width': 200},
        ),
        fac.AntdText(id='input-number-debounce-demo-output'),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)

...

@app.callback(
    Output('input-number-debounce-demo-output', 'children'),
    Input('input-number-debounce-demo', 'debounceValue'),
    prevent_initial_call=True,
)
def show_input_number_debounce_value(debounceValue):
    return f'debounceValue: {debounceValue}'
"""
    }
]