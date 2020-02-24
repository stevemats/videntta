# videntta
A simple yet powerful program that you can use to extract emails from Large files
If intergrated or expanded can be helpful to data researchers to gather emails from Large
document(s).


![videntta-image](https://user-images.githubusercontent.com/30528167/75135355-5bc60580-56f2-11ea-9556-6828cce8becd.JPG)


## Installation
videntta requires [Python](https://python.org/) to run. Download [Videntta](https://github.com/stevemats/videntta/) program from github and store it in your desired folder location .e.g. Desktop. Next extract the zip and you are good to start. As simple as that.

Now lets run our program in your desired terminal. For demonstration I'll be using 
Command Prompt(cmd), Linux users can as well follow up:

--Windows users
```sh
C:\Desktop> cd videntta    (Videntta is the folder we extracted the program into)
C:\Desktop> dir            (To view the directory)
C:\Desktop> python vein.py  (Now running our program to extract the emails)
```

--Linux Users

```sh
$ cd downloads\videntta       (Assuming the downloaded program is in downloads)
$ ls                          (To view the files inside our folder)
$ python vein.py
```

After running the script, it will prompt you to input the path to your file( the one you extracting emails from..).
Email extraction will happen on the backend automatically and present an output on a separate file with the name
match(to present the email match output).

You can also run sample extraction process using the text document residing withing the Test-Doc folder.


## ToDo:
#### Extraction->
- EXtract emails from unified resource locators
- Email extractions from microsoft word documents
- Support extractions from PDF, Word documents and other types of documents

#### Output-->
- Support export to pdf
- Custom Watermark Insertion in output document(for proper presentation)

**The Project is open for Contribution**
