# The GERALD Dataset

**Ge**rman **Ra**ilway **L**ightsignal **D**ataset

## General Information

The GERALD dataset contains 5000 individual images and annotations for 33554 occurring objects. Our focus was to annotate occuring lightsignals, however, we decided to also include annotations for other occuring objects (mostly static signs) for more a comprehensive understanding of the enviroment. From the three existing signalling systems used in Germany we decided to only gather images from the H/V- and Ks-Signalling-System. The additional Hl-Signalling-System is only in use on some tracks in the territory of former East Germany and we only found a few available videos showing these signals. The signal aspects of the H/V- and Ks-System form the main classes of the dataset:

* H/V-Signalling-System: Hp 0 (HV), Hp 1, Hp 2, Vr 0, Vr 1, Vr 2
* Ks-Signalling-System: Hp 0 (Ks), Ks 1, Ks 2

The following table specifies how many instances of each main class were labelled:

| Hp 0 (HV) | Hp 1   | Hp 2  | Vr 0   | Vr 1   | Vr 2  | Hp 0 (Ks) | Ks 1   | Ks 2  |
| --------- | ------ | ----- | ------ | ------ | ----- | --------- | ------ | ----- |
| 1700      | 973    | 627   | 1422   | 1115   | 554   | 807       | 1182   | 761   |
| 18.6 %    | 10.6 % | 6.9 % | 15.6 % | 12.2 % | 6.1 % | 8.8 %     | 12.9 % | 8.3 % |

## Further Information

Further Information about the dataset and how to use it can be found in the GitHub Repo: https://github.com/ifs-rwth-aachen/GERALD

There is also an accompying research paper that you can find here: https://doi.org/10.1177/09544097231166472. The paper includes more information about autonomous driving in railways in general and additional statistics and a deeper analysis of the dataset. We also show some exemplary results based on a YOLOv4 network trained on GERALD. 

### Data format
For easy data handling and revision the annotations come in the PASCAL VOC format. This format consists of individual XML-files for every image containing all labelled instances and additional information like width and height of the image. All further information that does not comply with the PASCAL VOC format is saved in the info.json (e.g. weather, light, source url). The PASCAL VOC uses a "difficult" tag for each annotation. For this case the difficult tag was used to indicate if the signal was relevant to the train conductor in that situation.

The images come in the .jpg format and are either 1280x720 or 1920x1080.

### How the data was gathered
The individual frames were created from video recordings from cab view rides which have been uploaded to YouTube. We asked the uploaders for permission to use their video material for our dataset. Microsofts video annotation tool [VoTT](https://github.com/microsoft/VoTT) was used to find and annotate relevant frames, in a second the step the images and annotations were revised and checked with [LabelImg](https://github.com/tzutalin/labelImg).

## Contact

Philipp Leibner - philipp.leibner@ifs.rwth-aachen.de 	Fabian Hampel - fabian.hampel@ifs.rwth-aachen.de

