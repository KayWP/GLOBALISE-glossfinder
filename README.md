# GLOBALISE-glossfinder
## GlobaGloss.py
### What it does
This script takes a folder containing at least one transcription from the GLOBALISE project and tries to identify 'glosses' in every transcription within the folder. It outputs a .csv file, in which every row represents a gloss, with seperate columns for the term, indicator, explanation and the name of the scan on which the gloss appears.

### What you need
#### Transcriptions
At least one transcription from the [GLOBALISE dataverse](https://hdl.handle.net/10622/LVXSBW). The most recent version is available at Dataverse. Download either the .txt files or the .xml files. .txt files are a lot faster and take a lot less space on your harddrive. For the purposes of this script, they are identical.

#### Python
Required packages: Pandas, OS, TQDM, SYS

### How to use it


### What to do with it
Please be aware that the resulting dataset contains a lot of false positives, as the indicators used to identify glosses are also used in other ways in the Dutch language.

The notebook 'Exploring Glosses.ipynb' contains a few functions that help an user explore the data. If you are interested in exploring the data further or in doing other things with the data, do not hesitate to [reach out to GLOBALISE](https://globalise.huygens.knaw.nl/contact-us/).

Because every 'gloss' contains a reference to the archival scan on which it appears, the information can be further enriched using the inventory-level metadata from the National Archives of the Netherlands.
           
               
## Sample Data
Because running GlobaGloss.py against all available GLOBALISE transcriptions results in a large .csv file of roughly 3.3 million rows, To create the sample data, the script was run on a small subsection of the available GLOBALISE transcriptions. It can be loaded into the 'Exploring Glosses.ipynb' notebook. Please be aware that with a smaller subset of data, some terms might be glossed rarely or not at all. The contents of the sample data are representative in form, but not in content, for a larger dataset.
