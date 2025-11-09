"use client";

interface Props {
  imgBase64?: string;
}

export default function ChartView({ imgBase64 }: Props) {
  if (!imgBase64) return null;

  return (
    <div className="mt-4 bg-white p-4 rounded shadow">
      <h2 className="font-bold mb-2">📊 Word Cloud</h2>
      <img src={`data:image/png;base64,${imgBase64}`} alt="Word Cloud" />
    </div>
  );
}
