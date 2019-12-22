
Surveillance Hack system
===

## Youtube 



## Project Description



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
Will be adding in some time
```

######  `CodeBreak 1.0`
