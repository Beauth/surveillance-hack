
Surveillance Hack system
===

## Youtube 



## Project Description

Smart security is the future and with the help of technology available today, an affordable intelligent video analytics system is within our reach. This application is a low-cost, adaptive and extensible surveillance system focused on identifying and alerting for potential campus intruders. It can integrate into an existing alarm system and provides customizable alerts for the user. It can process several IP cameras and can distinguish between someone who is in the face database and someone who is not (a potential intruder).

![Architecture](https://raw.githubusercontent.com/Beauth/clynica/master/docs/static/clynica_logo.png)

## How to Use

1) Clone Repo

```
git clone https://github.com/Beauth/surveillance-hack/
```

2) Pull Docker Image

```
docker pull spapinwar/surveillance-hack-codebreak
```

3) Run Docker image, make sure you mount your User directory as a volume so you can access your local files

```
docker run -v /Users/:/host -p 5000:5000 -t -i spapinwar/surveillance-hack-codebreak  /bin/bash
```

- First navigate to hosts as specified in previous step that the local volume will be mounted there
- Navigate to the home_surveillance project inside the volume within your Docker container
- Move into the system directory

```
cd system
```
4) Run the app
```
python WebApp.py
```
- Visit ```localhost:5000 ```
- Login Username: ```admin``` Password ```admin```


## Libraries Used
- Flask
- OpenCV
- sklearn
- Dlib

### Face Detection
 1. OpenCV Haar Cascade
 2. Dlib HOG (Histogram of oriented gradiants)
 
### facial recognition
1. Motion Object segmentation and Face Recognition
2. Face Recognition and Tracking



User story
---
```
The team was working all night on reducing the lag in face recognition and making it as fast as possible, with ranging from testing multiple models, solutions, and methodologies while tirelessly building the code that powers the solution over multiple cameras.
```

######  `CodeBreak 1.0`
