"use client";

import { useState } from "react";
import axios from "axios";

interface FileUploaderProps {
  onResult: (data: any) => void;
}

export default function FileUploader({ onResult }: FileUploaderProps) {
  const [loading, setLoading] = useState(false);

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
       const res = await axios.post(
      "http://localhost:8000/analyze/",
      formData,
      {
        headers: { "Content-Type": "multipart/form-data" },
        timeout: 120000,
      }
    );
      onResult(res.data);
    } catch (err: any) {
      console.error(err);
      alert("Error uploading document. Check backend running & CORS.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-4 border rounded shadow text-center">
      <input type="file" accept=".pdf,.docx,.txt" onChange={handleUpload} />
      {loading && <p className="mt-2">Processing document...</p>}
    </div>
  );
}
