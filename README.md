# Disco Diffusion - Local Python Mode Only!

Forked from Disco Diffusion 5.4.

This version intended for local usage only. Note: Jupyter Notebook stuff removed for clarity, simplification when cleaning up PEP warnings and moving parameters to the top for easy editing, as well as adding more features :)

To run:
1. Follow instructions to set up Disco Diffusion for local use with Anaconda.
2. Open up configured anaconda instance 
3. Go to folder where you unzipped this.
4. python -m disco
5. Wait and pray you have enough VRAM and a good prompt ;)
6. Profit!

Bonus Features:
- beeps when a frame is finished or an error occurs
- GPU selection with 'cuda_device' variable at the top

Planned features:
- Front-end GUI
- add descriptions from cheatsheet to each field
- allow batch calls (queue)
- import of settings.txt files
- easy list of words to cancel out
- multi-prompts (given prompt, allow (n) parameters to change over time)
- prompt generator?




# Following text copied from original Disco Diffusion project

## Notebook Provenance 

Original notebook by Katherine Crowson (https://github.com/crowsonkb, https://twitter.com/RiversHaveWings). It uses either OpenAI's 256x256 unconditional ImageNet or Katherine Crowson's fine-tuned 512x512 diffusion model (https://github.com/openai/guided-diffusion), together with CLIP (https://github.com/openai/CLIP) to connect text prompts with images.

Modified by Daniel Russell (https://github.com/russelldc, https://twitter.com/danielrussruss) to include (hopefully) optimal params for quick generations in 15-100 timesteps rather than 1000, as well as more robust augmentations.

Further improvements from Dango233 and nshepperd helped improve the quality of diffusion in general, and especially so for shorter runs like this notebook aims to achieve.

Vark added code to load in multiple Clip models at once, which all prompts are evaluated against, which may greatly improve accuracy.

The latest zoom, pan, rotation, and keyframes features were taken from Chigozie Nri's VQGAN Zoom Notebook (https://github.com/chigozienri, https://twitter.com/chigozienri)

Advanced DangoCutn Cutout method is also from Dango223.

--

Somnai (https://twitter.com/Somnai_dreams) added 2D Diffusion animation techniques, QoL improvements and various implementations of tech and techniques, mostly listed in the changelog below.

3D animation implementation added by Adam Letts (https://twitter.com/gandamu_ml) in collaboration with Somnai.

Turbo feature by Chris Allen (https://twitter.com/zippy731)

Improvements to ability to run on local systems, Windows support, and dependency installation by HostsServer (https://twitter.com/HostsServer)

VR Mode by Tom Mason (https://twitter.com/nin_artificial)

Horizontal and Vertical symmetry functionality by nshepperd. Symmetry transformation_steps by huemin (https://twitter.com/huemin_art). Symmetry integration into Disco Diffusion by Dmitrii Tochilkin (https://twitter.com/cut_pow).

Warp and custom model support by Alex Spirin (https://twitter.com/devdef).
