s = ''.join(sorted(input()))
n = ''.join(sorted(input(),reverse=True))

if s < n:
    print('Yes')
else:
    print('No')