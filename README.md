
<h1 align="center" style="font-weight: bold;">📆 MYGES-CAL 💻</h1>


<p align="center">A simple way to add your MyGES schedule to your calendar !</p>


<p align="center">
<a href="https://github.com/ShaanCoding">📱 Visit this Project</a>
</p>

<h2 id="started">🚀 Getting started</h2>

Here's how to run this script locally.

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running the project.

- [NodeJS](https://nodejs.org/fr/download/prebuilt-installer)
- [myges-cli](https://github.com/quantumsheep/myges-cli)
- [icalendar](https://pypi.org/project/icalendar/)

When you installed myges-cli, you will need to connect to your MyGES account. Don't worry, this is a one-time action !

```bash
myges login
```

And you will be guided through the proccess.

<h3>Cloning</h3>

Here is how to clone the project :

```bash
git clone https://github.com/Hegowo/myges-cal.git
```

<h3>Starting</h3>

Here is how to start the project :

```bash
npm calendrier.py
```

After that, you will need to get information about the week you want to get by using, for example, this command :

```bash
myges agenda 19-09
```

You will need to insert the raw information that myges agenda gave you line per line into the pyhon script.
