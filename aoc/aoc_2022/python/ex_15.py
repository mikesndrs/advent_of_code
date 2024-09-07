"""https://adventofcode.com/2022/day/15"""

import re


def puzzle1():
    target_row = 2000000
    input_filename = "aoc/aoc_2022/inputs/15.txt"
    beaconless_set = set()
    sensor_set = set()
    beacon_set = set()
    match_line = "Sensor at x=(.*), y=(.*):"
    match_line += " closest beacon is at x=(.*), y=(.*)"
    with open(input_filename) as f:
        for line in f:
            match = re.search(match_line, line.strip())
            sx = int(match.group(1))
            sy = int(match.group(2))
            bx = int(match.group(3))
            by = int(match.group(4))
            if sy == target_row:
                sensor_set.add(sx)
            if by == target_row:
                beacon_set.add(bx)
            dist = abs(sx - bx) + abs(sy - by)
            target_y_dist = abs(sy - target_row)
            if target_y_dist <= dist:
                for x in range(
                    sx - (dist - target_y_dist), sx + (dist - target_y_dist) + 1
                ):
                    beaconless_set.add(x)
    result1 = len(
        [x for x in beaconless_set if all([x not in sensor_set, x not in beacon_set])]
    )
    print(result1)


def puzzle2():
    input_filename = "aoc/aoc_2022/inputs/15.txt"
    match_line = "Sensor at x=(.*), y=(.*):"
    match_line += "closest beacon is at x=(.*), y=(.*)"
    with open(input_filename) as f:
        sensors = []
        max_val = 4000000
        for line in f:
            match = re.search(match_line, line.strip())
            sx = int(match.group(1))
            sy = int(match.group(2))
            bx = int(match.group(3))
            by = int(match.group(4))
            sensors.append([sx, sy, bx, by])
    for y in range(1, max_val + 1):
        beaconless_set = set()
        for [sx, sy, bx, by] in sensors:
            if sy == y:
                beaconless_set.add((sx, sx))
            dist = abs(sx - bx) + abs(sy - by)
            target_y_dist = abs(sy - y)
            if target_y_dist <= dist:
                beaconless_set.add(
                    (
                        max(1, sx - (dist - target_y_dist)),
                        min(max_val, sx + (dist - target_y_dist)),
                    )
                )
        sorted_set = sorted(beaconless_set, key=lambda x: x[0])
        row_end = 1
        for i in range(len(sorted_set)):
            start, end = sorted_set[i]
            if start <= row_end and end >= row_end:
                row_end = end
            elif end <= row_end:
                pass
            else:
                result = 4000000 * (row_end + 1) + y
                print(row_end + 1, y)
                print(result)
                return


if __name__ == "__main__":
    puzzle1()
    puzzle2()
