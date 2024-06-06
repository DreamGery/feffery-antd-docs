import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                fac.AntdText("size='small", code=True),
                innerTextOrientation='left',
            ),
            fac.AntdSegmentedColoring(
                size='small',
                min=-10,
                max=10,
                breakpoints=[0, 1, 2, 3, 4, 5],
                colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
            ),
            fac.AntdDivider(
                fac.AntdText("size='middle", code=True),
                innerTextOrientation='left',
            ),
            fac.AntdSegmentedColoring(
                min=-10,
                max=10,
                breakpoints=[0, 1, 2, 3, 4, 5],
                colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
            ),
            fac.AntdDivider(
                fac.AntdText("size='large", code=True),
                innerTextOrientation='left',
            ),
            fac.AntdSegmentedColoring(
                size='large',
                min=-10,
                max=10,
                breakpoints=[0, 1, 2, 3, 4, 5],
                colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            fac.AntdText("size='small", code=True),
            innerTextOrientation='left',
        ),
        fac.AntdSegmentedColoring(
            size='small',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
        ),
        fac.AntdDivider(
            fac.AntdText("size='middle", code=True),
            innerTextOrientation='left',
        ),
        fac.AntdSegmentedColoring(
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
        ),
        fac.AntdDivider(
            fac.AntdText("size='large", code=True),
            innerTextOrientation='left',
        ),
        fac.AntdSegmentedColoring(
            size='large',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
        ),
    ],
    direction='vertical',
)
"""
    }
]