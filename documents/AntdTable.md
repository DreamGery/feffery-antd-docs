**columns：** *list*型，必填，无默认值

　　用于*配置表格字段信息*的必要参数，元素为单个或多个字典，每个字典对应一个独立字段的相关信息，每个字典的**键值对**有：

- title：必填，*string*型，用于设置该字段对应列显示的字段名
- dataIndex：必填，*string*型，相当于此字段的id，需在所有字段中保持唯一性
- width：可选，*int*或*string*型，用于设置该字段对应列的显示宽度，其中：
  - 当传入*int*型时，代表像素宽度，如`200`即代表200px
  - 当传入*string*型时，代表百分比宽度，如`'20%'`即代表占表格整体宽度的20%
  - **注意事项**
    - 当所有字段设置的像素宽度之和超过表格整体宽度时，会自动变成*向右滑动查看更多*的形式
    - 当所有字段设置的百分比宽度之和超过100%时，会自动归一化，譬如四个字段`width`都设置为`'100%'`，会自动转换为宽度`25%`
- align：可选，*string*型，设置列文字对齐方式，可选项有`'left'`（左对齐）、`'center'`（居中）、`'right'`（右对齐）
- editable：可选，*bool*型，设置对应列单元格数据是否支持*编辑*，默认为`False`即不可编辑
- fixed：可选，*string*型，用于设置对应列的冻结固定倚靠方式，可选项有`'left'`（靠左）、`'right'`（靠右）
- renderOptions：可选，*dict*型，用于设置对应列所有单元格的*再渲染模式*，其中：
  - renderType：*string*型，用于设置以何种方式进行*再渲染*，可选项有`'link'`（超链接）、`'ellipsis'`（超长内容省略模式）、`'mini-line'`（迷你折线图）、`'mini-bar'`（迷你柱状图）、`'mini-progress'`（迷你进度条）、`'mini-area'`（迷你面积图），其中*迷你图*模式需要**数据格式**满足要求，具体要求会在下面对应示例中进行演示
  - renderLinkText：可选，*string*型，用于在`renderType`设置为`'link'`时，指定超链接显示的文字内容，默认为`'链接🔗'`

**data：** *list*型，必填，无默认值

　　用于配合`columns`参数，定义每一行数据记录，元素为单个或多个字典，每个字典内的键值对都对应当前行记录下指定字段的值（其中键值对`key`用于为每行数据赋值*唯一*的id信息，若未传入，会默认补上从0开始增1的序列作为id），譬如下面的例子：

```Python
data = [
    {
        'key': '1',
        '字段1': 1,
        '字段2': 2,
        '字段3': 3
    },
    {
        'key': '2',
        '字段1': 1,
        '字段2': 2,
        '字段3': 3
    }
]
```

**sortOptions：** *dict*型，可选

　　用于对指定若干列设置*排序*功能，其中：

- multiple：*bool*型，用于设置是否开启组合排序模式，默认为`False`即不开启
- sortDataIndexes：*list*型，用于传入需要添加排序功能的若干字段`dataIndex`组成的列表，注意，当`multiple`设置为`True`时，`sortDataIndexes`传入的列表`dataIndex`顺序即代表了组合排序模式下的*排序优先级*

**pagination：** *dict*型，可选

　　用于配置表格自带的*翻页*组件的相关功能，其中：

- position：*string*型，用于设置分页部件的*位置*，可选项有`'topLeft'`（左上）、`'topCenter'`（上方居中）、`'topRight'`（右上）、`'bottomLeft'`（左下）、`'bottomCenter'`（下方居中）、`'bottomRight'`（右下），默认为`bottomRight`
- pagesize：*int*型，用于设置初始状态下每页显示的纪录行数，默认为`20`条
- current：*int*型，用于设置初始状态下停留在的*页码*，默认为`1`
- pageSizeOptions：*list*型，用于设置*单页尺寸*切换选项中的可选项，默认为`[20, 50, 100]`
- showQuickJumper：*bool*型，用于设置是否渲染*快速页码跳转*控件
- showTotalPrefix：*string*型，用于设置*总记录显示*内容，记录数值之前的文字内容，默认为`"共 "`
- showTotalSuffix：*string*型，用于设置*总记录显示*内容，记录数值之后的文字内容，默认为`" 条记录"`

**bordered：** *bool*型，可选，默认为`False`

　　用于设置是否为单元格四周渲染网格线

**maxWidth：** *int*型，可选

　　用于设置表格的最大像素高度，当本页所有记录行长度超出此上显时会以*冻结表头*滑轮滑动的方式进行浏览

**maxHeight：** *int*型，可选

　　用于设置表格的最大像素高度，当本页所有记录行长度超出此上显时会以*冻结表头*滑轮滑动的方式进行浏览

**currentData：** *list*型

　　用于在回调中捕获最近一次修改之后整张表对应的`data`格式列表，由*排序*与*编辑*操作触发更新

**recentlyChangedRow：** *dict*型

　　用于在回调中捕获最近一次进行单元格内容修改之后，对应的行记录字典，由*编辑*操作触发更新