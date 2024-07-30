import os
import streamlit as st
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

interest_to_jobs = {
    'Technology': ['Software Developer', 'Data Scientist', 'Cybersecurity Analyst', 'UX/UI Designer', 'Artificial Intelligence Engineer', 'Cloud Architect', 'DevOps Engineer', 'Mobile App Developer', 'Quality Assurance Engineer', 'Network Engineer', 'Game Developer', 'Blockchain Developer', 'Machine Learning Engineer', 'Web Developer', 'Database Administrator'],
    'Healthcare': ['Registered Nurse', 'Medical Technologist', 'Physician Assistant', 'Pharmacist', 'Physical Therapist', 'Occupational Therapist', 'Speech-Language Pathologist', 'Nurse Practitioner', 'Medical Doctor (MD)', 'Radiologic Technologist', 'Dental Hygienist', 'Respiratory Therapist', 'Emergency Medical Technician (EMT)', 'Clinical Research Coordinator', 'Medical Laboratory Technician'],
    'Business': ['Marketing Specialist', 'Financial Analyst', 'Human Resources Manager', 'Operations Manager', 'Business Development Manager', 'Management Consultant', 'Supply Chain Manager', 'Risk Analyst', 'Project Manager', 'Data Analyst', 'Entrepreneur', 'Sales Manager', 'Accountant', 'Market Research Analyst', 'Logistics Coordinator'],
    'Education': ['Teacher', 'School Counselor', 'Education Administrator', 'Curriculum Developer', 'Special Education Teacher', 'Educational Psychologist', 'Instructional Designer', 'School Principal', 'Librarian', 'Educational Technologist', 'Admissions Counselor', 'Career Counselor', 'Academic Advisor', 'Student Affairs Coordinator', 'Online Course Developer'],
    'Engineering': ['Mechanical Engineer', 'Electrical Engineer', 'Civil Engineer', 'Aerospace Engineer', 'Chemical Engineer', 'Industrial Engineer', 'Environmental Engineer', 'Petroleum Engineer', 'Structural Engineer', 'Robotics Engineer'],
    'Finance': ['Investment Banker', 'Financial Advisor', 'Portfolio Manager', 'Actuary', 'Financial Controller', 'Credit Analyst', 'Treasury Analyst', 'Equity Research Analyst', 'Hedge Fund Manager', 'Insurance Underwriter'],
    'Creative Arts': ['Graphic Designer', 'Animator', 'Illustrator', 'Art Director', 'Creative Director', 'Film Director', 'Musician', 'Photographer', 'Copywriter', 'Content Creator'],
    'Science': ['Biologist', 'Chemist', 'Physicist', 'Environmental Scientist', 'Geologist', 'Marine Biologist', 'Astronomer', 'Epidemiologist', 'Pharmacologist', 'Neuroscientist'],
    'Hospitality and Tourism': ['Hotel Manager', 'Event Planner', 'Travel Agent', 'Tour Guide', 'Concierge', 'Restaurant Manager', 'Cruise Director', 'Resort Manager', 'Food and Beverage Manager', 'Hospitality Consultant']
}


def generate_jobs_prompt(area_of_interest, jobs):
    prompt = f"Suggested Jobs Related to {area_of_interest}\n\n"
    for job in jobs:
        prompt += f"- {job}\n"
    prompt += "\nPlease select a job from the above list:"
    return prompt.strip()

def generate_roadmap(selected_job, current_stage):
    try:
        prompt = f"Roadmap to Become a {selected_job}\n\n"
        prompt += f"You are currently at {current_stage} stage.\n"
        prompt += "Based on your current stage and the selected job, here is a personalized roadmap for you:\n"

        output = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=500
        )

        roadmap_text = output['choices'][0]['text']
        roadmap_with_headings = f"**Roadmap to Become a {selected_job}**\n\n"
        roadmap_with_headings += f"**Current Stage:** {current_stage}\n\n"
        roadmap_with_headings += "**Personalized Roadmap:**\n"
        roadmap_with_headings += roadmap_text

        return roadmap_with_headings
    except Exception as e:
        st.error(f"An error occurred: {e}")


def estimate_time_to_achieve(current_stage):
    time_estimations = {
        'High School': '4-6 years',
        'College': '2-4 years',
        'Entry-Level Professional': '1-3 years',
        'Mid-Level Professional': '3-5 years',
        'Senior Professional': '5+ years'
    }
    return time_estimations.get(current_stage, 'Unknown')

def main():
    st.set_page_config(page_title="Career Guidance Project", page_icon=":mortar_board:", layout="wide")

    st.title('Career Guidance')

    page = st.sidebar.radio("Navigation", ["Select Area of Interest", "Select Job", "Current Stage Details"])

    if page == "Select Area of Interest":
        area_of_interest = st.selectbox('Area of Interest', list(interest_to_jobs.keys()))
        if area_of_interest:
            st.session_state.area_of_interest = area_of_interest
            st.session_state.page = "Select Job"

    elif page == "Select Job":
        suggested_jobs = interest_to_jobs.get(st.session_state.get('area_of_interest', ''), [])
        
        job_chunks = [suggested_jobs[i:i+4] for i in range(0, len(suggested_jobs), 4)]
        for chunk in job_chunks:
            cols = st.columns(len(chunk))
            for col, job in zip(cols, chunk):
                if col.button(job, key=job):
                    st.session_state.selected_job = job
                    st.session_state.page = "Current Stage Details"

    elif page == "Current Stage Details":
        selected_job = st.session_state.get('selected_job', None)
        if selected_job:
            st.subheader(f'Selected Job: {selected_job}')
            current_stage = st.selectbox('Current Stage', ['High School', 'College', 'Entry-Level Professional', 'Mid-Level Professional', 'Senior Professional'])
            if st.button('Generate Roadmap'):
                roadmap = generate_roadmap(selected_job, current_stage)
                if roadmap:
                    st.write("Roadmap:")
                    st.write(roadmap)
                    st.write(f"Estimated time to achieve: {estimate_time_to_achieve(current_stage)}")
                else:
                    st.warning("Roadmap could not be generated.")
        else:
            st.write("Please select a job first from the 'Select Job' page.")

if __name__ == "__main__":
    main()
