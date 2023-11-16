"""
Adaugare teste la request-urile din Postman

- Vom testa din Postman, Simple Books API: https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Teste scrise doar in JavaScript
Documentatie teste Postman: https://learning.postman.com/docs/writing-scripts/test-scripts/

Trouble Shooting requests: https://learning.postman.com/docs/sending-requests/troubleshooting-api-requests/

How to run a collection:

Manually from Postman

Automation
Newman - run postamn collection in an automate way
Tutorial:
https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/


Windows:
Install NodeJS: https://nodejs.org/en/download?utm_source=blog
Install newman: open a terminal (in windows in search write terminal, or also you can use the git bash terminal, right click on desktop, open git bash)
In terminal/git bash write and press enter: npm install -g newman

MacOS:
Install NodeJS: https://nodejs.org/en/download?utm_source=blog
Install newman: brew install newman (if you don't have brew, You need to first install it)

Running collections (no need to do this step before workshop):
1. Export collection as JSON format on your local file
2. Rulam testele: newman run <fisier_json_as_collection>
3. Export newman report: newman run collection.json --reporters cli,html --reporter-html-export report.html

newman run simple_books

install newman-reporter-html
npm install -g newman-reporter-htmlextra

newman run simple_books.json --reporters cli,htmlextra --reporter-htmlextra-export report.html

"""
