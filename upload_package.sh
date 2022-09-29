#!bin/bash
entrypoint=$(pwd)
sys_python=$(which python)
project_ver=0.09.16.2022
project_name=$(basename "$entrypoint")
project_url=$(git config --get remote.origin.url)
username=$HOME/.pypirc

if [ -f "$username" ]; then
    echo "File $username exists."
else
    echo "File $username does not exist."
    echo "Please create a file $username with the following content:"
    echo "[distutils]"
    echo "index-servers ="
    echo "    pypi"
    echo ""
    echo "[pypi]"
    echo "repository: https://upload.pypi.org/legacy/"
    echo "username: <your username>"
    echo "password: <your password>"
    exit 1
fi




sample_setup() {
cat <<EOF > setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="$project_name", 
    version="$project_ver",
    author="Nii Golightly",
    author_email="nlli@pm.me",
    description="$project_name ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="$project_url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
EOF

}

check_config() {
    if [ -f $entrypoint/setup.py ]; then
        echo "found setup.py"
        rm -rf $entrypoint/build
        rm -rf $entrypoint/dist
        rm -rf $entrypoint/*.egg-info
        # $sys_python setup.py sdist bdist_wheel
    else
        echo "adding setup.py to $entrypoint please check and edit as needed !then run again"
        sample_setup
        exit 1
    fi

}





git_project=$(git config --get remote.origin.url | sed 's/.*\/\(.*\)\.git/\1/')
if [[ $1 == "-t" ]] ; then
# ask for project version and pass it to setup.py
    # check if this is a git project
    if [ -d .git ]; then
        if [ "$git_project" == "$project_name" ]; then
            read -p "Did you remove any sensitive info and config your setup.py file ?  " -n 1 -r
            if [[ $REPLY =~ ^[Yy]$ ]]
            then
                echo "Please enter the project version number to upload to pypi"
                echo ""
                echo "example: 0.09.16.2022"
                echo ""
                read project_ver
                echo "building package"
                sample_setup
                check_config 
                echo " "
                # python setup.py sdist bdist_wheel
                echo "uploading package"
                # twine upload --repository testpypi dist/*
            else
                echo "please remove sensitive info and try again"
            fi

        else
            echo "git project name does not match project name"
            echo "please rename your git project to $project_name or edit the script"
            exit 1
        fi
    else
        echo "this is not a git project"
        echo "please make this a git project.. I need the url for the package home page on TestPyPI"
        exit 1
    fi
fi 




if [[ $1 == "-update" ]] ; then
    update_config
fi