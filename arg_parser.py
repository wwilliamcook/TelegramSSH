import argparse

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action='store_true')

    return parser.parse_args()
