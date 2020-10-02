# -*- coding:utf-8 -*-

"""Test gendiff module."""

import sys

from gendiff.file_loader import open_file
from gendiff.scripts.gendiff import main


def test_main(capfd):
    """Test main function."""
    sample_diff = set(
        open_file('tests/fixtures/diff_json_like.txt').split('\n'),
    )
    sys.argv = [
        'test1',
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test2',
        'tests/fixtures/before.yml',
        'tests/fixtures/after.yml',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test3',
        '-fjson_like',
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test4',
        '-fjson_like',
        'tests/fixtures/before.yml',
        'tests/fixtures/after.yml',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sample_diff = set(
        open_file('tests/fixtures/diff_plain.txt').split('\n'),
    )
    sys.argv = [
        'test5',
        '-fplain',
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test6',
        '-fplain',
        'tests/fixtures/before.yml',
        'tests/fixtures/after.yml',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sample_diff = set(
        open_file('tests/fixtures/diff_json.txt').split('\n'),
    )
    sys.argv = [
        'test7',
        '-fjson',
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test8',
        '-fjson',
        'tests/fixtures/before.yml',
        'tests/fixtures/after.yml',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''
