import pytest
from catch_exception import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Konrad\nGreta\nMike\nFrida\nEphron\nlist index out of range\n'