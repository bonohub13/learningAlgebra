# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 第1章: 数と式
#
# - - -
#
# ## 1節: 式の展開と因数分解
#
# 問1〜5は単純に同一の式の内の同類項を揃えることを扱っているため, ここでは扱われない

import numpy as np


# - - -
#
# ### 問6
#
# $$
# [a, b, c] = a \times x + b \times y + c \times z \space \space (a, b, cは全て定数)
# $$

def prob6(A: np.poly1d, B: np.poly1d):
    print("-"*40)
    print(f"A + B = \n{(A + B).c}")
    print(f"A - B = \n{(A - B).c}")
    print(f"3A = \n{(3*A).c}")
    print("-"*40)


# +
# (1)
## [x, y, z]
A = np.poly1d([1, -2, 4])
B = np.poly1d([3, 1, -2])
prob6(A, B)

# (2)
## [x^2, x, x^0]
A = np.poly1d([2, -3, -1])
B = np.poly1d([-3, 7, -2])
prob6(A, B)

# (3)
## [x^3, x^2, x, x^0]
A = np.poly1d([1, 0, -2, -3])
B = np.poly1d([-3, 2, -5, -1])
prob6(A, B)

# (4)
## [x^2, xy, y^2]
A = np.poly1d([2, -1, -1])
B = np.poly1d([1, 1, -3])
prob6(A, B)
# -

# - - -
#
# ### 問7
#
# $$
# A = 3x^2 - x + 1 \\
# B = -x^2 + 4x - 3
# $$
#
# これらを次の式で計算せよ


# +
def prob7(prob: str, ans: np.poly1d):
    print('-'*40)
    print(f"{prob} = \n{ans.c}")
    print('-'*40)

A = np.poly1d([3, -1, 1])
B = np.poly1d([-1, 4, -3])

# +
# (1)
prob7("3A - 2B", 3*A - 2*B)

# (2)
prob7("2B - (B - 2A)", 2*B - (B - 2*A))

# (3)
prob7("2(A - 3B) - 3(A + B)", 2*(A - 3*B) - 3*(A + B))
# -

# - - -
#
# ### 問8
#
# $$
# A = x^2 - 2xy - 3y^2 \\
# B = -x^2 + 3xy - 2y^2 \\
# C = x^2 - xy + y^2
# $$
#
# これらを次の式で計算せよ

prob8 = prob7
A = np.poly1d([1, -2, -3])
B = np.poly1d([-1, 3, -2])
C = np.poly1d([1, -1, 1])

# +
# (1)
prob8("2A + B - C", 2*A+B-C)

# (2)
prob8("A + 2B - 2(B - C)", A+2*B-2*(B-C))

# (3)
prob8("3(A - 2B) - 2(C - 3B)", 3*(A-2*B)-2*(C-3*B))


# -

# - - -
#
# ### 問9
#
# $$
# A = 3x^2 + 2x - 1 \\
# B = -x^2 + 2x + 4
# $$
#
# のとき, 次の式を満たす整式_X_を求めよ

# +
def prob9(X_1: list, X_2: list): # [X_scala, np.array([x^2, x, x^0])]
    # converting [int, np.array] into np.array(list of ints)
    tmpX_1 = [X_1[0]]
    for i in X_1[1]: tmpX_1.append(i)
    tmpX_1 = np.array(tmpX_1)
    tmpX_2 = [X_2[0]]
    for i in X_2[1]: tmpX_2.append(i)
    tmpX_2 = np.array(tmpX_2)
    # ======================================================
    ans = tmpX_1 - tmpX_2
    ans = 1/ans[0]*ans[1:] if abs(ans[0]) > 1 else ans[1:]
    ans = np.poly1d(ans)
    print(f"{'-'*40}\nX = \n{ans}\n{'-'*40}")
    
A = np.array([3, 2, -1])
B = np.array([-1, 2, 4])

# +
# (1)
## X-2A=2X-B
prob9([1, -2*A], [2, -1*B])

# (2)
## 3X-2B=X+4A
prob9([3, -2*B], [1, 4*A])


# -

# - - -
#
# ## 2節: 整式の乗法
#
# 問10〜13は単項式, 多項式同士の展開であるため, ここでは扱わない
#
# ### Pythonを用いた単項式・多項式同士の演算方法
# - Numpyを用いて単項式, 多項式の演算を行う際はpoly1dメソッドを用いると乗算を行うことができる
#     - しかし, 出力結果が$$ax^n + bx^{n-1} + \dots + cx^0$$のようになってしまう。<br/>これは複数種の項を含む式 (αx+βy+γzなど) を計算する際には向かない。そのため, poly1dメソッドのあとに.cをつけることで$$[a, b, \dots, c]$$のような出力結果となり, 項を出力しなくすることができる
#
# - - -
#
# ### 問14
#
# 次の式を計算せよ。

def prob14(prob: str, ans: np.poly1d):
    print('-'*40)
    print(f"{prob} =\n{ans.c}")
    print('-'*40)


# +
# (1)
## (x+y)^2 + (x-y)^2
prob14_1 = np.poly1d([1, 1])**2 + np.poly1d([1, -1])**2
prob14("(x + y)^2 + (x - y)^2", prob14_1)

# (2)
## (x + y)^2 - (x - y)^2
prob14_2 = np.poly1d([1, 1])**2 - np.poly1d([1, -1])**2
prob14("(x + y)^2 - (x - y)^2", prob14_2)

# (3)
## (x - 1)(x + 2) - x(x + 1)
prob14_3 = np.poly1d([1, -1])*np.poly1d([1, 2]) - np.poly1d([1, 0])*np.poly1d([1, 1])
prob14("(x - 1)(x + 2) - x(x + 1)", prob14_3)

# (4)
## (a + 2b)^2 - (a - 2b)(a + 2b)
prob14_4 = np.poly1d([1, 2])**2 - np.poly1d([1, -2])*np.poly1d([1, 2])
prob14("(a + 2b)^2 - (a - 2b)(a + 2b)", prob14_4)
# -


