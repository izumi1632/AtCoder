N = int(input())

a = list(map(int , input().split()))
a.sort()

# 各チームの最弱は昇順ソート順に埋める。
# 以降は、チームの2番目→3番目の順に埋めていく。
print(sum(a[N::2]))


