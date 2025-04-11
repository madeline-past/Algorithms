# Algorithms

**字符串算法、排序算法、递归、最小生成树之prim算法、dfs算法、bfs算法、贪婪算法、动态规划**

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

#### 整数二分

当要找的边界点在右半部分的左端点时

```python
l = 0
r = n-1
while l < r:
    m = (l + r) // 2
    if q[m] >= key:
        r = m
    else:
        l = m+1
```

最后ans=l=r，用l或r表示答案都可

当要找的边界点在左半部分的右端点时

```python
while l < r:
    m = (l + r +1) // 2
    if q[m] <= key:
        l = m
    else:
        r = m-1
```

[Python3二分查找库函数bisect(), bisect_left()和bisect_right()介绍_bisect left-CSDN博客](https://blog.csdn.net/YMWM_/article/details/122378152)

bisect.bisect和bisect.bisect_right返回大于x的第一个下标(相当于C++中的upper_bound)，bisect.bisect_left返回大于等于x的第一个下标(相当于C++中的lower_bound)。

bisect使用举例：896.最长上升子序列 II

```
import bisect

n = int(input())
q = list(map(int, input().split()))
st = [q[0]]

for i in range(1, n):
    # 如果大于栈顶元素, 压入
    if q[i] > st[-1]:
        st.append(q[i])
    # 否则, 替换栈中 大于等于 q[i] 的最小元素
    else:
        idx = bisect.bisect_left(st, q[i])
        st[idx] = q[i]

print(len(st))
```

数据结构：

树：可以用链表的方式存储每个节点的子节点



python常用库
dijkstra
https://www.acwing.com/solution/content/9964/



heapq:https://www.cnblogs.com/lwp-boy/p/13557104.html

from heapq import *

heapify

heappop

heappush

哈夫曼树

```
from heapq import *

n = int(input())
nums = list(map(int, input().split()))

heapify(nums)

res = 0
while len(nums) > 1:
    a = heappop(nums)
    b = heappop(nums)
    res += a + b
    heappush(nums, a + b)
print(res)
```



递归法
python3默认最大栈深度为999，从第7个测试用例开始就会爆栈；

我们可以通过sys模块中的setrecursionlimit来调整最大栈深度，这样也可以用递归的方法AC

```
import sys
sys.setrecursionlimit(6010)
```



考前速记模板：

快速幂

```python
def qmi(a, k, p):
    res = 1
    while k:
        if k&1:
            res = res*a%p
        k >>= 1
        a = a**2%p
    return res
```

快速幂求逆元：用费马小定理

```
def qmi(a, k, p):
    res = 1
    while k:
        if k&1:
            res = res*a%p
        k >>= 1
        a = a**2%p
    return res
    
n = int(input())
for _ in range(n):
    a, p = map(int, input().split(" "))
    ans = qmi(a, p-2, p)
    if a%p:
        print(ans)
    else:
        print("impossible")
```

线性筛：对于每个素数，筛掉所有以该素数作为最小素因子的数

这样每个数只会被筛掉一次

https://www.bilibili.com/video/BV1Ah411N7E4

```python
def prime(n):
    isprime = [True]*(n+1)
    p_list = []
    for i in range(2, n+1):
        if isprime[i]:
            p_list.append(i)
        for p in p_list:
            if p*i>n:
                break
            isprime[p*i] = False
            if i%p==0:
                break
	return len(p_list)
```





未看：[902. 最短编辑距离 - AcWing题库](https://www.acwing.com/problem/content/904/)

[899. 编辑距离 - AcWing题库](https://www.acwing.com/problem/content/901/)
