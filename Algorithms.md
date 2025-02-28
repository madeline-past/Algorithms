# Algorithms

### 排序

#### quick sort

快排属于分治算法，分治算法都有三步：

分成子问题
递归处理子问题
子问题合并

```C
void quick_sort(int q[], int l, int r)
{
    //递归的终止情况
    if(l >= r) return;

    //第一步：分成子问题
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while(i < j)
    {
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if(i < j) swap(q[i], q[j]);
    }

    //第二步：递归处理子问题
    quick_sort(q, l, j), quick_sort(q, j + 1, r);

    //第三步：子问题合并.快排这一步不需要操作，但归并排序的核心在这一步骤
}
```

