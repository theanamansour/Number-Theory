import { useState } from "react";
import "./App.css";

function MillerRabinTab() {
  const [number, setNumber] = useState("");
  const [base, setBase] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleMillerRabin = async () => {
    setError("");
    setResult(null);
    setCopied(false);

    if (!number || isNaN(number) || Number(number) < 3 || Number(number) % 2 === 0) {
      setError("Please enter an odd integer greater than or equal to 3.");
      return;
    }

    if (!base || isNaN(base)) {
      setError("Please enter a valid base a.");
      return;
    }

    const nValue = Number(number);
    const aValue = Number(base);

    if (aValue <= 1 || aValue >= nValue - 1) {
      setError("Base a must satisfy 1 < a < n - 1.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/millerrabin/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          n: nValue,
          a: aValue
        })
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.detail || "Something went wrong.");
        return;
      }

      setResult(data);
    } catch {
      setError("Could not connect to backend.");
    }
  };

  const handleCopy = async () => {
    if (result) {
      const text = `Input: ${result.input}
Base: ${result.base}
Decomposition: ${result.decomposition}
Result: ${result.result}`;
      await navigator.clipboard.writeText(text);
      setCopied(true);
    }
  };

  const handleClear = () => {
    setNumber("");
    setBase("");
    setResult(null);
    setError("");
    setCopied(false);
  };

  return (
    <div className="tool-content">

      <main className="module-container">
        <div className="card">
          <input
            type="number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            placeholder="Enter an odd integer n"
          />

          <input
            type="number"
            value={base}
            onChange={(e) => setBase(e.target.value)}
            placeholder="Enter a base a"
          />

          <div className="button-row">
            <button onClick={handleMillerRabin}>Run Miller-Rabin</button>
            <button className="secondary" onClick={handleClear}>
              Clear
            </button>
          </div>

          {error && <p className="error">{error}</p>}

          {result && (
            <div className="result-box">
              <h2>Result</h2>
              <p><strong>Input:</strong> {result.input}</p>
              <p><strong>Base:</strong> {result.base}</p>
              <p><strong>Decomposition:</strong> {result.decomposition}</p>
              <p><strong>Result:</strong> {result.result}</p>

              <button onClick={handleCopy}>
                {copied ? "Copied!" : "Copy Result"}
              </button>

              <h3>Test Sequence</h3>
              <ul>
                {result.sequence.map((item, index) => (
                  <li key={index}>
                    {item.expression} = {item.value}
                  </li>
                ))}
              </ul>

              <h3>Step-by-Step Explanation</h3>
              <ol>
                {result.steps.map((step, index) => (
                  <li key={index}>{step}</li>
                ))}
              </ol>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default MillerRabinTab;