from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments_sorted = sorted(segments, key=lambda x: x.start)

    x = segments_sorted[0].end
    points = []

    for s in segments_sorted:
        if s.start > x:
            points.append(x)
            x = s.end
        else:
            x = min(x, s.end)
    points.append(x)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
