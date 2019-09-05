"""
This script takes 1 parameter:
    * int - some number

Usage example:
    python script.py <int x>

"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
args = parser.parse_args()

x = args.x
print("Input: ", x)
print("Output: ", int(x)**2)
print("Result: ", f"{x}*{x}={int(x)**2}")

