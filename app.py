from flask import Flask,request,jsonify
import googletrans
#import nltk
translator=googletrans.Translator()

app=Flask(__name__)
@app.route('/' ,methods=['POST'])
def helloworld():
    data=request.get_json()

    text=str(data['queryResult']['parameters']['any'])
    language=data['queryResult']['parameters']['language']
    text = text.lower()
    lang=""
    lang=lang.join(language)
    lang=lang.lower()
    dict1=googletrans.LANGUAGES
    try:
        def GetKey(val):
            for key, value in dict1.items():
                if val == value:
                    return key
                if val==key:
                    return key
        langcode=GetKey(lang)
        text = text.replace('translate', "")
        text = text.replace('translate ', "")

        a = translator.translate(text, dest=langcode)
    except:

        err = "Unfortunately! i am not able to Process your Translation 🥺\nPlease Click /helpme to know more 🙏 \n @translateabcd_bot ❤"
        response1 = {
            "fulfillmentText": "{}".format(err)
        }
        return jsonify(response1)


    let=str(a)
    a1=let.split(",")[2]
    a2=a1.split("=")[1]

    response={
        "fulfillmentText":"{}".format(a2)
    }
    return jsonify(response)

if __name__=="__main__":
    app.run(debug=True)
