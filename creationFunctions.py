import sys
import os
import fileinput


def createBackEndExpress():
    print('CRIEI')
    inicializaYarn()
    criaDiretorio()
    criaArquivos()
    editaPackage()
    criaNodemon()


def inicializaYarn():
    os.system("yarn init -y")
    os.system("yarn add express")
    os.system("yarn add sucrase nodemon -D")


def criaDiretorio():
    path = os.path.abspath("./")
    directory = "src"
    pathFull = os.path.join(path, directory)
    print(pathFull)
    os.mkdir(pathFull)


def criaArquivos():
    path = os.path.abspath("./")
    pathSrc = os.path.join(path, "src")
    criaApp(pathSrc)
    criaServer(pathSrc)
    criaRoutes(pathSrc)


def criaApp(pathLocal):
    f = open("{}/app.js".format(pathLocal), "w+")
    f.write("import express from 'express';\n")
    f.write("import routes from './routes';\n")
    f.write("\n")
    f.write("class App {\n")
    f.write("  constructor() {\n")
    f.write("    this.server = express();\n")
    f.write("    this.middlewares();\n")
    f.write("    this.routes();\n")
    f.write("  }\n")
    f.write("\n")
    f.write("\n")
    f.write("  middlewares() {\n")
    f.write("    this.server.use(express.json());\n")
    f.write("  }\n")
    f.write("\n")
    f.write("  routes() {\n")
    f.write("    this.server.use(routes);\n")
    f.write("  }\n")
    f.write("}\n")
    f.write("\n")
    f.write("export default new App().server;\n")
    f.close()


def criaServer(pathLocal):
    text = "import app from './app';\n\napp.listen(3333);\n"
    f = open("{}/server.js".format(pathLocal), "w+")
    f.write(text)
    f.close()


def criaRoutes(pathLocal):
    text = "import { Router } from 'express';\n\nconst routes = new Router();\nroutes.get('/', (req, res) => res.json({message: \"Hello World\"}));\n\nexport default routes;\n"
    f = open("{}/routes.js".format(pathLocal), "w+")
    f.write(text)
    f.close()


def criaNodemon():
    text = "{\n  \"execMap\": {\n    \"js\": \"node -r sucrase/register\"\n  }\n}"
    f = open("nodemon.json", "w+")
    f.write(text)
    f.close()


def editaPackage():
    text = "\"scripts\": {\n  \"dev\": \"nodemon src/server.js\",\n  \"dev:debug\": \"nodemon --inspect src/server.js\"\n},"
    abstPath = os.path.abspath("./")

    file_path = os.path.join(abstPath, "package.json")

    for line in fileinput.FileInput(file_path, inplace=True, backup=".bak"):
        if "  \"license\": \"MIT\"," in line:
            line = line.replace(line, line+"\n"+text)
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)
