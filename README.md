<header>

# Full-Stack Workshop in Python Flask

</header>

<h2>

Project Set-up Instructions

</h2>

### Use these Commands for the Project setup:

### 1. Initialize an empty repository:

```
git init
```
### 2. sending the repo to github:

```
gh repo create <repo_name>          # creates a repo
git remote add origin <repo url>    #connecting local and remote repos
git branch -M main                  #creating a branch 
git push -u origin main             #pushing the final edits 
```
_*These commands will help you in creating a new repository on GitHub and link it to your local repository._

### 3.Create a virtual environment:

```
python -m venv env
```

### 4. Activate the virtual environment:<br>

```
./env/Scripts/activate
```

### 5. install flask: (For Safety purposes use pip3)

```
pip3 install flask
```

### 6. Freeze the requirements

```
pip freeze > requirements.txt
```
### 7. For running the project, use :
```
python app.py
```
<p> ( or ) </p>

```
flask run
```
- [x] By using all the above steps you will be able to create a basic flask project setup.Happy coding:)
###### _This Project Folder is created for the usage of Full-Stack Workshop_
