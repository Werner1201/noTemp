import sys
import os
import fileinput


def createLinting():
    print("eslint")
    baixaDependencias()
    deletePack()
    updatePack()
    editEslint()
    criaPrettier()
    criaEditorConfig()


def baixaDependencias():
    os.system("yarn add eslint -D")
    os.system("yarn add prettier eslint-config-prettier eslint-plugin-prettier -D")
    os.system("yarn eslint --init")


def deletePack():
    path = "./"
    dir = os.listdir(path)
    for file in dir:
        if file == "package-lock.json":
            os.remove(file)


def updatePack():
    os.system("yarn")


def editEslint():
    text1 = "  plugins: ['prettier'],\n"
    text3 = "    'prettier/prettier': 'error', \n    'class-methods-use-this': 'off', \n    'no-param-reassign': 'off',\n    camelcase: 'off',\n    'no-unused-vars': ['error', {argsIgnorePattern: 'next'}],\n "
    abstPath = os.path.abspath("./")

    file_path = os.path.join(abstPath, ".eslintrc.js")

    for line in fileinput.FileInput(file_path, inplace=True, backup=".bak"):
        if "    'airbnb-base'," in line:
            line = line.replace(line, line + " 'prettier'\n")
            sys.stdout.write(line)
        elif "  ],\n" == line:
            line = line.replace(line, line + "\n" + text1)
            sys.stdout.write(line)
        elif "  rules: {" in line:
            line = line.replace(line, line + text3)
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)


def criaPrettier():
    text = "{\n  \"singleQuote\": true,\n  \"trailingComma\": \"es5\"\n}"
    f = open(".prettierrc", "w+")
    f.write(text)
    f.close()


def criaEditorConfig():
    text = "root = true\n\n[*]\nindent_style = space\nindent_size = 2\ncharset = utf-8\ntrim_trailing_whitespace = true\ninsert_final_newline = true"
    f = open(".editorconfig", "w+")
    f.write(text)
    f.close()


def createBackEndExpress():
    print('CRIEI')
    inicializaYarn()
    criaDiretorio()
    criaArquivos()
    editaPackage()
    criaNodemon()
    criaDiretorios("config", "src")
    criaArquivo("database.js", "src/config",
                "module.exports = {\n    dialect: 'dbnamedialect',\n	  host: 'localhost',\n	  port: '5433',\n	  username: 'username',\n	  password: 'pass',\n	  database: 'dbname',\n	  define: {\n		  timestamps: true,\n		  underscored: true,\n		  underscoredAll: true,\n	  },\n	};\n")
    criaDiretorios("database", "src")
    criaDiretorios("migrations", "src/database")
    criaDiretorios("seeds", "src/database")
    criaDiretorios("app", "src")
    criaDiretorios("controllers", "src/app")
    criaDiretorios("models", "src/app")
    addDependencies()
    criaArquivo(".sequelizerc", None, "const { resolve } = require(\"path\");\n\n	module.exports = {\n		config: resolve(__dirname, 'src', 'config', 'database.js'),\n		'models-path': resolve(__dirname, 'src', 'app', 'models'),\n  'migrations-path': resolve(__dirname, 'src', 'database', 'migrations'),\n  'seeders-path': resolve(__dirname, 'src', 'database', 'seeds'),\n};\n")


def addDependencies():
    os.system("yarn add sequelize")
    os.system("yarn add pg pg-hstore")
    os.system("yarn add sequelize-cli -D")


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


def criaDiretorios(diretorio, dentro):
    if dentro is not None:
        path = os.path.abspath("./{}".format(dentro))
        directory = diretorio
        pathFull = os.path.join(path, directory)
        print(pathFull)
        os.mkdir(pathFull)
    else:
        path = os.path.abspath("./")
        directory = diretorio
        pathFull = os.path.join(path, directory)
        print(pathFull)
        os.mkdir(pathFull)


def criaArquivos():
    path = os.path.abspath("./")
    pathSrc = os.path.join(path, "src")
    criaApp(pathSrc)
    criaServer(pathSrc)
    criaRoutes(pathSrc)


def criaArquivo(nome, dentro, text):
    if dentro is not None:
        path = os.path.abspath("./")
        pathSrc = os.path.join(path, dentro)
        f = open("{}/{}".format(pathSrc, nome), "w+")
        f.write(text)
        f.close()
    else:
        path = os.path.abspath("./")
        f = open("{}/{}".format(path, nome), "w+")
        f.write(text)
        f.close()


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
