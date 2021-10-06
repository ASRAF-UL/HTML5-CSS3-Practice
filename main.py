from flask import Flask, render_template, request, jsonify
import os, random
import shutil
from PIL import Image
PEOPLE_FOLDER = "static/Output"
app = Flask(__name__)

filename_array = []
for filename in os.listdir(PEOPLE_FOLDER):
    filename = os.path.join(PEOPLE_FOLDER, filename)
    filename_array.append(filename)
print(len(filename_array))
index = 0

@app.route("/", methods=['GET', 'POST'])
def json():
    print("Hello")
    global index
    if request.method == 'POST':
            if request.form.get('Next') == 'next':
                index += 1
                # pass
                print("next: ", index)
                print(filename_array[index])

            elif request.form.get('Right') == 'right':
                index += 1
                #pass
                print('Right')
                replaced_image = filename_array[index].replace("static/Output/", "")
                replaced_label = filename_array[index].replace("static/Output/", "").replace(".jpeg", "")
                depz_image_folder = "DEPZ_LPD_data/images"
                depz_label_folder = "DEPZ_LPD_data/labels"
                image = os.path.join(depz_image_folder, replaced_image)
                label = os.path.join(depz_label_folder, replaced_label +  ".txt")
                if image:
                    shutil.move(image, "static/Right/images")
                    print('File from base images: ', image)
                else:
                    os.remove(filename_array[index])
                if label:
                    shutil.move(label, "static/Right/labels")
                    print('File from base label: ', label)
                else:
                    print('Not found')
            
            elif  request.form.get('Wrong') == 'wrong':
                index += 1
                # pass # do something else
                print("wrong")
                replaced_image = filename_array[index].replace("static/Output/", "")
                replaced_label = filename_array[index].replace("static/Output/", "").replace(".jpeg", "")
                depz_image_folder = "DEPZ_LPD_data/images"
                depz_label_folder = "DEPZ_LPD_data/labels"
                image = os.path.join(depz_image_folder, replaced_image)
                label = os.path.join(depz_label_folder, replaced_label +  ".txt")
                if image:
                    shutil.move(image, "static/Wrong/images")
                    print('File from base images: ', image)
                else:
                    os.remove(filename_array[index])
                    return
                if label:
                    shutil.move(label, "static/Wrong/labels")
                    print('File from base label: ', label)
                else:
                    print('Not found')
                    return

    return render_template("home.html", user_image = filename_array[index] )

@app.route('/image-path', methods=['GET'])
def image():
    print('New: ', filename_array[index], index)
    return filename_array[index]
if __name__ == '__main__':
   app.run(debug=True, host="localhost", port=8000)
