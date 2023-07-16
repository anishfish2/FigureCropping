import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
import sys 
if __name__ == "__main__":
    image_path = sys.argv[1]
    ins = instanceSegmentation()
    ins.load_model("pointrend_resnet50.pkl")
    ins.segmentImage(image_path, show_bboxes=True, output_image_name="masked_image2.jpg")
