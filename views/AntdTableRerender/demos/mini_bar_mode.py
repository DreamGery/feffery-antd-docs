import numpy as np
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'mini-bar示例1',
                'dataIndex': 'mini-bar示例1',
                'renderOptions': {'renderType': 'mini-bar'},
                'width': '50%',
            },
            {
                'title': 'mini-bar示例2',
                'dataIndex': 'mini-bar示例2',
                'renderOptions': {
                    'renderType': 'mini-bar',
                    'tooltipCustomContent': """(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`""",
                },
                'width': '50%',
            },
        ],
        data=[
            {
                'mini-bar示例1': [np.random.rand() for i in range(25)],
                'mini-bar示例2': [np.random.rand() for i in range(25)],
            }
        ]
        * 3,
        bordered=True,
        style={'width': 300},
    )

    return demo_contents


code_string = [
    {
        'code': '''
fac.AntdTable(
    columns=[
        {
            'title': 'mini-bar示例1',
            'dataIndex': 'mini-bar示例1',
            'renderOptions': {'renderType': 'mini-bar'},
            'width': '50%',
        },
        {
            'title': 'mini-bar示例2',
            'dataIndex': 'mini-bar示例2',
            'renderOptions': {
                'renderType': 'mini-bar',
                'tooltipCustomContent': """(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`""",
            },
            'width': '50%',
        },
    ],
    data=[
        {
            'mini-bar示例1': [np.random.rand() for i in range(25)],
            'mini-bar示例2': [np.random.rand() for i in range(25)],
        }
    ]
    * 3,
    bordered=True,
    style={'width': 300},
)
'''
    }
]