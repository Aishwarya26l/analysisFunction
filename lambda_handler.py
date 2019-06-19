try:
    import requests
except ImportError:
    from botocore.vendored import requests
import json
import random


def getIndexPage():
    indexPage = """
    <html>
        <head>
            <meta charset="utf-8">
            <meta content="width=device-width,initial-scale=1,minimal-ui" name="viewport">
            <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/vue-material.min.css">
            <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/theme/default.css">
        </head>
        <body>
            <div id="app">
            <div class="md-layout">
                <div class="md-layout-item md-size-100">
                <md-card class="input-card">
                    <md-card-header>
                    <md-card-header-text>
                        <div class="md-title">Analysis Function - Analyse your text responses </div>
                    </md-card-header-text>
                    </md-card-header>
                    <md-card-content>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-size-50">
                        <md-field>
                            <label>Shown Block</label>
                            <md-textarea v-model="shownBlock"></md-textarea>
                        </md-field>
                        </div>
                        <div class="md-layout-item md-size-50">
                        <button class="button" v-on:click="staygo">
                            <span>Submit</span>
                        </button>
                        </div>
                    </div>
                    </md-card-content>
                </md-card>
                </div>
                <div class="md-layout-item md-size-100">
                <md-card class="input-card">
                    <md-card-header>
                    <md-card-header-text>
                        <div class="md-title">Input</div>
                    </md-card-header-text>
                    </md-card-header>
                    <md-card-content>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-size-50">
                        <md-field>
                            <label>Editable Block</label>
                            <md-textarea v-model="editableBlock"></md-textarea>
                        </md-field>
                        </div>
                        <div class="md-layout-item md-size-50">
                        <md-field>
                            <label>Hidden Block</label>
                            <md-textarea v-model="hiddenBlock"></md-textarea>
                        </md-field>
                        </div>
                    </div>
                    </md-card-content>
                </md-card>
                </div>
                <div class="md-layout-item md-size-100 output-card">
                <md-card>
                    <md-card-header>
                    <md-card-header-text>
                        <div class="md-title">Results</div>
                    </md-card-header-text>
                    </md-card-header>
                    <md-card-content>
                    <md-field>
                        <md-tabs>
                        <md-tab id="tab-htmlResults" md-label="HTML results">
                            <div v-html="answer.htmlFeedback"></div>
                        </md-tab>
                        <md-tab id="tab-jsonResults" md-label="JSON results">
                            <md-textarea
                            class="output-tab"
                            v-model="answer.jsonFeedback"
                            readonly
                            ></md-textarea>
                        </md-tab>
                        <md-tab id="tab-textResults" md-label="Text results">
                            <md-textarea
                            class="output-tab"
                            v-model="answer.textFeedback"
                            readonly
                            ></md-textarea>
                        </md-tab>
                        </md-tabs>
                    </md-field>
                    </md-card-content>
                </md-card>
                </div>
            </div>
            </div>
        </body> 
        <script src="https://unpkg.com/vue"></script>
        <script src="https://unpkg.com/vue-material@beta"></script>
        <script>
            Vue.use(VueMaterial.default)
            new Vue({
                el: '#app',
                data: {
                    shownBlock: "Introduction - \\n Please enter your text responses in the blocks below and hit Submit.",
                    hiddenBlock: "",
                    editableBlock: "How can I use firebase in my project?\\nWhat is firebase?\\nShould I use redux for state management?",   
                    answer:""
                },
                methods: {
                    staygo: function () {
                    const gatewayUrl = '';
                    fetch(gatewayUrl, {
                method: "POST",
                headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({userToken:"ABCDE",shown:{0:this.shownBlock},editable:{0:this.editableBlock}, hidden:{0:this.hiddenBlock}})
                }).then(response => {
                    return response.json()
                }).then(data => {
                    this.answer = JSON.parse(JSON.stringify(data))
                    })
                }
                }
            })
        </script>
        <style lang="scss" scoped>
            textarea {
                font-size: 1rem !important;
            }
            .md-card-header{
                padding-top: 0px;
            }
            .md-tabs{
                width:100%;
            }
            .md-tabs-container .md-tab textarea{
                height:100%;
            }
            .md-tab{
                min-height:500px;
            }
            .md-content{
                min-height:500px;
            }
            .md-card{
                overflow: hidden;
            }
            .input-card{
                height: 200px;
            }
            .output-tab{
                min-height:400px !important;
            }
            .output-card > .md-card > .md-card-content > .md-field{
                padding-top: 0px;
            }
            .button {
                display: inline-block;
                border-radius: 4px;
                background-color: #0099ff;
                border: none;
                color: #FFFFFF;
                text-align: center;
                font-size: 28px;
                padding: 20px;
                width: 200px;
                transition: all 0.5s;
                cursor: pointer;
                margin: 5px;
                //transform: translate(50%, 100%)
            }
            .button span {
                cursor: pointer;
                display: inline-block;
                position: relative;
                transition: 0.5s;
            }
            .button span:after {
                content: '>';
                position: absolute;
                opacity: 0;
                top: 0;
                right: -20px;
                transition: 0.5s;
            }
            .button:hover span {
                padding-right: 25px;
            }
            .button:hover span:after {
                opacity: 1;
                right: 0;
            }
        </style>
    </html>
    """
    return indexPage


def exec_tests(editableBlock, shownBlock, userToken, hiddenBlock):
    jsonResponse = {"results": []}

    # If hidden Block contains model, use model else Default
    if(hiddenBlock):
        model = hiddenBlock
    else:
        model = "Default"

    for oneTest in editableBlock:
        # Analysis Function goes here
        score = round(random.uniform(0, 1), 2)
        # Store the score with the corresponding test value
        result = {"model": model,
                  "score": score,
                  "testValue": oneTest}
        jsonResponse["results"].append(result)
    return jsonResponse


def calcFeedback(jsonResponse, userToken):
    jsonResponseData = json.loads(json.dumps(jsonResponse))
    resultContent = jsonResponseData.get('results')
    textResults = ""
    tableContents = ""
    textBackgroundColor = "#ffffff"
    allTestCaseResult = True
    if resultContent:
        for i in range(len(resultContent)):
            model = resultContent[i]["model"]
            score = resultContent[i]["score"]
            testValue = resultContent[i]["testValue"]

            if score > 0.5:
                textBackgroundColor = "#b2d8b2"  # Green
            else:
                textBackgroundColor = "#ffffff"

            textResults += ("INFO: Using {model} {testValue} got a score of {score}\n").format(
                model=model,
                testValue=testValue,
                score=score)
            tableContents = tableContents + """
            <tr bgcolor={color}>
                <td>{model}</td>
                <td>{score}</td>
                <td>{testValue}</td>
            </tr>
            """.format(color=textBackgroundColor, model=model, score=score,
                       testValue=testValue)
    htmlResults = """
        <html>
            <head>
                <meta charset="utf-8">
                <meta content="width=device-width,initial-scale=1,minimal-ui" name="viewport">
            </head>
            <body>
                <div>
                    <table>
                         <thead>
                            <tr>
                                <th>Model</th>
                                <th>Score</th>
                                <th>Test Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            {tableContents}
                        </tbody>
                    </table>
                </div>
            </body>
            <style>
            br {{
                display:block;
                content:"";
                margin:1rem
            }}
            table{{
                text-align:center
            }}
            </style>
        </html>
        """.format(tableContents=tableContents)
    allFeedback = {"isCorrect": True,
                   "htmlFeedback": htmlResults,
                   "textFeedback": textResults,
                   "jsonFeedback": json.dumps(jsonResponseData, indent=4, sort_keys=True)}
    return allFeedback


def lambda_handler(event, context):
    method = event.get('httpMethod', {})
    indexPage = getIndexPage()
    if method == 'GET':
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'text/html',
            },
            "body": indexPage
        }

    if method == 'POST':
        recResp = json.loads(event.get('body', {}))
        print("Received request")
        print(recResp)
        # Editable Block contains the text responses to analyse
        editableBlock = recResp["editable"]["0"].strip().splitlines()

        # Hidden Block contains the model to used, Uses Default if empty
        hiddenBlock = recResp["hidden"]["0"].strip()

        # Shown Block contains introduction/Helper text
        shownBlock = recResp["shown"]["0"]

        # User token specific to the user calling the function
        userToken = recResp["userToken"].strip()

        # Execute tests
        shownJsonResp = exec_tests(
            editableBlock, shownBlock, userToken, hiddenBlock)
        result = shownJsonResp["results"]
        jsonResp = {"results": result}
        print(jsonResp)
        # Form feedback
        allFeedback = calcFeedback(jsonResp, userToken)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body":  json.dumps({
                "isComplete": allFeedback["isCorrect"],
                "jsonFeedback": allFeedback["jsonFeedback"],
                "htmlFeedback": allFeedback["htmlFeedback"],
                "textFeedback": allFeedback["textFeedback"]
            })
        }
