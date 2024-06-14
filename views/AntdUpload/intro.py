import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': '文件上传'},
                {'title': 'AntdUpload 上传'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdUpload 上传', level=2),
        fac.AntdParagraph('提供点击按钮触发的通用文件上传功能。'),
    ]