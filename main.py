import argparse

import vboa


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog='VBOA',
        description='Vision Based Obstacle Avoidance System',
        add_help=True)

    arg_parser.add_argument('--img', nargs='?',
                            help='Filepath to image for usage', type=str)

    arg_parser.add_argument('--imgdir', nargs='?',
                            help='Filepath to dir for usage', type=str)

    args = arg_parser.parse_args()

    vboa.run_app(
        img_file=args.img, imgs_dir=args.imgdir)
