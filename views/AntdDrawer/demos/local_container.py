from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fac.AntdButton(
                '打开示例抽屉', id='drawer-local-demo-open', type='primary'
            ),
            fac.AntdDrawer(
                '示例内容',
                id='drawer-local-demo',
                title='局部容器抽屉示例',
                containerId='drawer-local-container',
            ),
        ],
        id='drawer-local-container',
        style={
            'height': 400,
            'border': '1px solid #e9ecef',
            'position': 'relative',
            'padding': 25,
            'overflowX': 'hidden',
        },
    )

    return demo_contents


@app.callback(
    Output('drawer-local-demo', 'visible'),
    Input('drawer-local-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_local_demo(nClicks):
    return True


code_string = [
    {
        'code': """
html.Div(
    [
        fac.AntdButton(
            '打开示例抽屉', id='drawer-local-demo-open', type='primary'
        ),
        fac.AntdDrawer(
            '示例内容',
            id='drawer-local-demo',
            title='局部容器抽屉示例',
            containerId='drawer-local-container',
        ),
    ],
    id='drawer-local-container',
    style={
        'height': 400,
        'border': '1px solid #e9ecef',
        'position': 'relative',
        'padding': 25,
        'overflowX': 'hidden',
    },
)

...

@app.callback(
    Output('drawer-local-demo', 'visible'),
    Input('drawer-local-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_local_demo(nClicks):
    return True
"""
    }
]