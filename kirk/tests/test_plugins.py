"""
Unittests for framework module.
"""
import kirk
from kirk.sut import SUT
from kirk.framework import Framework


def test_sut(tmpdir):
    """
    Test if SUT implementations are correctly loaded.
    """
    suts = []
    suts.append(tmpdir / "sutA.py")
    suts.append(tmpdir / "sutB.py")
    suts.append(tmpdir / "sutC.txt")

    for index in range(0, len(suts)):
        suts[index].write(
            "from kirk.sut import SUT\n\n"
            f"class SUT{index}(SUT):\n"
            "    @property\n"
            "    def name(self) -> str:\n"
            f"        return 'mysut{index}'\n"
        )

    suts = kirk.discover_objects(SUT, str(tmpdir))

    assert len(suts) == 2


def test_framework(tmpdir):
    """
    Test if Framework implementations are correctly loaded.
    """
    suts = []
    suts.append(tmpdir / "frameworkA.py")
    suts.append(tmpdir / "frameworkB.py")
    suts.append(tmpdir / "frameworkC.txt")

    for index in range(0, len(suts)):
        suts[index].write(
            "from kirk.framework import Framework\n\n"
            f"class Framework{index}(Framework):\n"
            "    @property\n"
            "    def name(self) -> str:\n"
            f"        return 'fw{index}'\n"
        )

    suts = kirk.discover_objects(Framework, str(tmpdir))

    assert len(suts) == 2
