import os
import glob
import json
# should read question_topics.csv and get file locations from there
# import pandas as pd

if __name__ == '__main__':

    TOPIC0 = 'Probability_density_function'
    TOPIC1 = 'Eigenvalues_and_eigenvectors'
    SOURCE_DIR = os.path.join('..', 'scrape_wiki_content', 'json_data')
    DIRECTORY = 'json_data_2_topics'

    if not os.path.exists(SOURCE_DIR):
        print(('The source directory of json files is expected at %s but can '
               'not be found. Please make sure the folder structure is '
               'correct or obtain the json files from'
               'https://github.com/MathEducationResources' % SOURCE_DIR))

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    fo_list = [x[0] for x in os.walk(SOURCE_DIR)]
    for folder in fo_list:
        Files = glob.glob(folder + '/*.json')
        for File in Files:

            fd = open(File, 'r')
            data = json.loads(fd.read())
            fd.close()

            if 'topics' in data:
                topics = data['topics']
                for topic in topics:
                    topic = str(topic)
                    if topic == TOPIC0:
                        topic = []
                        topic.append(TOPIC0)
                        data['topics'] = topic
                        question_id = data['ID']
                        location = os.path.join('json_data_2_topics',
                                                question_id + '.json')
                        with open(location, "w") as outfile:
                            json.dump(data, outfile, indent=4, sort_keys=True)

                    if topic == TOPIC1:
                        topic = []
                        topic.append(TOPIC1)
                        data['topics'] = topic
                        question_id = data['ID']
                        location = os.path.join('json_data_2_topics',
                                                question_id + '.json')
                        with open(location, "w") as outfile:
                            json.dump(data, outfile, indent=4, sort_keys=True)
