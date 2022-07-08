import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--n-batches", type=int, default=1, help="numbers of images to render")
parser.add_argument("-p", "--prompt", nargs='+', default=["Japanese city", "human:-2"],
                    help="Text prompt(s) to render")
parser.add_argument("-w", "--width_height", nargs='+', type=int, default=[1024, 768],
                    help="Width and height e.g. -w 1024 768 - Must be multiples of 64!")
parser.add_argument("-b", "--batch-size", type=int, default=1, help="size of batch")
parser.add_argument("-s", "--steps", type=int, default=250, help="Steps (iterations)")
parser.add_argument("-d", "--display-rate", type=int, default=25,
                    help="display rate of image while rendering, location: ./progress.png")
parser.add_argument("-o", "--output", type=str, default="DefaultDisco", help="output name of img")
parser.add_argument("-I", "--init-image", type=str, default=None, help="init noise from img")
parser.add_argument("-S", "--skip-steps", type=int, default=10, help="skip step while init noise from img")
parser.add_argument("--init-scale", type=int, default=1000, help="the init scale for init image")
parser.add_argument("-t", "--turbo", type=bool, default=False,
                    help="Turbo mode (only for 3D animations).\n"
                         "Skips diffusion steps and just uses depth map to warp images for skipped frames.\n"
                         "Speeds up rendering by 2x-4x, and may improve image coherence between frames.")

args = parser.parse_args()

print("Prompt: " + str(args.prompt))
print("Width/Height: " + str(args.width_height))
print("Steps: " + str(args.steps))
print("Turbo: " + str(args.turbo))
