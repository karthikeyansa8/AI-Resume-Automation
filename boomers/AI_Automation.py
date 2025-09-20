import google.generativeai as genai
from decouple import config
from dotenv import load_dotenv
import os
load_dotenv()

class Automation:
    def __init__(self):
        API_KEY = os.getenv("API_KEY")

        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel("gemini-2.0-flash")

        self.chat = model.start_chat()

        # print("Welcome to AI Automation Model!")
        
    
    def summary(self,input):
        prompt = f"""
        You are a professional resume writer. 
        Generate a **professional summary** (like an objective) for a resume based on these skills: {input}.

        Rules:
        - Write **one single paragraph**, 3 to 4 sentences long.
        - Use concise, professional language suitable for resumes.
        - Focus on **programming languages, tools, technologies**, and career strengths.
        - Do not use bullet points, numbers, or line breaks.
        - Provide only **one best version**, nothing else.
        """

        response = self.chat.send_message(content=prompt)
        return response.text.strip()
    
    def intern_description(self,input):
        prompt = f"""
        You are a professional resume writer. 
        Generate an internship description based on the intern role details: "{input}".

        Rules:
        - Output exactly **4 lines**, no more and no less.
        - Each line should be **18 to 25 words long**, detailed yet concise.
        - Use **active voice** with strong action verbs and measurable impact.
        - Separate each line with "||" (double pipe symbol) as a delimiter, not commas, not line breaks.
        - Provide only **one best version**, nothing else.
        """
        response = self.chat.send_message(content=prompt)
        return response.text.strip()

    def test(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Exiting the chat. Goodbye!")
                break
            response = self.chat.send_message(user_input)
            # response = chat.send_message(input_text)
            print("AI:", response.text)
            # return response.text
            
if __name__ == '__main__':
    Automation().test()