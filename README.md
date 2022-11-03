# [SCUD Library](https://scud-library.herokuapp.com/docs) `A sample FastApi Project`

<br />

> Features 

| Status | Item | info | 
| --- | --- | --- |
| ✅ | **FastAPI** | For `Backend API` |
| ✅ | **Deployment** | `Heroku` |
| ✅ | **Database** | `MongoDB` |
| ❌ | **User_Outh** | JWT not configured |
| ❌ | **CI/CD** | Render Deployment Platform |

<br />

## ✨ API Endpoints
[lib](https://scud-library.herokuapp.com/docs)-`https://scud-library.herokuapp.com/docs`

### ✨ Manual Build

The process is basically the usual set up for any Python app: `environment` set up, `dependencies` install

<br />

> 👉 **Step 1** - `Download the code` from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-fastapi-stripe.git
$ cd scud-library
```

<br />

> 👉 **Step 2** - Mail me for the .env file

- Edit `MONGODB_URL` - provided by MongoDB Platform

<br />

> 👉 **Step 3** - `Install dependencies`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 **Step 4** - `Start the App`

```bash
$ uvicorn src.app:app --reload
```

Visit `http://localhost:8000` in your browser. For another port, use `--port 8099` directive.

<br />

## ✨ Credits & Links

- [FastAPI Framework](https://fastapi.tiangolo.com/) - The official website

<br />

---
