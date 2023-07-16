# Hi! This is an implementation of Segment Anything, a project by Meta AI Research involving the segmentation of 2D images

I added scripts to easily obtain the objects which are segmented from these images. 

My files:
- Preprocessing directory
-- My personal attempt at a segmentation algorithm -> Relatively poor results
--- Added functionality for resizing images, extracting cropped images of detected faces, and removal of background for 2D images.
---- transparentBackground.py, resize.py, createMask.py and deleteBackground.py are scripts that can be run from terminal

- cropped_images directory
-- Default output folder for cropped 2D image objects

- test_images
-- Default folder for input 2D image objects

- segment.py & trial.ipynb
-- Python and Ipynb notebook I wrote, heavily inspired by "automatic_mask_generator_example.ipynb" given by Meta, that obtains cropped images

How to Use:
1. Download the "sam_vit_h_4b8939.pth" file from [here](https://github.com/facebookresearch/segment-anything#model-checkpoints) and place it in the "segment-anything" directory
2. Install the requirements from requirements.txt using 'pip install -r requirements.txt'
3. Place test images into 'test_images' folder
4. Run the command 'python segment.py [file-name]'
5. See the cropped image in the 'cropped_images' folder

Note:
The Segment Anything Model generates multiple images for different masks in the given image. My script only obtains the object contained by the largest mask by size. In order to generate objects by multiple or different masks, edit line 28 to reflect all/other values in 'sorted_anns'


Credits:
**[Meta AI Research, FAIR](https://ai.facebook.com/research/)**

[Alexander Kirillov](https://alexander-kirillov.github.io/), [Eric Mintun](https://ericmintun.github.io/), [Nikhila Ravi](https://nikhilaravi.com/), [Hanzi Mao](https://hanzimao.me/), Chloe Rolland, Laura Gustafson, [Tete Xiao](https://tetexiao.com), [Spencer Whitehead](https://www.spencerwhitehead.com/), Alex Berg, Wan-Yen Lo, [Piotr Dollar](https://pdollar.github.io/), [Ross Girshick](https://www.rossgirshick.info/)

[[`Paper`](https://ai.facebook.com/research/publications/segment-anything/)] [[`Project`](https://segment-anything.com/)] [[`Demo`](https://segment-anything.com/demo)] [[`Dataset`](https://segment-anything.com/dataset/index.html)] [[`Blog`](https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation/)] [[`BibTeX`](#citing-segment-anything)]

![SAM design](assets/model_diagram.png?raw=true)

The **Segment Anything Model (SAM)** produces high quality object masks from input prompts such as points or boxes, and it can be used to generate masks for all objects in an image. It has been trained on a [dataset](https://segment-anything.com/dataset/index.html) of 11 million images and 1.1 billion masks, and has strong zero-shot performance on a variety of segmentation tasks.

## License

The model is licensed under the [Apache 2.0 license](LICENSE).

## Contributing

See [contributing](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).

## Contributors

The Segment Anything project was made possible with the help of many contributors (alphabetical):

Aaron Adcock, Vaibhav Aggarwal, Morteza Behrooz, Cheng-Yang Fu, Ashley Gabriel, Ahuva Goldstand, Allen Goodman, Sumanth Gurram, Jiabo Hu, Somya Jain, Devansh Kukreja, Robert Kuo, Joshua Lane, Yanghao Li, Lilian Luong, Jitendra Malik, Mallika Malhotra, William Ngan, Omkar Parkhi, Nikhil Raina, Dirk Rowe, Neil Sejoor, Vanessa Stark, Bala Varadarajan, Bram Wasti, Zachary Winstrom

## Citing Segment Anything

If you use SAM or SA-1B in your research, please use the following BibTeX entry.

```
@article{kirillov2023segany,
  title={Segment Anything},
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```
