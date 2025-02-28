# Algorithms

**字符串算法、排序算法、递归、最小生成树之prim算法、dfs算法、bfs算法、贪婪算法、动态规划**

### 排序

#### 快排quick sort

[AcWing 785. 快速排序算法的证明与边界分析 - AcWing](https://www.acwing.com/solution/content/16777/)

快排属于分治算法，分治算法都有三步：

分成子问题
递归处理子问题
子问题合并

```C
void quick_sort(int q[], int l, int r)
{
    //递归的终止情况
    //这里也可以写成if(l == r) return;
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

#### 归并merge_sort

归并是稳定的

归并需要新开一个和原数组一样大的一个数组

[AcWing 787. 归并排序的证明与边界分析 - AcWing](https://www.acwing.com/solution/content/16778/)

```c
void merge_sort(int q[], int l, int r)
{
    //递归的终止情况
    if(l >= r) return;

    //第一步：分成子问题
    int mid = l + r >> 1;

    //第二步：递归处理子问题
    merge_sort(q, l, mid ), merge_sort(q, mid + 1, r);

    //第三步：合并子问题
    int k = 0, i = l, j = mid + 1, tmp[r - l + 1];
    while(i <= mid && j <= r)
        if(q[i] <= q[j]) tmp[k++] = q[i++];
        else tmp[k++] = q[j++];
    while(i <= mid) tmp[k++] = q[i++];
    while(j <= r) tmp[k++] = q[j++];

    for(k = 0, i = l; i <= r; k++, i++) q[i] = tmp[k];
}
```

