from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from agents.reader_agent import ReaderAgent
from agents.insight_agent import InsightAgent
from agents.summary_agent import SummaryAgent
from agents.visualizer_agent import VisualizerAgent
from utils.logger import log_event

app = FastAPI(title="Multi-Agent Document Analyzer")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate agents
reader_agent = ReaderAgent()
insight_agent = InsightAgent()
summary_agent = SummaryAgent()
visualizer_agent = VisualizerAgent()

@app.get("/")
async def root():
    return {"message": "Multi-Agent Document Analyzer API running."}

@app.post("/analyze/")
async def analyze_document(file: UploadFile = File(...)):
    """
    Upload a document (PDF, DOCX, TXT) and get:
    - extracted text
    - AI-generated insights
    - AI-generated executive summary
    - word cloud chart (base64)
    """
    log_event(f"Received file: {file.filename}")
    content = await file.read()
    
    # Extract text from file
    text = reader_agent.extract_text(content, file.filename)
    
    # Run insight and summary agents in parallel
    insight_task = asyncio.create_task(insight_agent.generate_insights(text))
    summary_task = asyncio.create_task(summary_agent.summarize(text, ""))  # empty insights for now
    
    insights, summary_text = await asyncio.gather(insight_task, summary_task)
    
    # Generate word cloud chart
    chart_base64 = visualizer_agent.generate_wordcloud(text)
    
    return {
        "filename": file.filename,
        "text": text,
        "insights": insights,
        "summary": summary_text,
        "chart": chart_base64
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok"}

@app.get("/example")
async def example_endpoint():
    """
    Example endpoint to test API without uploading files
    """
    example_text = "This is a sample document text for testing the Multi-Agent Analyzer."
    insights_task = asyncio.create_task(insight_agent.generate_insights(example_text))
    summary_task = asyncio.create_task(summary_agent.summarize(example_text, ""))
    
    insights, summary_text = await asyncio.gather(insights_task, summary_task)
    chart_base64 = visualizer_agent.generate_wordcloud(example_text)
    
    return {
        "text": example_text,
        "insights": insights,
        "summary": summary_text,
        "chart": chart_base64
    }
