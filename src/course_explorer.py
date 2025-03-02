import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://courses.illinois.edu/cisapp/explorer/schedule"

def get_sections(year: str, term: str, subject: str, course_number: str):
    url = f"{BASE_URL}/{year}/{term}/{subject}/{course_number}.xml"
    print(f"Fetching sections from: {url}") # why tf doesn't this work

    try:
        response = requests.get(url)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        crns = []

        for section in root.findall(".//section"):
            crn = section.get("id")
            if crn:
                crns.append(crn)

        return crns

    except requests.exceptions.RequestException as e:
        print(f"Error fetching sections: {e}")
        return []

def get_professors(year: str, term: str, subject: str, course_number: str):
    crns = get_sections(year, term, subject, course_number)
    professors = set()

    for crn in crns:
        section_url = f"{BASE_URL}/{year}/{term}/{subject}/{course_number}/{crn}.xml"
        print(f"Fetching professor data from: {section_url}")  # Debugging

        try:
            response = requests.get(section_url)
            response.raise_for_status()

            root = ET.fromstring(response.content)

            for meeting in root.findall(".//meeting"):
                for instructor in meeting.findall(".//instructor"):
                    if instructor.text:
                        professors.add(instructor.text.strip())

        except requests.exceptions.RequestException as e:
            print(f"Error fetching section details for CRN {crn}: {e}")

    return list(professors)
