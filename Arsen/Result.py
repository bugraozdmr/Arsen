import os

class Result:
    def WriteOut(text,filename):
        path = os.getcwd()

        result_directory = os.path.join(path, "result")

        if not os.path.exists(result_directory):
            os.makedirs(result_directory)


        location = os.path.join(result_directory,filename)

        with open(location,"w") as file:
            file.write(text)