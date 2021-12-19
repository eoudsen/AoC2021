import numpy as np


def solve():
    scanners = load_scanners(open('input.txt').read())
    distances = get_distances(scanners)

    find_scanners(scanners, distances)
    beacons = find_beacons(scanners)

    return len(beacons)


def solve2():
    scanners = load_scanners(open('input.txt').read())
    distances = get_distances(scanners)

    scanner_positions = find_scanners(scanners, distances)

    max_value = 0
    for scanner1 in scanner_positions:
        for scanner2 in scanner_positions:
            if np.sum(np.abs(scanner1 - scanner2)) > max_value:
                max_value = np.sum(np.abs(scanner1 - scanner2))

    return max_value


def load_scanners(inp):
    reports = inp.split('\n\n')
    scanners = []

    for rep in reports:
        values = np.array([[int(i) for i in line.split(',')] for line in rep.splitlines()[1:]])
        scanners.append(values)

    return scanners


def get_distances(scanners):
    all_distances = []
    for scan in scanners:
        distances = []
        for point in scan:
            distances.append(np.sum(np.abs(scan - point), axis=1))
        all_distances.append(distances)
    return all_distances


def find_one_overlap(scan0, scan1, distances):
    for i, d0 in enumerate(distances[scan0]):
        for j, d1 in enumerate(distances[scan1]):
            overlaps = set(d0) & set(d1)
            if len(overlaps) >= 12:
                return i, j, overlaps


def find_positions(s0, s1, scanners, dists, p0, p1, overlaps):

    for d in overlaps:
        if d == 0:
            continue
        q0 = np.where(dists[s0][p0] == d)[0][0]
        q1 = np.where(dists[s1][p1] == d)[0][0]

        diff0 = scanners[s0][p0] - scanners[s0][q0]
        diff1 = scanners[s1][p1] - scanners[s1][q1]

        if len(set(np.abs(diff0))) < 3:
            continue

        order = []
        sign = []

        try:
            for i in range(3):
                idx = np.where(np.abs(diff1) == abs(diff0[i]))[0][0]
                order.append(idx)
                sign.append(diff1[idx] // diff0[i])

            new_orientation = scanners[s1][:, order] * np.array(sign)
        except:
            continue

        break

    scanner_position = scanners[s0][p0] - new_orientation[p1]
    new_coords = new_orientation + scanner_position

    return scanner_position, new_coords


def find_scanners(scanners, dists):
    scanners_found = {0}
    number_found = 1
    scanner_positions = [None] * len(scanners)
    scanner_positions[0] = np.array([0, 0, 0])

    while number_found < len(scanners):
        s0 = scanners_found.pop()

        for i in range(len(scanners)):
            if scanner_positions[i] is not None:
                continue
            overlaps = find_one_overlap(s0, i, dists)
            if not overlaps:
                continue
            position, coords = find_positions(s0, i, scanners, dists, *overlaps)
            scanner_positions[i] = position
            scanners[i] = coords
            scanners_found.add(i)
            number_found += 1

    return scanner_positions


def find_beacons(scanners):
    beacons = set()

    for blist in scanners:
        beacons.update([tuple(pos) for pos in blist])

    return beacons


if __name__ == "__main__":
    print(solve())
    print(solve2())
