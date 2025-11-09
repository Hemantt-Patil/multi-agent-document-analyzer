"use client";

import { useState } from "react";
import FileUploader from "./components/FileUploader";
import AnalysisResults from "./components/AnalysisResults";
import ChartView from "./components/ChartView";

export default function HomePage() {
  const [result, setResult] = useState<any>(null);

  return (
    <main className="max-w-5xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">📄 Multi-Agent Document Analyzer</h1>
      <FileUploader onResult={setResult} />
      {result && (
        <>
          <AnalysisResults result={result} />
          <ChartView imgBase64={result.chart} />
        </>
      )}
    </main>
  );
}
