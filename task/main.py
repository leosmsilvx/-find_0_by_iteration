import solveEquation
from robocorp.tasks import task

#======================================================================================
#RUN THE CODE
#======================================================================================

@task
def main():
    solveEquation.inputs()

if __name__ == "__main__":
    main()