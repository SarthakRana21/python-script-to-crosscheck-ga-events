# python-script-to-crosscheck-ga-events
python script to crosscheck ga events


user need to install `python3`, `pip3`(latest version)


open `cmdprompt` or `terminal` and enter the following command 

`pip install cdifflib` if this gives error then enter `pip3 install cdifflib`


create 2 `.txt` text files "textfile1", "textfile2"

copy their paths and paste it on the script between double quotes


`# Open the two text files`

`with open("{path}", "r") as f1, open("{path}", "r") as f2:`

 save the script.
 
 
 *note: copy paste the parameters that are needed to be checked in textfile1 and from which it needs to be checked, copy paste on textfile2*


to run the script, open `cmdprompt` or `terminal` and enter the following command

`python3 checker.py` if this gives error then enter `python checker.py`
