from wordcloud import WordCloud
import base64
from io import BytesIO
import matplotlib.pyplot as plt

class VisualizerAgent:
    """
    Generates a word cloud image (base64) from extracted text.
    """

    def generate_wordcloud(self, text: str) -> str:
        # Handle empty text gracefully
        if not text or len(text.strip()) == 0:
            text = "No valid text extracted from document."

        try:
            wc = WordCloud(width=600, height=400, background_color="white").generate(text)
            plt.figure(figsize=(6, 4))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")

            buf = BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight")
            plt.close()
            buf.seek(0)
            return base64.b64encode(buf.read()).decode("utf-8")

        except Exception as e:
            # Return placeholder image if generation fails
            print(f"[VisualizerAgent] Error: {e}")
            fallback_text = "Word cloud could not be generated."
            wc = WordCloud(width=600, height=400, background_color="lightgray").generate(fallback_text)
            plt.figure(figsize=(6, 4))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")

            buf = BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight")
            plt.close()
            buf.seek(0)
            return base64.b64encode(buf.read()).decode("utf-8")
