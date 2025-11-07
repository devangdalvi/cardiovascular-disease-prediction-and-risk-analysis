# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import pyttsx3

def create_visualization(predictions):
    fig, ax = plt.subplots()
    conditions = list(predictions.keys())
    values = list(predictions.values())
    
    sns.barplot(x=conditions, y=values, palette="viridis", ax=ax)
    ax.set_title("Health Condition Predictions")
    ax.set_ylabel("Prediction")
    
    # Save the plot to a BytesIO object and encode it as a base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()#it will make it easy to display without saving
    img.close()
    
    # Prepare the text for text-to-speech
    prediction_texts = [f"{condition}: {'Yes' if result else 'No'}" for condition, result in predictions.items()]
    speech_text = "Here are the prediction results: " + ", ".join(prediction_texts)
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(speech_text)
    engine.runAndWait()
    
    return plot_url
