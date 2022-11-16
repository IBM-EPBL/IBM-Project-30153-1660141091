{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "563e4faf",
      "metadata": {
        "id": "563e4faf"
      },
      "source": [
        "# IBM Project Name: Real-Time Communication System Powered by AI for Specially Abled\n",
        "# TEAM ID: PNT2022TMID17658\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c497eb4d",
      "metadata": {
        "id": "c497eb4d"
      },
      "outputs": [],
      "source": [
        "\n",
        "import cv2 #mporting opencv Library this i to open camera and take the video\n",
        "import numpy as np # to convert image to array and expand dimensions\n",
        "from tensorflow.keras.models import load_model # to Load the saved model\n",
        "from tensorflow.keras.preprocessing import image # to preproccess the image\n",
        "model = load_model(\"dataset.h5\") # we are loading the saved moodek\n",
        "video = cv2.VideoCapture(0) # two parameters 1, bool 0 or 1, frame\n",
        "index = [\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\"]\n",
        "index=['A','B','C','D','E','F','G','H','I']\n",
        "#from playsound import playsound\n",
        "while(1):\n",
        "    success,frame = video.read()\n",
        "    cv2.imwrite(\"image.jpg\",frame)\n",
        "    img = image.load_img(\"image.jpg\",target_size = (64,64))\n",
        "    x = image.img_to_array(img)\n",
        "    x = np.expand_dims (x,axis = 0)\n",
        "    pred = np.argmax(model.predict(x),axis=1)\n",
        "    p = index [pred[0]]\n",
        "    print(\"predicted letter is: \"+ str(p))\n",
        "    #playSound(\"letter\"+str(str(index [p])+\"is detected\"))\n",
        "    cv2.putText (frame, \"predicted letter is \"+str(p), (100, 100), cv2. FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 4)\n",
        "    cv2.imshow(\"showcasewindow\", frame)\n",
        "    \n",
        "    if cv2.waitkey(1) & 0xFF == ord('a'):\n",
        "        break\n",
        "video.release()\n",
        "cv2.destroyAllwindows()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "e5fb95ee",
      "metadata": {
        "id": "e5fb95ee"
      },
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3.10.0 64-bit",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.0"
    },
    "vscode": {
      "interpreter": {
        "hash": "26de051ba29f2982a8de78e945f0abaf191376122a1563185a90213a26c5da77"
      }
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}