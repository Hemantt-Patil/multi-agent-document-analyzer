"use client";

interface Props {
  result: any;
}

export default function AnalysisResults({ result }: Props) {
  if (!result) return null;

  return (
    <div className="bg-white p-4 rounded shadow mt-4">
      <h2 className="font-bold mb-2">📄 Document Text</h2>
      <pre className="whitespace-pre-wrap text-sm">{result.text}</pre>

      <h2 className="font-bold mt-4 mb-2">💡 Insights</h2>
      <pre className="whitespace-pre-wrap text-sm">{result.insights}</pre>

      <h2 className="font-bold mt-4 mb-2">📝 Summary</h2>
      <pre className="whitespace-pre-wrap text-sm">{result.summary}</pre>
    </div>
  );
}
