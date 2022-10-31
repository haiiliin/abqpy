import os


def test_mdb():
    os.chdir(os.path.dirname(__file__))
    os.system("python examples/Compression/compression.py")
    os.system("python examples/Compression/compression-output.py")
