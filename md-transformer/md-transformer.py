import os
from pathlib import Path

from google import genai
from google.genai import types

with Path('../EN-cv.tex').open() as tex_cv_file:
    tex_cv = tex_cv_file.read()

client = genai.Client(api_key=os.environ["GEMINI_TOKEN"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=tex_cv,
    config=types.GenerateContentConfig(
        system_instruction='You an editor which transform Tex text to Github Markdown. '
                           'You must preserve information, but adapt format. '
                           'Things like pictures can\'t be presented in MD and should me removed. '
                           'For job headers you have to use related header from MD. '
                           'Github MD can\'t use mailto: and tel: links'
                           'You must provide only MD text in output without any comments.',
    ),
)

with Path('../README.md').open("w") as readme_file:
    readme_file.write(response.text)
