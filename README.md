# Does it fulfill the SOLID principles?
The refactored application covers the five SOLID principles to their fullest extent. Next up we explain why this is the case for each principle.
- __Single-responsibility__: In this case, the program complies with this principle because each of the classes has only one specific job (one for scraping the data, one for extracting it and one for writing it to file).
- __Open-closed__: If we wanted to scrape and extract the data for another site, we wouldn't need to modify the existing methods, but rather extend their class's capabilities.
- __Liskov substitution__: Although we do not have child classes in this simple example, if we wanted to implement a file writer for JSON files instead of CSV files, the methods to implement would be the same ones.
- __Interface segregation__: Once again, we do not implement interfaces because they're not standard in Python's programming ruleset. Regardless, we do not try to implement methods that aren't going to be used at least once.
- __Dependency inversion__: None of the classes implemented throughout the program rely on previous concretions, allowing them to be decoupled and depend only on higher-level abstractions.

# Building project locally
Install VirtualEnvironment (one time)

    python -m pip install virtualenv

Create virtual environment

    virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    python -m pip install -r requirements.txt

Install local src/ folder

    python -m pip install -e src 

# Building Docker image
At the root of the project run

    docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    docker run YOUR_NAME