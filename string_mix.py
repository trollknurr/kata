import itertools
from collections import defaultdict


def mix(s1, s2):
    s1 = filter(lambda ch: ch.islower(), s1)
    s2 = filter(lambda ch: ch.islower(), s2)

    counts = defaultdict(lambda: [0, 0])

    for ch1, ch2 in itertools.izip_longest(s1, s2):
        counts[ch1][0] += 1
        counts[ch2][1] += 1

    data = defaultdict(list)
    for ch, (v1, v2) in counts.iteritems():
        v = max(v1, v2)
        if not ch or v <= 1:
            continue

        k = '1' if v1 > v2 else '2'
        k = '=' if v1 == v2 else k
        data[v].append((k, ch))

    items = sorted(data.items(), key=lambda (k, v): k, reverse=True)
    results = list()
    for count, chrs in items:
        eq_chrs = list()
        f_eq_chrs = list()
        s_eq_chrs = list()
        for mark, ch in chrs:
            {
                '=': eq_chrs,
                '1': f_eq_chrs,
                '2': s_eq_chrs,
            }.get(mark).append((mark, ch))
        for l in (f_eq_chrs, s_eq_chrs, eq_chrs):
            chrs = sorted(l, key=lambda (mark, ch): ch)
            for s_num, ch in chrs:
                results.append(
                    '{}:{}'.format(s_num, ch * count)
                )
    return '/'.join(results)
