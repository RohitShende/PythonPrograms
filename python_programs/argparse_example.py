import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--setup", help="takes the setup config json for already deployed setup")
args = parser.parse_args()
if args.setup:
    print(args.setup)
else:
    raise(Exception('Required argument --setup'))