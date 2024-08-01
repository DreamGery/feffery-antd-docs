import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdTable 表格'},
                {'title': '进阶功能'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTable 表格', level=2),
        fac.AntdParagraph('表格组件主要进阶功能示例。'),
    ]