# videntta
A simple yet powerful program that you can use to extract emails from Large files
If intergrated or expanded can be helpful to data researchers to gather emails from Large
document(s).


![videnta demo](https://user-images.githubusercontent.com/30528167/133281198-99551a87-1e34-415c-8b1b-febb57d33cd5.PNG)

<i>Note: You can either download or use git to have [videntta](https://github.com/stevemats/videntta).</i>


## Installation

```
git clone https://github.com/stevemats/videntta.git
```

git install -r requirements.txt

Now lets run in these few simple steps:

--Windows users
```sh
C:\Desktop> cd videntta    (assuming videntta is on Desktop)

C:\Desktop> dir            (To view the directory)

C:\Desktop> pip install -r requirements.txt  (install anything missing)

C:\Desktop> python vein.py  (Finally run the script)
```

--Linux Users

```sh
$ cd downloads\videntta       (Assuming videntta is on downloads)

$ ls                          (Displays files inside videntta)

$ pip install -r requirements.txt  (installs anything missing)

$ python vein.py              (Finally run the script)
```


After running the script, you'll be prompted with a menu. Choose the options according to your needs.

Current options:
- Email extraction from text documents.
- Email extraction from unified resource locators(URLs).
- A user friendly exit option for those just looking around.

You can also run tests using demo emails located within the Test-Doc folder. You can play around with it to see how it works and hopefully contribute on it. Thanks


## ToDo:
#### Extraction->
- Email extractions from microsoft word documents
- Support extractions from PDF, Word documents and other types of documents

#### Output-->
- Support export to pdf
- Custom Watermark Insertion in output document(for proper presentation)

### How to contribute

```
  > git clone https://github.com/stevemats/videntta.git
```
```
  > git pull
```
```
  > git checkout -b "your-branch-name"
```
 - Make changes and git add changes + git commit those changes
 - then finally:
```
  > git push (and remember to create a pr)
```
- you can also contribute to my own branches using
```
  git fetch origin <my-branch-here>
```
Then finally:
```
> git checkout <branch>
```

**The Project is open for Contribution**
