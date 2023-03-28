import argparse

import finding_differences
import makingdata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='The script will spot the differences between two images, circle and number them. ')
    parser.add_argument('--img', action='store', type=str, help='the path to image', default='imagines/titan1.jpg')
    parser.add_argument('--level', action='store', type=int, help='level game', default=3)
    parser.add_argument('--limit', action='store', type=int, help='limit difference', default=5)
    # python main.py --img '' --level 2 --limit 10

    # IMG1 = input('Enter path to image 1: ')
    # IMG2 = input('Enter path to image 2: ')
    args = parser.parse_args()
    IMG = args.img
    Level = args.level
    Limit = args.limit
    makingdata.processing_data()
    finding_differences.spotting()
    print("BuiDaoDuyAnh_21020263")
