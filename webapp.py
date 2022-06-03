import streamlit as st
import json
from algorithm import KNearestNeighbours
from operator import itemgetter
import base64

with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'names.json', 'r+', encoding='utf-8') as f:
    app_titles = json.load(f)

def knn(test_point, k):
    target = [0 for item in app_titles]
    model = KNearestNeighbours(data, target, test_point, k=k)
    model.fit()
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of 10 recommendations < Change value of k for a different number >
    table = list()
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([app_titles[i][0], app_titles[i][2]])
    return table

def set_bg_hack(main_bg):
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('bcg.jpg')

# st.image('images.jpg', captio n=None, width=650, use_column_width=None, clamp=True, channels="RGB", output_format="auto")
if __name__ == '__main__':
    appnames = ['analytics',
 'animations',
 'appointments',
 'automate-content-processing',
 'automating-processes',
 'blank-canvas',
 'blogs',
 'bookings',
 'branding',
 'browsing',
 'business',
 'calendar',
 'charting',
 'chartingfreestyle-writin',
 'cloud',
 'collaboration',
 'collection',
 'communications',
 'company',
 'connection',
 'content',
 'content-classification',
 'control',
 'conversation',
 'creative-writing',
 'custom-apps',
 'dBMS',
 'daily-planner',
 'data',
 'data-analysis',
 'data-grading',
 'defence',
 'diagrams',
 'documentation',
 'dynamic-storage',
 'employee',
 'endpoint',
 'enterprise',
 'family safety',
 'files',
 'format',
 'graphics',
 'identity',
 'kids mode',
 'knowledge',
 'knowledge-sharing',
 'large-group-discussion',
 'letters',
 'machine-learning-models',
 'mail',
 'management',
 'mobile',
 'online-meetings',
 'operating-systems',
 'organisation',
 'personal-task',
 'presentation',
 'productivity',
 'progress',
 'protection',
 'publish',
 'reminders',
 'report',
 'resources',
 'save-photos',
 'schedule-meeting',
 'schedule-meetings',
 'scheduling-emails',
 'security',
 'services',
 'set-task',
 'small-group',
 'suite',
 'task',
 'threat',
 'vba',
 'video',
 'video-calling',
 'virtual-machine',
 'web-clipper']
    apps_ms = [title[0] for title in app_titles]
    st.header('----------------------- APPLITFY ----------------------------------App Recommendation System-----------') 
    apps = ['--Select--', 'App name based', 'Feature based']   
    app_options = st.selectbox('Select application:', apps)
    
    if app_options == 'App name based':
        app_select = st.selectbox('Select APP:', ['--Select--'] + apps_ms)
        if app_select == '--Select--':
            st.write('Select an APP')
        else:
            n = st.number_input('Number of APPs:', min_value=1, max_value=5, step=1)
            name_of_app = data[apps_ms.index(app_select)]
            test_point = name_of_app
            table = knn(test_point, n)
            for app_name, link in table:
                st.markdown(f"[{app_name}]({link})")
    elif app_options == apps[2]:
        options = st.multiselect('Select Features:', appnames)
        if options:
            version_score = st.slider('score:', 1, 10, 8)
            n = st.number_input('Number of APPs:', min_value=1, max_value=5, step=1)
            test_point = [1 if i in options else 0 for i in appnames]
            test_point.append(version_score)
            table = knn(test_point, n)
            for app_name, link in table:
                st.markdown(f"[{app_name}]({link})")
        else:
                st.write("This is an App Recommender application. "
                        "You can select the features and their working status.")
    else:
        st.write('Select option')