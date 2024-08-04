import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdProgress(
                percent=80,
                strokeColor={'from': '#f067b4', 'to': '#81ffef'},
                style={'width': 200},
            ),
            fac.AntdProgress(
                percent=80,
                strokeColor={'from': '#f067b4', 'to': '#81ffef'},
                type='circle',
            ),
            fac.AntdProgress(
                percent=80,
                strokeColor={'from': '#f067b4', 'to': '#81ffef'},
                type='dashboard',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80,
            strokeColor={'from': '#f067b4', 'to': '#81ffef'},
            style={'width': 200},
        ),
        fac.AntdProgress(
            percent=80,
            strokeColor={'from': '#f067b4', 'to': '#81ffef'},
            type='circle',
        ),
        fac.AntdProgress(
            percent=80,
            strokeColor={'from': '#f067b4', 'to': '#81ffef'},
            type='dashboard',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]