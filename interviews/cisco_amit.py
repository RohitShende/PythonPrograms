def is_overlap(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    if e2 > s1 and e1 > s2:
        return True
    return False


if __name__ == '__main__':
    assert is_overlap((0, 65535), (4000, 8400)) is True
    assert is_overlap((0, 2000), (4000, 8400)) is False
